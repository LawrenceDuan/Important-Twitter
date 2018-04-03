import json

with open('data/stream_apple.json', 'r') as f:
    content = f.readlines() # read only the first tweet/line
    for tweet in content:
        t = json.loads(tweet)
        new_t = {}
        for k, v in t.items():
            if k == "user": new_t.update({k:v})
            if k == "id": new_t.update({k:v})
            if k == "lang": new_t.update({k:v})
            if k == "text": new_t.update({k:v})
            if k == "created_at": new_t.update({k:v})
            if k == "favorite_count": new_t.update({k:v})
            if k == "retweet_count": new_t.update({k:v})
            if k == "favorited": new_t.update({k:v})
            if k == "retweeted": new_t.update({k:v})
        with open('data/pretty.json', 'a') as ff:
            ff.write(json.dumps(new_t,sort_keys=True,indent=4)) # pretty-print
            ff.write('\n')

# created_at: the date of creation
# favorite_count, retweet_count: the number of favourites and retweets
# favorited, retweeted: boolean stating whether the authenticated user (you) have favourited or retweeted this tweet
# lang: acronym for the language (e.g. “en” for english)
# id: the tweet identifier
# place, coordinates, geo: geo-location information if available
# user: the author’s full profile
# entities: list of entities like URLs, @-mentions, hashtags and symbols
# in_reply_to_user_id: user identifier if the tweet is a reply to a specific user
# in_reply_to_status_id: status identifier id the tweet is a reply to a specific status
