import TwitterClient
import lxml
import lxml.html as lh
import json
from datetime import datetime

import unittest

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite

class TweetTestDataPrepareFromFile():

    def __init__(self, tweetIds):
        self.twitterClient = TwitterClient.TwitterClient()
        self.test_tweet_ids = tweetIds
        self.test_data = self._get_test_files(self.test_tweet_ids)
    
    def get_test_data(self):
        return self.test_data

    def _get_test_files(self, test_ids):
        test_files = []
        for id in test_ids:
            tf = {}
            tf['parsed'] = self._parse_tweet_from_html('./samplehtml/{}.html'.format(id))
            tf['api'] = self._open_json_tweet_from_file('./samplehtml/{}.json'.format(id))
            test_files.append(tf)
        return test_files
    def _parse_tweet_from_html(self, file_name):
        with open(file_name, 'r') as file:
            tweet_tree = lh.fromstring(file.read())
            result = self.twitterClient._parse_tweet(tweet_tree)
            return result
    def _open_json_tweet_from_file(self, file_name):
        with open(file_name, 'r') as file:
            result = json.load(file)
            return result    

class TestTweetParsing2(ParametrizedTestCase):

    @classmethod
    def setUpClass(cls):
        cls.datetime_format = '%a %b %d %H:%M:%S %z %Y'

    def test_parsed_id_matches_api_id(self):
        p_id = self.param['parsed']['id_str']
        a_id = self.param['api']['id_str']

        self.assertEqual(p_id, a_id)

    def test_parsed_text_matches_api_text(self):
        p_text = self.param['parsed']['text']
        a_text = self.param['api']['text']

        self.assertEqual(p_text, a_text)
    
    def test_parsed_date_is_formated_correctly(self):
        p_date = self.param['parsed']['created_at']

        try:
            datetime.strptime(p_date, self.datetime_format)
        except ValueError:
            self.fail('parsed tweet created_at "{}" is formated incorrectly'.format(self.datetime_format))


    def test_parsed_date_matches_api_date(self):
        
        p_date = self.param['parsed']['created_at']
        a_date = self.param['api']['created_at']
        'Sun Aug 28 02:19:13 +0000 2016'
        self.assertEqual(datetime.strptime(p_date, self.datetime_format),
         datetime.strptime(a_date, '%a %b %d %H:%M:%S %z %Y'))
    
    def test_parsed_counts_match_api_counts(self):
        pass 

def run_tests():
    suite = unittest.TestSuite()

    on_file_test_data_tweet_ids = [
            '769043391917199360',
            '769706112614629376',
            '769720966364667904']

    test_data = TweetTestDataPrepareFromFile(on_file_test_data_tweet_ids).get_test_data()
    
    for data in test_data:
        suite.addTest(ParametrizedTestCase.parametrize(TestTweetParsing2, param=data))

    unittest.TextTestRunner(verbosity=1).run(suite)


if __name__ == '__main__':
    run_tests()