import tweepy

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

def tweet(storyId):
    status = news_story_to_tweet(storyId)
    print "tweeting...: "+status
    #api.update_status(status) #todo Make this live
    return