import sys
import requests
from requests import Request, Session
from bs4 import BeautifulSoup
from time import sleep

__author__ = 'Darren Tuit'

class TwitterWebsiteSearch():

    def __init__(self, rate_delay, error_delay=5, timeout=5, retry_limit=4):
        self.rate_delay = rate_delay
        self.error_delay = error_delay
        self.timeout = timeout
        # TODO: impl timeout and retry
        self.retry_limit = retry_limit

        self.base_url = 'https://twitter.com/i/search/timeline'
    
    def search(self, query):
        s = Session()
        min_tweet = None
        request = self.prepare_request(self.base_url, query)
        result_json = self.execute_request(request)

        while result_json is not None and result_json['items_html'] is not None:
            tweets = self.parse_tweets(result_json['items_html']) 
            
            if(tweets) == 0:
                break
            
            if min_tweet is None:
                min_tweet = tweets[0]

            yield tweets

            max_tweet = tweets[-1]
            if min_tweet['id_str'] is not max_tweet['id_str']:
                max_position = "TWEET-{0}-{1}".format(max_tweet['id_str'], min_tweet['id_str'])
                request = self.prepare_request(self.base_url, query, max_position)
                sleep(self.rate_delay)
                result_json = self.execute_request(request)

    def execute_request(self, preparedRequest):
        try:
            s = Session()
            result = s.send(preparedRequest)
            result_json = result.json()
            return result_json
        except requests.exceptions.Timeout as e:
            print(e.message)
            print("Sleeping for {:d}".format(self.error_delay))
            sleep(self.error_delay)
            return self.execute_request(preparedRequest)

    @staticmethod
    def prepare_request(url, query, max_position=None):
        payload = { 'q' : query }
        if max_position is not None:
            payload['max_position'] = max_position
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/29.0.1547.65 Chrome/29.0.1547.65 Safari/537.36',
            'Accept-Encoding' : 'gzip, deflate, sdch, br'
        }
        req = Request('GET', url, params=payload, headers=headers)
        return req.prepare()
    
    @classmethod
    def parse_tweets(cls, items_html):
        tweets = []
        soup = BeautifulSoup(items_html, "lxml")

        for li in soup.findAll('li', attrs={'class':'js-stream-item'}):

            # Check if is a tweet otherwise skip
            if 'data-item-id' not in li.attrs:
                continue
            
            tweet = {
                'created_at' : None,
                'id_str' : li['data-item-id'],
                'text' : None,
                'in_reply_to_screen_name': None,
                'user' : {
                    'id_str' : None,
                    'name' : None,
                    'screen_name': None
                    },
                'retweet_count' : 0,
                'favorite_count' : 0,
                }

            text_p = li.find('p', class_="tweet-text")
            if text_p is not None:
                tweet['text'] = text_p.get_text()

            user_div = li.find('div' , class_="tweet")
            if user_div is not None:
                tweet['user']['id_str'] = cls._extract_attr_value(user_div, 'data-user-id')
                tweet['user']['name'] = cls._extract_attr_value(user_div, 'data-name')
                tweet['user']['screen_name'] = cls._extract_attr_value(user_div, 'data-screen-name')
            
            date_span = li.find('span', class_="_timestamp")
            if date_span is not None:
                tweet['created_at'] = int(cls._extract_attr_value(date_span, 'data-time-ms'))
                
            retweet_span = li.select("span.ProfileTweet-action--retweet > span.ProfileTweet-actionCount")
            if retweet_span is not None:
                tweet['retweet_count'] = int(cls._extract_attr_value(retweet_span[0], 'data-tweet-stat-count'))

            fav_span = li.select("span.ProfileTweet-action--favorite > span.ProfileTweet-actionCount")
            if fav_span is not None:
                tweet['favorite_count'] = int(cls._extract_attr_value(fav_span[0], 'data-tweet-stat-count'))
            
            # TODO: extract more values

            tweets.append(tweet)
        return tweets 
    
    def _extract_attr_value(tag, attr):
        if tag.has_attr(attr):
            return tag[attr]
        return None

if __name__ == '__main__':
    tw = TwitterWebsiteSearch(0)
    search_generator = tw.search('$AAPL')

    uniq_tw_ids = {}

    count = 0

    for tweets in search_generator:
        for tweet in tweets:
            count += 1
            print('{0}, {1}, {2}'.format(count, tweet['id_str'], tweet['text']))
        print(len(tweets))

        if count > 100:
            break,