import tweepy
from Auth import twitterAccessSecret,twitterAccessToken,twitterKey,twitterSecret
import Debugging
auth = tweepy.OAuthHandler(twitterKey, twitterSecret)
auth.set_access_token(twitterAccessToken, twitterAccessSecret)
api = tweepy.API(auth)

def get_tweets_all(): #todo limit number of tweets to something reseanble
    public_tweets = api.home_timeline()
    return public_tweets

def parse_tweets_all(public_tweets): #make array of existing tweets's text #todo dont get all existing tweets
    tweets = []
    for tweet in public_tweets:
        title = tweet.text.rsplit(":", 2)[0] #TODO test this
        tweets.append(title)
    return tweets

def process_twitter_title(tweet,i): #give tweets array and number, return title #TODO remove function if not using hardcoded alltweets
    title = tweet[i].rsplit(":",2)[0]
    return title

def news_story_to_tweet(storyTitle, storyUrl): #format final tweet to be sent to twitter
    return storyTitle+":"+"\n"+storyUrl

def tweet(storyTitle, storyUrl): #todo add try logic
    status = news_story_to_tweet(storyTitle, storyUrl)
    if Debugging.debugging_flag() == True:
        print "DEBUG (NOT LIVE) tweeting...: "
        print(status)
    else:
        print('>>Attempting to tweet: '+ str(status))
        api.update_status(status)
    return api.get_status