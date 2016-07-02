import requests
from requests import Request, Session
from bs4 import BeautifulSoup, SoupStrainer
from time import sleep
import time
from contextlib import contextmanager
import re

s = Session()
base_url = 'https://twitter.com/i/search/timeline'

from statistics import mean
timings = []

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print("{} function took {:0.3f} ms".format(f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap

@contextmanager
def timeit_context(name):
    startTime = time.time()
    yield
    elapsedTime = time.time() - startTime
    timings.append(elapsedTime)
    print('[{}] finished in {} ms'.format(name, int(elapsedTime * 1000)))

def search(query, min_tweet_id=None, max_tweet_id=None, session=None):

    # Create Request
    max_position = None
    if min_tweet_id is not None and max_tweet_id is not None:
        max_position = encode_max_postion_param(min_tweet_id, max_tweet_id)
    request = prepare_request(query, max_position)

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

def prepare_request(query, max_position=None):
    payload = { 'q' : query }
    if max_position is not None:
        payload['max_position'] = max_position
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/29.0.1547.65 Chrome/29.0.1547.65 Safari/537.36',
        'Accept-Encoding' : 'gzip, deflate, sdch, br'
    }
    cookie = {}
    req = Request('GET', base_url, params=payload, headers=headers, cookies=cookie)
    return req.prepare()

# @timing
def execute_request(prepared_request, session):
    try:
        if session is None:
            session = Session()
        
        result = session.send(prepared_request)
        return result
    except requests.exceptions.Timeout as e:
        raise

def parse_tweets_lxml(items_html):
    pass

@timing
def parse_tweets(items_html):
    tweets = []
    # 389ms
    with timeit_context('My profiling code'):
        soup = BeautifulSoup(items_html, "lxml")
    #165ms
    #42ms
    
    lis = soup.select('li.js-stream-item')
    # 220ms
    for li in lis:

        # Check if is a tweet otherwise skip
        if 'data-item-id' not in li.attrs:
            continue

        tweet = {
            'created_at' : None,
            'id_str' : li['data-item-id'],
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
        
        # tweet text 
        text_p = li.find('p', class_="tweet-text")
        if text_p is not None:
            tweet['text'] = text_p.get_text()
                
        # user details
        # 0ms
        user_div = li.find('div' , class_="tweet")
        if user_div is not None:
            tweet['user']['id_str'] = extract_attr_value(user_div, 'data-user-id')
            tweet['user']['name'] = extract_attr_value(user_div, 'data-name')
            tweet['user']['screen_name'] = extract_attr_value(user_div, 'data-screen-name')
        
        # 1ms
        user_img = user_div.find('img', class_="avatar")
        if user_img is not None:
            tweet['user']['profile_image_url'] = extract_attr_value(user_img, 'src')
        
        section_div = user_div.find('div', class_='stream-item-header')

        # 20ms
        # 7ms
        # 2ms
        # 1ms
        # user_verifed_span = user_div.select('div.content > div.stream-item-header > a > strong > span.Icon--verified')
        # with timeit_context('My profiling code'):
        user_verifed = section_div.find(string=re.compile('Verified'))
            # user_verifed_span = user_div.find('div', class_='stream-item-header').find('a', 'account-group').find('span', class_="Icon--verified")
        if user_verifed is not None:
            tweet['user']['verified'] = True
            # print(tweet['user']['verified'])
            # user_verifed_span = user_div.find('span', class_="Icon--verified")
            # if user_verifed_span is not None:
            #     tweet['user']['verified'] = True
            #     print(tweet['user']['verified'])

        # tweet date
        # 3-4ms
        # 2ms
        # with timeit_context('My profiling code'):
        date_span = section_div.find('span', class_="_timestamp")
        if date_span is not None:
            tweet['created_at'] = int(extract_attr_value(date_span, 'data-time-ms'))
        

        footer_section = li.find('div', class_='stream-item-footer')
        # retweet count
        # 6ms
        # 4ms
        # 0ms
        
            # retweet_span = footer_section.find('span', class_='ProfileTweet-action--retweet').find('span', class_='ProfileTweet-actionCount')
        retweet_span = footer_section.select_one("span.ProfileTweet-action--retweet > span.ProfileTweet-actionCount")
        if retweet_span is not None:
            tweet['retweet_count'] = int(extract_attr_value(retweet_span, 'data-tweet-stat-count'))

        # favourite count
        # 6ms
        # 1ms
        
        fav_span = footer_section.select("span.ProfileTweet-action--favorite > span.ProfileTweet-actionCount", limit=1)
        if len(fav_span) > 0:
            tweet['favorite_count'] = int(extract_attr_value(fav_span[0], 'data-tweet-stat-count'))
        
        entities = tweet['entities']
        # extract hashtags
        # 3-10ms
        # 3.8ms
        # with timeit_context('My profiling code'):
            # hashtags_a = text_p.find_all('a', class_=["twitter-hashtag","twitter-cashtag"])
        tags = text_p.select('a.twitter-hashtag, a.twitter-cashtag')
            # hashtags_a = text_p.find_all('a', class_="twitter-hashtag")
        if len(tags) > 0:
            for tag in tags:
                if 'twitter-cashtag' in tag.attrs['class']:
                    entities['hashtags'].append(tag.text)
                if 'twitter-hashtag' in tag.attrs['class']:
                    entities['symbols'].append(tag.text)
            # print(entities['hashtags'])
            # print(entities['symbols'])

        # extract symbols
        # 1-5 -10 ms
        # symbols_a = text_p.find_all('a', class_="twitter-cashtag")
        # if len(symbols_a) > 0:
        #     entities['symbols'] = [s.text for s in symbols_a]
        # # extract user_mentions

        # extract urls
        # 4ms
        urls_a = text_p.find_all('a', class_="twitter-timeline-link")
        if len(urls_a) > 0:
            for url in urls_a:
                # excludes hidden urls
                if('u-hidden' in url.attrs['class']):
                    continue
                this_url = {
                    'url' : extract_attr_value(url, 'href'),
                    'expanded_url' : extract_attr_value(url, 'data-expanded-url'),
                    'display_url' : None
                }
                display_url = url.find('span', class_="js-display-url")
                if display_url is not None:
                    this_url['display_url'] = display_url.text
                entities['urls'].append(this_url)

        tweets.append(tweet)
    return tweets 

def encode_max_postion_param(min, max):
    return "TWEET-{0}-{1}".format(min, max)

def extract_attr_value(tag, attr):
    if tag.has_attr(attr):
        return tag[attr]
    return None

class TwitterPager():
    def __init__(self, 
                rate_delay=0,
                error_delay=5,
                timeout=5,
                retry_limit=4,
                continue_on_empty_result=True):
        self.rate_delay = rate_delay
        self.error_delay = error_delay
        self.timeout = timeout
        self.retry_limit = retry_limit
        self.continue_on_empty_result = continue_on_empty_result

    def execute_request(prepared_request, session):
        try:
            return execute_request(prepared_request, session)
        except requests.exceptions.Timeout as e:
            print(e.message)
            print("Sleeping for {:d}".format(self.error_delay))
            sleep(self.error_delay)
            return self.execute_request(prepared_request)

    def get_iterator(self, query, min_tweet_id=None, max_tweet_id=None):
        session = Session()
        result = search(query, min_tweet_id, max_tweet_id)
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
                        max_position = encode_max_postion_param(str(min_to_try), max_tweet_id)
                        request = prepare_request(base_url, query, max_position)
                        result_json = self.execute_request(request, session)
                        tweets = parse_tweets(result_json['items_html'])
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

            result = search(query, min_tweet_id, max_tweet_id, session)
            
            yield result

if __name__ == '__main__':
    count = 0
    for x in TwitterPager().get_iterator('$AAPL'):
        print("{} {} {}".format(count, len(x['tweets']), x['_request'].url))
        count += 1

        if count == 20:
            print(mean(timings))
            break