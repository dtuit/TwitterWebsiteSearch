from urllib.parse import quote, urlsplit
from datetime import datetime

class QueryBuilder():
    
    def __init__(self):
        pass
    
class SearchType():
    Top = ''
    All = 'tweets'
    Videos = 'Videos'
    News = 'news'

class SearchQueryBuilder():

    def __init__(self, query, min_tweetId=None, max_tweetId=None, since=None, until=None, searchtype=SearchType.Top, latent_count=None):
        self.base_url = 'https://twitter.com/i/search/timeline'
        self.query = query
        self.min_tweetId = min_tweetId
        self.max_tweetId = max_tweetId
        self.since = since
        self.until = until
        self.searchType = searchtype
        self.latent_count = latent_count

    def build(self):
        params = {}

        q = self.query
        if self.since is not None:
            q += ' since:' + self.since.strftime('%Y-%m-%d')
        if self.until is not None:
            q += ' until:' + self.until.strftime('%Y-%m-%d')
        params['q'] = quote(q)

        if self.min_tweetId is not None and self.max_tweetId is not None:
            params['max_position'] = self.encode_max_postion_param(self.min_tweetId, self.max_tweetId)

        if self.searchType is not SearchType.Top:
            params['f'] = self.searchType

        query_str = "&".join("%s=%s" % (k,v) for k,v in params.items())
        params['q'] = quote(q)

        return query_str

    @staticmethod
    def encode_max_postion_param(min_tweetId, max_tweetId):
        return "TWEET-{0}-{1}".format(min_tweetId, max_tweetId)

if __name__ is '__main__':

    sq = SearchQueryBuilder('asdf', 'sadfsadf', 'kljhl', datetime.now(), datetime.now(), SearchType.All)
    print(sq.build())