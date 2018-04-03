import json

with open('data/stream_apple.json', 'r') as f:
    content = f.readlines() # read only the first tweet/line
    for tweet in content:
        with open('data/pretty.json', 'a') as ff:
            tweet = json.loads(tweet) # load it as Python dict
            ff.write(json.dumps(tweet, indent=4)) # pretty-print
            ff.write('\n')
