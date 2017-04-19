# TwitterWebsiteSearch 

TwitterWebsiteSearch is a python script for searching and saving data from [Twitter.com search](https://twitter.com/search-home) without using the [official Twitter API](https://dev.twitter.com/rest/public/search). 
This allows bypassing some of the limitations of the official twitter API

* Get tweets older than 7 days. 

## Data Format
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
	'lang' : None
	'is_quote_status' : False,
	'quoted_status_id_str' : "" optional
	'quoted_status' : {} optional
	'in_reply_to_user_id': None,
	'in_reply_to_screen_name' : None,
	'contains_photo': False,
	'contains_video': False
}
```
## Usage
note: pass the query without url encoding.
```python

from TwitterWebsiteSearch import TwitterClient, SearchQuery

client = TwitterClient()
query = SearchQuery('#python')

count = 0
for page in client.get_search_iterator(query):
    for tweet in page['tweets']:
        print("{0} id: {1} text: {2}".format(count, tweet['id_str'], tweet['text']))
        count += 1
```


### Twitter Search Operator Guides

Useful resources for creating search queries.
http://www.followthehashtag.com/help/hidden-twitter-search-operators-extra-power-followthehashtag/
https://twitter.com/search-advanced
https://dev.twitter.com/rest/public/search

#### Useful search operators

* -filter:nativeretweets 
* -filter:replies 
* -filter:links

### Dependencies 

* [requests](http://docs.python-requests.org)
* [lxml](http://lxml.de/index.html)
* [cssselect](https://pythonhosted.org/cssselect/)
