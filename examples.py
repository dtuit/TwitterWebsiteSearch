from TwitterWebsiteSearch import TwitterWebsiteSearch

tw = TwitterWebsiteSearch(0)
search_generator = tw.search_generator('#python')

count = 0

for result in search_generator:
    for tweet in result['tweets']:
        count += 1
        print("{0} id: {1} text: {2}".format(count, tweet['id_str'], tweet['text']))