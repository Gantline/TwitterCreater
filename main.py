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

if newsResponse is not None:
    #publicTweets = Twitter.get_tweets_all()
    #tweets = Twitter.parse_tweets_all(publicTweets)

    #beginning of twitter bypass
    allTweets = [u'OPPO A83 (2018) Mid-Ranger Now Expanding Beyond India:\nhttps://t.co/cB2wiEv366',
                  u'An Incredible, One-of-a-Kind Expanding Tiny House \u2014 House Tour Greatest Hits:\nhttps://t.co/O9U2aSAysQ']
    tweetTitles = []
    i = 0
    for tweet in allTweets:
        tweetTitles.append(Twitter.process_twitter_title(allTweets, i))
        print tweetTitles[i]
        i = i + 1
    #end of twitter bypass

    for storyId in range(3): #checks first 3 story titles against all tweets to see if story has been posted before
        #TODO make sure there actually are 3 stories.  All we know so far is there were more than None
        story = NewsGatherer.parse_news_stories(newsResponse, storyId)
        storyTitle = NewsGatherer.parse_news_title(story)
        alreadyPosted = False
        i = 0
        while not alreadyPosted and i < len(tweetTitles):
            if storyTitle != tweetTitles[i]:
                i++
            else:
                alreadyPosted = True
        if not alreadyPosted:
            #TODO call url shortenener, pass to final tweet
            #for now the tweet function only takes storyId as an argument?
            #also tweet function has an empty return

            #move news_story_to_tweet from logic to Twitter?
            #or change tweet function to accept storyId and title as arguments?

            #Twitter.tweet(storyId)