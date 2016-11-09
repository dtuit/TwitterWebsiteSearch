from urllib.parse import quote, urlsplit
from datetime import datetime
   
class SearchType():
    
    """
    Enum for working SearchType parameters.
    """

    Top = ''
    All = 'tweets'
    Videos = 'Videos'
    News = 'news'

class BaseQuery():
    def __init__(self):
       pass
    
    def build(self):
        raise NotImplementedError

class UserTimelineQuery(BaseQuery):
    def __init__(self, screen_name, min_position=None, max_position=None, reset_error_state=False, next_page_query=True, **kwargs):
        
        self.base_url = 'https://twitter.com/i/search/timeline'
        self.user = user
        self.max_position = max_position
        self.min_position = min_position
        self.reset_error_state = reset_error_state
        self.is_next_page_query = next_page_query

    def build(self):
        raise NotImplementedError


class SearchQuery(BaseQuery):

    """
    Bundle of parameters to Construct the url query string for a search query 
    
    :param query: the query string
    :param max_position: used as a cursor to which next page is desired.
    :param min_position: 
    :param since:
    :param until:
    :param search_type: 
    :param reset_error_state: When True query will always return the first page of results, result will include both the min_position and max_position parameters.
    :param next_page_query: Determines if to send the max_postion(next page) parameter or min_position(new tweets)
    :param **kwargs:
    """

    def __init__(self,
            query,
            max_position=None,
            min_position=None,
            since=None,
            until=None,
            search_type=SearchType.Top,
            reset_error_state=False,
            next_page_query=True,
            **kwargs #TODO 
            ):

        self.base_url = 'https://twitter.com/i/search/timeline'
        self.query = query
        self.max_position = max_position
        self.min_position = min_position
        self.since = since
        self.until = until
        self.search_type = search_type
        self.reset_error_state = reset_error_state
        self.is_next_page_query = next_page_query

    def build(self):
        params = {}

        q = self.query
        if self.since is not None:
            q += ' since:' + self.since.strftime('%Y-%m-%d')
        if self.until is not None:
            q += ' until:' + self.until.strftime('%Y-%m-%d')
        params['q'] = quote(q)

        if self.is_next_page_query:
            params['max_position'] = '' if not self.max_position else self.max_position
        else:
            params['min_position'] = '' if not self.min_position else self.min_position
        
        if self.search_type is not SearchType.Top:
            params['f'] = self.searchType
        
        params['reset_error_state'] = self.reset_error_state

        query_str = "&".join("%s=%s" % (k,v) for k,v in params.items())

        return query_str

    def set_max_postion(self, min_tweetId, max_tweetId, extra=None):
        mp = "TWEET-{0}-{1}".format(min_tweetId, max_tweetId)
        if extra is not None:
            mp += '-{0}'.format(extra)
        self.max_position = mp
    
    def set_min_position(self, min_tweetId, max_tweetId, extra=None):
        mp = "TWEET-{0}-{1}".format(max_tweetId, min_tweetId)
        if extra is not None:
            mp += '-{0}'.format(extra)
        self.min_position = mp

    def autoset_reset_error_state(self):
        """
        Set self.reset_error_state based on the combination of max_position, min_position and is_next_page_query

        """
        if self.is_next_page_query is True and self.max_position is None or self.is_next_page_query is False and self.min_position is None or self.min_position is None and self.max_position is None:
            self.reset_error_state = True
        else:
            self.reset_error_state = False