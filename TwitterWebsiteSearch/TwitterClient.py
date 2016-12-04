import requests
from requests import Request, Session
from requests.packages.urllib3.util import Retry
from requests.adapters import HTTPAdapter
from datetime import datetime, timezone
from time import sleep
import lxml
import lxml.html as lh
from urllib.parse import quote, urlsplit
import re
from operator import itemgetter
from copy import deepcopy

# import logging
# logging.basicConfig(level=logging.DEBUG)

# import time
# def timing(f):
#     def wrap(*args):
#         time1 = time.time()
#         ret = f(*args)
#         time2 = time.time()
#         print("{} function took {:0.3f} ms".format(f.__name__, (time2-time1)*1000.0))
#         return ret
#     return wrap


class TwitterClient():
    
    FIDDLER_DEBUG = False

    @staticmethod
    def init_default_session(retrys=5,backoff_factor=0.1):
        session = Session()
        session.headers.update(
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
            'Accept-Encoding' : 'gzip, deflate, sdch, br',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
            'X-Requested-With': 'XMLHttpRequest'})
        retries = Retry(total=retrys,
                backoff_factor=backoff_factor,
                status_forcelist=[ 500, 502, 503, 504 ])
        session.mount('https://', HTTPAdapter(max_retries=retries))

        if TwitterClient.FIDDLER_DEBUG:
            proxies = {'http': 'http://127.0.0.1:8888', 'https': 'https://127.0.0.1:8888'}
            session.proxies.update(proxies)

        return session

    def __init__(self, 
            session=None,
            timeout=12,
            continue_on_empty_result=True):
        
        if session is None:
            session = self.init_default_session()
        self.session = session
        self.timeout = timeout
        self.continue_on_empty_result = continue_on_empty_result
        self.search_url = 'https://twitter.com/i/search/timeline'
        self.user_url = 'https://twitter.com/i/profiles/show/{username}/timeline/tweets'

    def search_query(self, queryBuilder, raw_query_str=None):
      
        if raw_query_str is None:
            raw_query_str = queryBuilder.build()

        request = self._prepare_request(self.search_url, raw_query_str)
        resp = self._execute_request(request)
        resp_json = resp.json()

        # Extract Results
        tweets = []
        if resp_json is not None and resp_json['items_html'] is not None:
            tweets = self.parse_tweets(resp_json['items_html']) 
        
        next_query = deepcopy(queryBuilder)
        next_query.max_position = resp_json.get('min_position') #switch the labels because twitter mislabels them
        next_query.min_position = resp_json.get('max_position')
        next_query.reset_error_state = False

        min_id = max_id = None

        if len(tweets) > 0:
            min_id = tweets[0]['id_str']
            max_id = tweets[1]['id_str']

        retval = {
                '_request': request,
                '_response_raw': resp,
                '_response_json': resp_json,
                'refresh_query': queryBuilder,
                'next_query': next_query,
                'tweets': tweets,
                'min_id': min_id,
                'max_id': max_id
            }
        return retval

    def user_query(self, user):
        raise NotImplementedError

    def get_search_iterator_2(self, search_query):
        
        # determine if this is the first query or a continuation.
        search_query.autoset_reset_error_state()

        result = self.search_query(search_query)
        next_query = result['next_query']
        yield result

        while True:

            if len(result['tweets']) == 0:
                if not self.continue_on_empty_result:
                    print('No tweets returned terminating program')
                    break
                else:
                    break
                    # TODO remimplement

            result = self.search_query(next_query)
            next_query = result['next_query']

            yield result



    def get_search_iterator(self, queryBuilder):
        qb = qb_prev = deepcopy(queryBuilder)

        result = self.search_query(qb)
        prev_min_tweetId = None
        yield result

        while True:

            if len(result['tweets']) == 0:
                if not self.continue_on_empty_result:
                    print('No tweets returned terminating program')
                    break
                else:
                    # Sometimes the API stops returning tweets even when there are more
                    # we can try to find these tweets by modifying the max_position parameter.
                    int_minId = int(qb.min_tweetId)
                    for x in range(8, len(qb.min_tweetId)): #TODO impl something more sophisticated 
                        qb.min_tweetId = int_minId - 10**x
                        result = self.search(qb)
                        if len(result['tweets']) > 0:
                            break
                    else:
                        print('No tweets returned terminating program')
                        # if we didnt find any point to continue from, break.
                        break

            if qb.max_tweetId is None:
                qb.max_tweetId = result['tweets'][0]['id_str']
            
            # In a high volume search query like 'a' must use the max_tweet_id provided by the result,
            # otherwise the same results will be returned many times. (only happens during the first ~10 pages of results)
            res_min_pos = result['response_json'].get('min_position')
            if res_min_pos is not None:
                split = res_min_pos.split('-')
                qb.max_tweetId = split[2]

            prev_min_tweetId = qb.min_tweetId
            qb.min_tweetId = result['tweets'][-1]['id_str']

            # If the current request returns the same tweets as the last
            # the query is configured wrong
            # TODO create more accurate metric
            if prev_min_tweetId is qb.min_tweetId:
                break

            result = self.search_query(qb)
            
            yield result
    
    def _execute_request(self, prepared_request):
        try:
            if TwitterClient.FIDDLER_DEBUG:
                result = self.session.send(prepared_request, timeout=self.timeout, verify=False)
            else:
                result = self.session.send(prepared_request, timeout=self.timeout)
            return result
        except requests.exceptions.Timeout as e:
            raise

    def _prepare_request(self, url, payload_str):
        req = Request('GET', url, params=payload_str, cookies={})
        return self.session.prepare_request(req)
    
    @staticmethod
    def _encode_max_postion_param(min, max):
        return "TWEET-{0}-{1}".format(min, max)

    def parse_tweets(self, items_html):
        try:
            html = lh.fromstring(items_html)
        except lxml.etree.ParserError as e:
            return []
        tweets = []
        for li in html.cssselect('li.js-stream-item'):
            
            # Check if is a tweet type element
            if 'data-item-id' not in li.attrib:
                continue
            tweet = self._parse_tweet(li)
            if tweet is not None:
                tweets.append(tweet)

        return tweets

    def _parse_tweet(self, tweetElement):
        '''
        Parses the attributes of a tweet from the tweetElement into a dict
        returns None if there is an error in the tweet
        '''
        li = tweetElement
        tweet = {
            'created_at' : None,
            'id_str' : li.get('data-item-id'),
            'text' : None,
            'lang' : None,
            'entities': {
                'hashtags': [],
                'symbols':[],
                'user_mentions':[],
                'urls':[],
            },
            'user' : {
                'id_str' : None, 
                'name' : None,
                'screen_name': None,
                'profile_image_url': None,
                'verified': False
                },
            'retweet_count' : 0,
            'favorite_count' : 0,
            'is_quote_status' : False,
            'in_reply_to_user_id': None,
            'in_reply_to_screen_name' : None,
            'contains_photo': False,
            'contains_video': False,
            'contains_card': False
        }   

        content_div = li.cssselect('div.tweet')
        if len(content_div) > 0:
            content_div = content_div[0]
            tweet['user']['id_str'] = content_div.get('data-user-id')
            tweet['user']['name'] = content_div.get('data-name')
            tweet['user']['screen_name'] = content_div.get('data-screen-name')
        
        reply_a = content_div.cssselect('div.tweet-context a.js-user-profile-link')
        if len(reply_a) > 0:
            tweet['in_reply_to_user_id'] = reply_a[0].get('data-user-id')
            tweet['in_reply_to_screen_name'] = reply_a[0].get('href') # remove /

        user_img = content_div.cssselect('img.avatar')
        if len(user_img) > 0:
            tweet['user']['profile_image_url'] = user_img[0].get('src')
        
        text_p = content_div.cssselect('p.tweet-text, p.js-tweet-text')
        if len(text_p) > 0:
            text_p = text_p[0]
            
            #hacky way to include Emojis
            for emoj in text_p.cssselect('img.Emoji'):
                emoj.tail = emoj.get('alt') + emoj.tail if emoj.tail else emoj.get('alt')
            
            for invis in text_p.cssselect('span.invisible'):
                invis.getparent().remove(invis)

            for elips in text_p.cssselect('span.tco-ellipsis'):
                elips.

            #remove non breaking space and ellipsis
            tweet['text'] = text_p.text_content().replace(u"\xa0", u"")
            tweet['lang'] = text_p.get('lang')
        else:
            # there is no tweet text, unknown if this occurs
            return None

        verified_span = content_div.cssselect('span.Icon--verified')
        if len(verified_span) > 0:
            tweet['user']['verified'] = True
        
        date_span = content_div.cssselect('span._timestamp')
        if len(date_span) > 0:
            timestamp = int(date_span[0].get('data-time-ms'))/1000
            tweet['created_at'] = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%a %b %d %H:%M:%S %z %Y') 

        #Retweet and Favoritte counts
        counts = li.cssselect('span.ProfileTweet-action--retweet, span.ProfileTweet-action--favorite')
        if len(counts) > 0:
            for c in counts:
                classes = c.get('class').split(' ')
                if 'ProfileTweet-action--retweet' in classes:
                    tweet['retweet_count'] = int(c[0].get('data-tweet-stat-count'))
                elif 'ProfileTweet-action--favorite' in classes:
                    tweet['favorite_count'] = int(c[0].get('data-tweet-stat-count'))

        entities = tweet['entities']
        self._parse_tweet_entites(text_p, entities)

        quoted_tweet_context = content_div.cssselect('div.QuoteTweet-innerContainer')
        if len(quoted_tweet_context) > 0:
            quoted_tweet_context = quoted_tweet_context[0]
            tweet['is_quote_status'] = True
            tweet['quoted_status_id_str'] = quoted_tweet_context.get('data-item-id')
            tweet['quoted_status'] = {
                    'id_str': None,
                    'text': None,
                    'user': {
                        'id_str' : None,
                        'name' : None,
                        'screen_name' : None,
                    },
                    'entities' : {
                        'hashtags' : [],
                        'symbols' :[],
                        'user_mentions':[],
                        'urls':[]
                    }
                }
            qtweet = tweet['quoted_status']

            qtweet['id_str'] = quoted_tweet_context.get('data-item-id')
            qtweet['user']['id_str'] = quoted_tweet_context.get('data-user-id')
            qtweet['user']['screen_name'] = quoted_tweet_context.get('data-screen-name')

            qt_user_name = quoted_tweet_context.cssselect('b.QuoteTweet-fullname')
            if len(qt_user_name) > 0:
                qtweet['user']['name'] = qt_user_name[0].text_content()
            
            qt_text = quoted_tweet_context.cssselect('div.QuoteTweet-text.tweet-text')
            if len(qt_text) > 0:
                qt_text = qt_text[0]
                qtweet['text'] = qt_text.text_content()

            qt_entites = qtweet['entities']
            self._parse_tweet_entites(qt_text, qt_entites)
        
        tweet_media_context = content_div.cssselect('div.AdaptiveMedia-container')
        if len(tweet_media_context) > 0:
            tweet_media_context = tweet_media_context[0]
            tweet['entities']['media'] = []
            photo_found = False
            tweet_media_photos = tweet_media_context.cssselect('div.AdaptiveMedia-photoContainer')
            for elm in tweet_media_photos:
                tweet['contains_photo'] = photo_found = True
                photo = {
                'media_url' : elm.get('data-image-url'),
                'type' : 'photo'
                }
                tweet['entities']['media'].append(photo)
            if not photo_found:
                tweet_media_video = tweet_media_context.cssselect('div.AdaptiveMedia-videoContainer')
                if len(tweet_media_video) > 0:
                    tweet['contains_video'] = True
                    video = {
                        'type' : 'video',
                        'video_type' : re.search(re.compile(r"PlayableMedia--([a-zA-Z]*)"), tweet_media_video[0].cssselect('div[class*="PlayableMedia--"]')[0].get('class')).group(1),
                        'media_url' : 'https://twitter.com/i/videos/tweet/' + tweet['id_str'],
                        'video_thumbnail' : re.search(re.compile(r"background-image:url\(\'(.*)\'"),tweet_media_video[0].cssselect('div.PlayableMedia-player')[0].get('style')).group(1)
                    }
                    tweet['entities']['media'].append(video)
            # print(tweet['entities']['media'])

        # else:
        #     tweet_media_context = content_div.cssselect('div.card2')
        #     if len(tweet_media_context) > 0:
        #         pass

        return tweet

    def _parse_tweet_entites(self, element, entities):
        tags = element.cssselect('a.twitter-hashtag, a.twitter-cashtag, a.twitter-atreply, a.twitter-timeline-link')
        if len(tags) > 0:
            for tag in tags:
                classes = tag.get('class').split(' ')
                if 'twitter-hashtag' in classes:
                    entities['hashtags'].append(tag.text_content().strip(' \n#')) #TODO remove # symbol
                elif 'twitter-cashtag' in classes:
                    entities['symbols'].append(tag.text_content().strip(' \n$')) #TODO remove $ symbol
                elif 'twitter-atreply' in classes:

                    mentioned_user = {
                        'id_str' : tag.get('data-mentioned-user-id'),
                        'screen_name' : tag.get('href').strip('/') if tag.get('href') is not None else None
                    }
                    
                    entities['user_mentions'].append(mentioned_user)
                elif 'twitter-timeline-link' in classes: #TODO and 'u-hidden' not in classes
                    url = {
                        'url': tag.get('href'),
                        'expanded_url' : tag.get('data-expanded-url'),
                        'display_url' : None
                    }
                    display_url = tag.cssselect('span.js-display-url')
                    if len(display_url) > 0:
                        url['display_url'] = str(display_url[0].text_content())
                    entities['urls'].append(url)

if __name__ == "__main__":

    import TwitterQuery
    TwitterClient.FIDDLER_DEBUG = True
    x = TwitterClient(timeout=None)
    TwitterQuery.SearchQuery('a')
    try:
        gen = x.get_search_iterator_2(TwitterQuery.SearchQuery('$AAPL'))
        for res in gen:
            print(len(res['tweets']))
    except requests.exceptions.Timeout as e:
        print('asdf')
        print(e)
        
def get_ids(tweets):
    return [tweet['id_str'] for tweet in tweets]