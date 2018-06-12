import NewsGatherer
import Twitter
import Debugging

# TODO :
# todo: place in prod twitter auth token
#TODO fix short url
#TODO It looks like I am getting an issue with non ascii characters in title?
#TODO for better testing.  iva change to only post 1 story
'''
C:\Python27\python.exe C:/Users/Chris/Documents/GitHub/TwitterCreater/main.py
https://newsapi.org/v2/everything?q=tall%20ships&from=2018-06-11&to=2018-06-11&apiKey=62632fc6669e4cc6975ea775834492a3
Traceback (most recent call last):
  File "C:/Users/Chris/Documents/GitHub/TwitterCreater/main.py", line 39, in <module>
    Twitter.tweet(storyTitle, storyUrl)
  File "C:\Users\Chris\Documents\GitHub\TwitterCreater\Twitter.py", line 32, in tweet
    print('>>Attempting to tweet: '+ str(status))
UnicodeEncodeError: 'ascii' codec can't encode character u'\u2019' in position 1: ordinal not in range(128)
'''


# -get news stories that fit query
newsResponse = NewsGatherer.get_news_stories()
if newsResponse['status'] == 'ok' and newsResponse['totalResults'] > 0:
    tweetTitles = []
    if Debugging.debugging_flag() == True:  # bypass call to twitter
        allTweets = [u'OPPO A83 (2018) Mid-Ranger Now Expanding Beyond India:\nhttps://t.co/cB2wiEv366',u'An Incredible, One-of-a-Kind Expanding Tiny House \u2014 House Tour Greatest Hits:\nhttps://t.co/O9U2aSAysQ']
        i = 0
        for tweet in allTweets:
            tweetTitles.append(Twitter.process_twitter_title(allTweets, i)) #todo should make this use parse_tweets_all
            i = i + 1
    else:  # get tweets from twitter
        publicTweets = Twitter.get_tweets_all()
        tweetTitles= (Twitter.parse_tweets_all(publicTweets))
    for storyId in range(1):  # checks first 1 story titles against all tweets to see if story has been posted before
        # TODO make sure there actually are 3 stories.  All we know so far is there were more than None
        story = NewsGatherer.parse_news_stories(newsResponse, storyId)
        storyTitle = NewsGatherer.parse_news_title(story)
        storyUrl = NewsGatherer.parse_news_url(story)
        alreadyPosted = False
        i = 0
        while not alreadyPosted and i < len(tweetTitles):
            if storyTitle != tweetTitles[i]:
                i = i + 1
            else:
                alreadyPosted = True
                print('>>News Story already tweeted: ' + str(storyTitle))
        if not alreadyPosted:
            # todo tweet function has an empty return
#            shortUrl = ShortUrl.goo_shorten_url(storyUrl) #TODO uh.... this is not working
            Twitter.tweet(storyTitle, storyUrl)
else: # newsResponse['status'] != 'ok' and newsResponse['totalResults'] !> 0
    print('No News Stories from Today: '+ str(newsResponse))