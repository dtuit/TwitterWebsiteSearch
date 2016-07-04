import TwitterWebsiteSearch
from bs4 import BeautifulSoup, SoupStrainer 
from contextlib import contextmanager
import time
from statistics import mean
from lxml import  etree
from io import StringIO, BytesIO
from lxml.cssselect import CSSSelector
import lxml.html as lh
import json

timings = []
@contextmanager
def timeit_context(name):
    startTime = time.time()
    yield
    elapsedTime = time.time() - startTime
    timings.append(elapsedTime)
    print('[{}] finished in {} ms'.format(name, int(elapsedTime * 1000)))

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print("{} function took {:0.3f} ms".format(f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap

with open('samplehtml/twf', 'r') as f:
  data = f.read()
  tweets = TwitterWebsiteSearch.parse_tweets(data)
  with open('output2.txt', 'w') as f2:
    reses = []
    for t in tweets:
      res = {
        'id': t['id_str'],
        'tweet': t['text']
      }
      reses.append(res)
    f2.write(json.dumps(reses, indent=4))