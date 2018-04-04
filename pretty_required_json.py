# To use this method, type in directory of the source json file and the name of the source json file (without .json)
# python3 pretty_required_json.py -fn stream_movie -d data

import json
import argparse
import string

def get_parser():
    # Get parser for command line arguments.
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-fn",
                        "--fname",
                        dest="fname")
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        help="Output/Data Directory")
    return parser

def full_version_json(source_file, data_dir):
    # Full version of pretty json
    with open('data/stream_movie.json', 'r') as f:
        content = f.readlines() # read only the first tweet/line
        for tweet in content:
            t = json.loads(tweet)
            outfile = "%s/%s_pretty.json" % (data_dir, source_file)
            with open(outfile, 'a') as ff:
                ff.write(json.dumps(t,indent=4)) # pretty-print
                ff.write('\n')

def required_version_json(source_file, data_dir):
    # Required fields version of json
    with open('data/stream_movie.json', 'r') as f:
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
            outfile = "%s/%s_pretty_required.json" % (data_dir, source_file)
            with open(outfile, 'a') as ff:
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

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    full_version_json(args.fname, args.data_dir)
    required_version_json(args.fname, args.data_dir)
