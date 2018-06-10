import NewsGatherer
import Twitter
import ShortUrl
'''todo:
1. take single news title.  Iterate through twitter array to see if it matches.

'''

#cal check_tweet_not_exist for each iteration (for each tweet title / news title)
def check_tweet_not_exist(tweetTitle, newsTitle):
    print "check_tweet_not_exist: do titles match?"
    print "Tweet Title: " + tweet_title
    print "News title: " + newsTitle
    if tweet_title != newsTitle:
        print "Tweet does not exist"
        return true
    else:
        print "tweet already exists"
        return false

