import requests
from Auth import newsgathererKey
import datetime


#get_news_stories should be used once and saved to an object to reduce the number of calls to the api
def get_news_stories(): #TODO change url query to "tall%20ships"
    url = 'https://newsapi.org/v2/everything'
    data = {
        'q' : 'tall%20ships',
        'from' :  str(datetime.date.today() - datetime.timedelta(days=1)), #TODO make today - 2
        'sortBy' : 'publishedAt',
        'apiKey' : newsgathererKey,
        'to': str(datetime.date.today() - datetime.timedelta(days=1)),  # TODO make today - 2
    }
    r = requests.get(url, data)
    return r.json()

def parse_news_stories(response, story): #Takes json responce from get_news_stories() and a int of which story you would like
    news = response
    if news['totalResults'] == 0: #TODO test this
        return None
    data = { 'title': news['articles'][story]['title'], 'longUrl': news['articles'][story]['url'], 'description': news['articles'][story]['description']}
    return data

def parse_news_title(story):
    newsTitle = story['title']
    return newsTitle

def parse_news_url(story):
    newsUrl = story['longUrl']
    return newsUrl