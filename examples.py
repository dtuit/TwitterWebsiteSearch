import TwitterWebsiteSearch

TitterPageIterator = TwitterWebsiteSearch.TwitterPager().get_iterator('#python')

count = 0
for page in TitterPageIterator:
    for tweet in page['tweets']:
        print("{0} id: {1} text: {2}".format(count, tweet['id_str'], tweet['text']))
        count += 1