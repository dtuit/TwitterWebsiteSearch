from TwitterWebsiteSearch import TwitterClient, SearchQuery

client = TwitterClient()
query = SearchQuery('#python')

count = 0
for page in client.get_search_iterator(query):
    for tweet in page['tweets']:
        print("{0} id: {1} text: {2}".format(count, tweet['id_str'], tweet['text']))
        count += 1