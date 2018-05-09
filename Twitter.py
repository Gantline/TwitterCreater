import tweepy
from Auth import twitterAccessSecret,twitterAccessToken,twitterKey,twitterSecret

auth = tweepy.OAuthHandler(twitterKey, twitterSecret)
auth.set_access_token(twitterAccessToken, twitterAccessSecret)
api = tweepy.API(auth)

def get_tweets_all(): #todo limit number of tweets to something reseanble
    public_tweets = api.home_timeline()
    return public_tweets

def parse_tweets_all(public_tweets): #make array of existing tweets's text #todo dont get all existing tweets
    tweets = []
    print(public_tweets.text)
    for tweet in public_tweets:
        tweets.append(tweet.text)
    return tweets

def process_twitter_title(tweet,i): #give tweets array and number, return title
    title = tweet[i].rsplit(":",2)[0]
    return title

def tweet(storyId): #todo add try logic
    status = news_story_to_tweet(storyId)
    print "DEBUG (NOT LIVE) tweeting...: "+status
    #api.update_status(status) #todo Make this live
    return