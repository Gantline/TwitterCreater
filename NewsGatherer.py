import requests
import json

'''
This is to get new articles.
To Do:
1. Tweet message
2. Check to see if I have already tweeted this article
3. Perhaps tweet out an image, if Image Url is not null?'''

def goo_shorten_url(url): #Used to get shorter url to tweet
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyB7DHtzdPLF9Pl90XFzkw_YD_sr8PI58gA'
    data = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(data), headers=headers)
    return r.json()['id']

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

'''
response = get_news_stories()
story = parse_news_stories(response, 1)
'''