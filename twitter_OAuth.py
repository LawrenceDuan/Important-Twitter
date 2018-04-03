import tweepy
from tweepy import OAuthHandler

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.user_timeline).items(1):
    # Process a single status
    print (tweet._json)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print (tweet.text)
