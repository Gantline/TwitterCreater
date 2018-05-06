import NewsGatherer
import Twitter
import ShortUrl

def check_tweet_not_exist(tweetTitle, newsTitle):
    print "checking to tweet?"
    print "Tweet Title: " + tweet_title
    print "News title: " + newsTitle
    if tweet_title != newsTitle:
        print "Posting Tweet..."
    else:
        print "not posting..."

# in progerss...
# def iterater_tmp(all_tweets_obj, news_title): #TODO this needs to go through twitter tiles to check if the news titles has already been tweeted.  return true or false
#         for tweet_title in all_tweets_obj:
#         exist = check_tweet_not_exist(tweet_title, newsTitle)
#         return exist

def news_story_to_tweet(storyId):
    return story["title"]+":"+"\n"+story['longUrl'] #TODO this should be short url?

#produciton:
#public = get_tweets_all()
#all_tweets = parse_tweets_all(public)
all_tweets = [u'OPPO A83 (2018) Mid-Ranger Now Expanding Beyond India:\nhttps://t.co/cB2wiEv366', u'An Incredible, One-of-a-Kind Expanding Tiny House \u2014 House Tour Greatest Hits:\nhttps://t.co/O9U2aSAysQ']

#get single tweet
tweet_title = Twitter.process_twitter_title(all_tweets,1)

#get single news story
NewsResponse = NewsGatherer.get_news_stories()
story = NewsGatherer.parse_news_stories(NewsResponse, 0)
newsTitle = NewsGatherer.parse_news_title(story)

check_tweet_not_exist(tweet_title, newsTitle)
print "----"
print "Text to tweet:\n"+news_story_to_tweet(0)