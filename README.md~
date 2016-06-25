#TwitterWebsiteSearch 

TwitterWebsiteSearch is a small python library for searching and saving data from [Twitter.com search](https://twitter.com/search-home) without using the [official API](https://dev.twitter.com/rest/public/search). 

##Usage
create your query using [twitter advanced search](https://twitter.com/search-advanced)
```python

	tw = TwitterWebsiteSearch(0)
	search_generator = tw.search_generator('#python')
	
	for result in search_generator:
	    count = 0
	    for tweet in result['tweets']:
	        count += 1
	        print("{0} id: {1} text: {2}".format(count, tweet['id_str'], tweet['text']))
		
```
###Dependencies 

* [requests](http://docs.python-requests.org)
* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)