import tweepy

auth = tweepy.OAuthHandler('L8mHYjnbVoOpKQ5KbTvps2hHt', 'HC8ETgLRsAFqedlaq5h1CyHuKm7EcukMYYX9eELo19buuoFaiF')
auth.set_access_token('801874596798439424-HCfH0BPJlaa2pHVGMvDEedM2Zp0L5Gk', 'rj7gkLcMW52p0BjArLOhea1lF9u8gVhKplfX4pgCV0fDB')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)