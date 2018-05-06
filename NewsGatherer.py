import requests
import json

def get_news_stories(): #TODO change url query to "tall%20ships"
    url = 'https://newsapi.org/v2/everything'
    data = {
        'q' : 'tall+ships',
        'from' : '2018-05-04', #TODO make today - 2
        'sortBy' : 'publishedAt',
        'apiKey' : 'e14cf16aa4a4403d88aac364c17810fa',
        'to' : '2018-05-05' #TODO remove this
    }
    r = requests.get(url, data)
    return r.json()

def parse_news_stories(response, story):
    news = response
    for articles in news:
        data = { 'title': news['articles'][story]['title'], 'longUrl': news['articles'][story]['url'], 'description': news['articles'][story]['description']}
        return data

def parse_news_title(story):
    newsTitle = story['title']
    return newsTitle

#  Testing
# response = get_news_stories()
# story = parse_news_stories(response, 1)
# print story
# print parse_news_title(story)
