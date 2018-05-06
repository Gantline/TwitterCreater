import tweepy
import NewsGatherer #TODO move to main.py

auth = tweepy.OAuthHandler('L8mHYjnbVoOpKQ5KbTvps2hHt', 'HC8ETgLRsAFqedlaq5h1CyHuKm7EcukMYYX9eELo19buuoFaiF')
auth.set_access_token('801874596798439424-HCfH0BPJlaa2pHVGMvDEedM2Zp0L5Gk', 'rj7gkLcMW52p0BjArLOhea1lF9u8gVhKplfX4pgCV0fDB')
api = tweepy.API(auth)

def get_tweets_all():
    public_tweets = api.home_timeline()
    return public_tweets

def parse_tweets_all(public_tweets):
    tweets = []
    print(public_tweets.text)
    for tweet in public_tweets:
        tweets.append(tweet.text)
    return tweets

def process_twitter_title(tweet,i):
    title = tweet[i].rsplit(":",2)[0]
    return title

#produciton:
#public = get_tweets_all()
#all = parse_tweets_all(public)

all = [u'OPPO A83 (2018) Mid-Ranger Now Expanding Beyond India:\nhttps://t.co/cB2wiEv366', u'An Incredible, One-of-a-Kind Expanding Tiny House \u2014 House Tour Greatest Hits:\nhttps://t.co/O9U2aSAysQ']

#get tweets
title = process_twitter_title(all,1)
print "Tweet Title: "+title


#news stories
NewsResponse = NewsGatherer.get_news_stories()
story = NewsGatherer.parse_news_stories(NewsResponse, 0)
print "News title: "+story['title']
if (story['title'] != title):
    print "Posting Tweet..."
else:
    print "not posting..."
