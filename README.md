#TwitterWebsiteSearch 

TwitterWebsiteSearch is a small python script for searching and saving data from [Twitter.com search](https://twitter.com/search-home) without using the [official API](https://dev.twitter.com/rest/public/search). 

##Data Format
Tweets extracted, are formatted similarly to the official API, detailed [here](https://dev.twitter.com/overview/api/tweets)

each tweet is a python dict with the following structure.
```
{
	'created_at' : UTC-datetime format '%Y-%m-%d %H:%M:%S' ,
	'id_str' : "",
	'text' : "",
	'entities': {
		'hashtags': [],
		'symbols':[],
		'user_mentions':[],
		'urls':[],
		'media'[] optional
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
	'is_quote_status' : False,
	'in_reply_to_user_id': None,
	'in_reply_to_screen_name' : None,
	'contains_photo': False,
	'contains_video': False
}
```
##Usage
create your query using [twitter advanced search](https://twitter.com/search-advanced)  
note: pass the query without url encoding.
```python

	import TwitterWebsiteSearch

	TitterPageIterator = TwitterWebsiteSearch.TwitterPager().get_iterator('#python')

	count = 0
	for page in TitterPageIterator:
		for tweet in page['tweets']:
			print("{0} id: {1} text: {2}".format(count, tweet['id_str'], tweet['text']))
			count += 1
```

###Dependencies 

* [requests](http://docs.python-requests.org)
* [lxml](http://lxml.de/index.html)
* [cssselect](https://pythonhosted.org/cssselect/)

note. using lmxl directly instead of BeautifulSoup as BS was too slow.
