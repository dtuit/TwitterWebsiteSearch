#TwitterWebsiteSearch 

TwitterWebsiteSearch is a small python library for searching and saving data from [Twitter.com search](https://twitter.com/search-home) without using the [official API](https://dev.twitter.com/rest/public/search). 

##Data Format
Tweets extracted, are formatted similarly to the official API, detailed [here](https://dev.twitter.com/overview/api/tweets)

each tweet is a python dict with the following structure.
```
{
	'created_at' : UTC-datetime,
	'id_str' : "",
	'text' : "",
	'entities': {
		'hashtags': [],
		'symbols':[],
		'user_mentions':[],
		'urls':[],
		},
	'user' : {
		'id_str' : "",
		'name' : "",
		'screen_name': "",
		'profile_image_url': "",
		'verified': bool
		},
	'retweet_count' : 0,
	'favorite_count' : 0,
	''
}
```
##Usage
create your query using [twitter advanced search](https://twitter.com/search-advanced)
```python

	tw = TwitterWebsiteSearch(0)
	search_generator = tw.search_generator('YOUR_QUERY')
	
	for result in search_generator:
	    count = 0
	    for tweet in result['tweets']:
	        count += 1
	        print("{0} id: {1} text: {2}".format(count, tweet['id_str'], tweet['text']))
		
```

###Dependencies 

* [requests](http://docs.python-requests.org)
* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)
