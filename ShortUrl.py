import requests
import json
from Auth import urlshortenerKey

#TODO This api endpoint is gone on March 30, 2019

def goo_shorten_url(url): #Used to get shorter url to tweet
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key='+urlshortenerKey
    data = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(data), headers=headers)
    return r.json()['id']