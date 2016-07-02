import requests
from requests import Request, Session
from time import sleep
import time
import lxml.html as lh
from urllib.parse import quote

base_url = 'https://twitter.com/i/search/timeline'

def search(query, min_tweet_id=None, max_tweet_id=None, aditional_params=None, session=None):
    """
    
    """
    # Init query parameters
    params = {'q' : quote(query)}
    if aditional_params is not None:
        params = aditional_params
        params['q'] = quote(query)        

    # Create Request
    if min_tweet_id is not None and max_tweet_id is not None:
        params['max_position'] = encode_max_postion_param(min_tweet_id, max_tweet_id)
    request = prepare_request(params)

    # Execute Request
    result = execute_request(request, session)
    result_json = result.json()

    # Extract Results
    tweets = []
    if result_json is not None and result_json['items_html'] is not None:
        tweets = parse_tweets(result_json['items_html']) 

    # Return Result
    return {
        '_request': request,
        '_result': result,
        'tweets': tweets
        }

def prepare_request(params):
    payload_str = "&".join("%s=%s" % (k,v) for k,v in params.items())
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/29.0.1547.65 Chrome/29.0.1547.65 Safari/537.36',
        'Accept-Encoding' : 'gzip, deflate, sdch, br'
        }
    cookie = {}
    req = Request('GET', base_url, params=payload_str, headers=headers, cookies=cookie)
    return req.prepare()

def execute_request(prepared_request, session=None):
    try:
        if session is None:
            session = Session()
        result = session.send(prepared_request)
        return result
    except requests.exceptions.Timeout as e:
        raise

def parse_tweets(items_html):
    html = lh.fromstring(items_html)
    tweets = []
    for li in html.cssselect('li.js-stream-item'):
        
        if 'data-item-id' not in li.attrib:
            continue

        tweet = {
            'created_at' : None,
            'id_str' : li.get('data-item-id'),
            'text' : None,
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
            'favorite_count' : 0
        }
  
        content_div = li.cssselect('div.tweet')
        if len(content_div) > 0:
            content_div = content_div[0]
            tweet['user']['id_str'] = content_div.get('data-user-id')
            tweet['user']['name'] = content_div.get('data-name')
            tweet['user']['screen_name'] = content_div.get('data-screen-name')
        
        user_img = content_div.cssselect('img.avatar')
        if len(user_img) > 0:
            tweet['user']['profile_image_url'] = user_img[0].get('src')
        
        text_p = content_div.cssselect('p.tweet-text')
        if len(text_p) > 0:
            text_p = text_p[0]
            tweet['text'] = text_p.text_content()
        
        verified_span = content_div.cssselect('span.Icon--verified')
        if len(verified_span) > 0:
            tweet['user']['verified'] = True
        
        date_span = content_div.cssselect('span._timestamp')
        if len(date_span) > 0:
            tweet['created_at'] = int(date_span[0].get('data-time-ms'))
        
        counts = li.cssselect('span.ProfileTweet-action--retweet, span.ProfileTweet-action--favorite')
        if len(counts) > 0:
            for c in counts:
                classes = c.get('class').split(' ')
                if 'ProfileTweet-action--retweet' in classes:
                    tweet['retweet_count'] = c[0].get('data-tweet-stat-count')
                elif 'ProfileTweet-action--favorite' in classes:
                    tweet['favorite_count'] = c[0].get('data-tweet-stat-count')

        entities = tweet['entities']
        tags = text_p.cssselect('a.twitter-hashtag, a.twitter-cashtag, a.twitter-timeline-link')
        if len(tags) > 0:
            for tag in tags:
                classes = tag.get('class').split(' ')
                if 'twitter-hashtag'in classes:
                    entities['hashtags'].append(tag.text_content())
                elif 'twitter-cashtag' in classes:
                    entities['symbols'].append(tag.text_content())
                elif 'twitter-timeline-link' in classes and 'u-hidden' not in classes:
                    url = {
                        'url': tag.get('href'),
                        'expanded_url' : tag.get('data-expanded-url'),
                        'display_url' : None
                    }
                    display_url = tag.cssselect('span.js-display-url')
                    if len(display_url) > 0:
                        url['display_url'] = display_url[0].text_content()
                    entities['urls'].append(url)
        
        tweets.append(tweet)
    return tweets

def encode_max_postion_param(min, max):
    return "TWEET-{0}-{1}".format(min, max)

class TwitterPager():
    def __init__(self, 
                rate_delay=0,
                error_delay=5,
                timeout=5,
                retry_limit=4,
                continue_on_empty_result=True,
                session=Session()):
        self.rate_delay = rate_delay
        self.error_delay = error_delay
        self.timeout = timeout
        self.retry_limit = retry_limit
        self.continue_on_empty_result = continue_on_empty_result
        self.session = session

    def execute_request(prepared_request, session=None):
        try:
            return execute_request(prepared_request, session)
        except requests.exceptions.Timeout as e:
            print(e.message)
            print("Sleeping for {:d}".format(self.error_delay))
            sleep(self.error_delay)
            return self.execute_request(prepared_request)

    def get_iterator(self, query, min_tweet_id=None, max_tweet_id=None, aditional_params=None):
        result = search(query, min_tweet_id, max_tweet_id, aditional_params)
        prev_min_tweet_id = None
        yield result

        while True:

            if len(result['tweets']) == 0:
                if not self.continue_on_empty_result:
                    print('No tweets returned terminating program')
                    break
                else:
                    # Sometimes the API stops returning tweets even when there are more
                    # we can try to find these tweets by modifying the max_position parameter.
                    int_min_id = int(min_tweet_id)
                    for x in range(8, len(min_tweet_id)):
                        min_to_try = int_min_id - 10**x
                        tweets = search(query, str(min_to_try), max_tweet_id, aditional_params)['tweets']
                        if len(tweets) > 0:
                            break
                    else:
                        print('No tweets returned terminating program')
                        # if we didnt find any point to continue from break anyway.
                        break

            if max_tweet_id is None:
                max_tweet_id = result['tweets'][0]['id_str']   

            prev_min_tweet_id = min_tweet_id
            min_tweet_id = result['tweets'][-1]['id_str']

            # If the current request returns the same tweets as the last
            # the query is configured wrong
            if prev_min_tweet_id is min_tweet_id:
                break

            result = search(query, min_tweet_id, max_tweet_id, aditional_params, self.session)
            
            yield result

if __name__ == '__main__':
    count = 0
    for x in TwitterPager().get_iterator('a b c "e" f OR g OR h -i -j -k #l OR #m OR #n lang:en'):
        print("{} {} {}".format(count, len(x['tweets']), x['_request'].url))
        count += 1

        # if count == 20:
        #     break