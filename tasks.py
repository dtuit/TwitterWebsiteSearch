from TwitterWebsiteSearch import TwitterWebsiteSearch
from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def search(query, min=None, max=None):
    result = TwitterWebsiteSearch.search(query, min, max)
    return len(result['tweets'])