import tweepy
from tweepy import OAuthHandler

consumer_key = 'NYICJJWGEHWjLzf16L4bdOmBp'
consumer_secret = 'AT8vDFvB6IkjLM5Ckz9DC5yQ0nsqut8vwGYOpnXPMFIESsHKG5'
access_token = '2909697444-NNDWfyczj7Asgv7t5YvysLcnnEj3CcoC12AB46R'
access_secret = 'kRaSQf3FEEz3X7TSH1o0EisdweIGoxm9Af6E0WceFzeEp'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.user_timeline).items(1):
    # Process a single status
    print (tweet._json)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print (tweet.text)
