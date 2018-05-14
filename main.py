import NewsGatherer
import Twitter
import ShortUrl
import logic
'''
I think I will get the top news stories, where the title != my latest tweet (s).
I will then post that news story with a shortened url
'''

#TODO :
#1. Add debugging flag (no calls to twitter)
#2. generate new auth toeksn and put in seperate file and make private


# -get news stories that fit query
newsResponse = NewsGatherer.get_news_stories()
story = NewsGatherer.parse_news_stories(newsResponse, 0)
if newsResponse is not None:
    #publicTweets = Twitter.get_tweets_all()
    #tweets = Twitter.parse_tweets_all(publicTweets)

    allTweets = [u'OPPO A83 (2018) Mid-Ranger Now Expanding Beyond India:\nhttps://t.co/cB2wiEv366',
                  u'An Incredible, One-of-a-Kind Expanding Tiny House \u2014 House Tour Greatest Hits:\nhttps://t.co/O9U2aSAysQ']
    tweetTitles = []
    i = 0
    for tweet in allTweets:
        tweetTitles.append(Twitter.process_twitter_title(allTweets, i))
        print tweetTitles[i]
        i = i + 1




#
# -get tweets
# -parse tweets and return an array of titles
#
#
# -for story in most recent 3:
# 	-if empty, break
# 	-parse story title, etc.
# 	-set already_posted = false
# 	-while ! already_posted && i < length of tweet array:
# 		-if story title != tweets[i]
# 			i++
# 		-else set already_posted = true
# 	-if ! already_posted:
# 		-call url shortener
# 		-tweet story title & url

#   allTweets = [u'OPPO A83 (2018) Mid-Ranger Now Expanding Beyond India:\nhttps://t.co/cB2wiEv366',
 #                 u'An Incredible, One-of-a-Kind Expanding Tiny House \u2014 House Tour Greatest Hits:\nhttps://t.co/O9U2aSAysQ']