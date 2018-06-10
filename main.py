import NewsGatherer
import Twitter
import ShortUrl
import Debugging

# TODO :
# todo: place in prod twitter auth token
#TODO fix short url


# -get news stories that fit query
newsResponse = NewsGatherer.get_news_stories()
if newsResponse['status'] == 'ok' and newsResponse['totalResults'] > 0:
    tweetTitles = []
    if Debugging.debugging_flag() == True:  # bypass call to twitter
        allTweets = [u'OPPO A83 (2018) Mid-Ranger Now Expanding Beyond India:\nhttps://t.co/cB2wiEv366',u'An Incredible, One-of-a-Kind Expanding Tiny House \u2014 House Tour Greatest Hits:\nhttps://t.co/O9U2aSAysQ']
        i = 0
        for tweet in allTweets:
            tweetTitles.append(Twitter.process_twitter_title(allTweets, i))
            i = i + 1
    else:  # get tweets from twitter
        publicTweets = Twitter.get_tweets_all()
        tweetTitles.append(Twitter.parse_tweets_all(publicTweets))
    for storyId in range(3):  # checks first 3 story titles against all tweets to see if story has been posted before
        # TODO make sure there actually are 3 stories.  All we know so far is there were more than None
        story = NewsGatherer.parse_news_stories(newsResponse, storyId)
        storyTitle = NewsGatherer.parse_news_title(story)
        storyUrl = NewsGatherer.parse_news_url(story)
        alreadyPosted = False
        i = 0
        #TODO TESTING HERE
        print(storyTitle)
        print(tweetTitles)
        print(tweetTitles[0])
        #end testing
        while not alreadyPosted and i < len(tweetTitles):
            if storyTitle != tweetTitles[i]:
                i = i + 1
            else:
                alreadyPosted = True
        if not alreadyPosted:
            # todo tweet function has an empty return
            shortUrl = ShortUrl.goo_shorten_url(storyUrl) #TODO uh.... this is not working
            Twitter.tweet(storyTitle, shortUrl)