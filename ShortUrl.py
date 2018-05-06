def goo_shorten_url(url): #Used to get shorter url to tweet
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyB7DHtzdPLF9Pl90XFzkw_YD_sr8PI58gA'
    data = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(data), headers=headers)
    return r.json()['id']