import requests
from Auth import newsgathererKey
import datetime


#get_news_stories should be used once and saved to an object to reduce the number of calls to the api
def get_news_stories(): #TODO change url query to "tall%20ships"
    url = 'https://newsapi.org/v2/everything'
    data = {
        'q' : 'tall%20ships%20regatta',
        'from' :  str(datetime.date.today() - datetime.timedelta(days=1)),
        'sortBy' : 'publishedAt',
        'apiKey' : newsgathererKey,
        'to': str(datetime.date.today() - datetime.timedelta(days=1)),
    }
    print(url+'?q='+data['q']+'&from='+data['from']+'&to='+data['to']+'&apiKey='+data['apiKey'])
    #r = requests.get(url, data) ##< returning {u'status': u'ok', u'articles': [], u'totalResults': 0}
    r = requests.get(url+'?q='+data['q']+'&from='+data['from']+'&to='+data['to']+'&apiKey='+data['apiKey']) #TODO make this more like get(url, data)  ALSO, i've removed sortBy to default to sortBy=best
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