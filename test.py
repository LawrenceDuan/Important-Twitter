import tweepy
from tweepy import OAuthHandler
import csv
import config
import json

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
api = tweepy.API(auth)

# # Open/Create a file to append data
# csvFile = open('tweets3.csv', 'a')
# #Use csv Writer
# csvWriter = csv.writer(csvFile)


# for tweet in tweepy.Cursor(api.search,count=100, lang="en", user_id="515061026",since_id="2018-01-01").items():
#     print (tweet.created_at, tweet.text)
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), ])
# # q="#ps4"

# status_list = api.user_timeline(user_id = '2895676380', count = 1, include_rts = True)
# for status in status_list:
#     # csvWriter.writerow([stuff.created_at, stuff.text.encode('utf-8'), ])
#     json_str = json.dumps(status._json, indent=4)
#     print(json_str, '\n')
    # for tweet in status._json:
    #     t = json.loads(tweet)
    #     print(json.dumps(t,indent=4))
    #     print ('\n')
# print (stuff)

# user = api.get_user(user_id = "2895676380")
# print(user)


# with open('test.json', 'a') as f:
#     status_list = api.user_timeline(user_id = '2895676380', count = 50, include_rts = True)
#     for status in status_list:
#         # csvWriter.writerow([stuff.created_at, stuff.text.encode('utf-8'), ])
#         json_str = json.dumps(status._json)
#         json_str.
#         f.write(json_str)
#         f.write('\n')

# print("111")
# print (api.retweets(989547112441438208))
# for reTweet in api.retweets(989544173744275456):
#     print("USER:", reTweet.user.screen_name)

status = api.get_status(989547112441438208)
for reTweet in api.retweets(status.retweeted_status.id):
    print("USER:", reTweet.user.screen_name)
# print(status.retweeted_status.retweet_count)
