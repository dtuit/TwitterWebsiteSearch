class Api():

    def __init__(self, session):
        self.session = session

    def search(self, query, min_position=None, max_position=None, search_type=None, reset_error_state=False):
        pass
    
    def get_status(self, id):
        pass

    def get_user(self, screen_name):
        pass
    
    def user_timeline(self, screen_name, max_position=None, min_position=None, reset_error_state=False):
        pass

    def get_search_iterator(self, query, min_position=None, max_position=None, search_type=None, reset_error_state=False):
        pass
    
    def get_user_timeline_iterator(self, screen_name, max_position=None, min_position=None, reset_error_state=False):
        pass
    
