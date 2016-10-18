from .context import TwitterWebsiteSearch
from TwitterWebsiteSearch import TwitterClient
from TwitterWebsiteSearch import SearchQuery
import lxml
import lxml.html as lh
import json
from datetime import datetime
from operator import itemgetter
import os
import unittest
import itertools

def to_csv(query, page_limit):
    
    TwitterClient.FIDDLER_DEBUG = True
    tc = TwitterClient()
    sq = SearchQuery(query)
    tc.get_search_iterator(sq)

    csv = []

    count = 0
    for res in tc.get_search_iterator(sq):
        count += 1
        if count == page_limit:
            break
        res_tweets = res['tweets']

        

        csv_tweet = ['{0},{1},{2}'.format(tweet['id_str'],tweet['created_at'],tweet['user']['screen_name']) for tweet in res_tweets]
        csv = csv + csv_tweet

    dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    with open(os.path.join(os.path.dirname(__file__),'output/output_{0}.csv'.format(dt_str)), 'w+') as file:
        for line in csv:
            file.write(line+'\n')


        