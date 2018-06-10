import requests
from Auth import firebaseKey

#TODO This api endpoint is gone on March 30, 2019
#TODO use another url shortener

'''
def goo_shorten_url(url): #Used to get shorter url to tweet
    url = 'https://www.googleapis.com/urlshortener/v1/url?key='+urlshortenerKey
    data = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()['id']

print(goo_shorten_url('www.google.com'))
'''

def shorten_url(longUrl): #TODO change url query to "tall%20ships"
    url = 'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key='+firebaseKey
    data = {
        'longLink' : longUrl,
    }
    r = requests.post(url, data)
    return r.json()

