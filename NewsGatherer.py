import requests
from Auth import newsgathererKey

#get_news_stories should be used once and saved to an object to reduce the number of calls to the api
def get_news_stories(): #TODO change url query to "tall%20ships"
    url = 'https://newsapi.org/v2/everything'
    data = {
        'q' : 'tall+ships',
        'from' : '2018-05-04', #TODO make today - 2
        'sortBy' : 'publishedAt',
        'apiKey' : newsgathererKey,
        'to' : '2018-05-05' #TODO remove this or make today
    }
    r = requests.get(url, data)
    return r.json()

#currently parse_news_stories is given the saved responce form get_news_stories and an id.
# It returns a single story.  I may want it to return the array of stories?
def parse_news_stories(response, story): #Takes json responce from get_news_stories() and a int of which story you would like
    news = response
    if news['totalResults'] == 0: #TODO test this
        return None
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
#