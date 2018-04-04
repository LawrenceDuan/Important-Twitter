import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import config
import json
import urllib3.exceptions
import http
import sys

def get_parser():
    # Get parser for command line arguments.
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        help="Output/Data Directory")
    parser.add_argument("-n",
                        "--number",
                        dest="number")
    return parser

class MyListener(StreamListener):
    # Custom StreamListener for streaming data.

    def __init__(self, data_dir, query, number):
        query_fname = format_filename(query)
        self.outfile = "%s/stream_%s.json" % (data_dir, query_fname)
        self.number = int(number)

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                temp_number = print_count(self.outfile)
        except BaseException as e:
            print("Error on_data: %s, Pausing..." % str(e))
            print("~~~ Restarting stream search in 5 seconds... ~~~")
            time.sleep(5)
            return True

        if temp_number == self.number: return False
        if temp_number < self.number: return True

    def on_error(self, status):
        print(status)
        return True

def format_filename(fname):
    # Convert file name into a safe string.
    # Arguments:
    #     fname -- the file name to convert
    # Return:
    #     String -- converted file name
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    # Convert a character into '_' if invalid.
    # Arguments:
    #     one_char -- the char to convert
    # Return:
    #     Character -- converted char
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

def print_count(outfile_name):
    with open(outfile_name, 'r') as f:
        for i, l in enumerate(f):
            pass
        print (i + 1, end='\r')
        return i+1

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)

    twitter_stream = Stream(auth, MyListener(args.data_dir, args.query, args.number))
    streamer_monitor = True
    while streamer_monitor:
        try:
            twitter_stream.filter(track=[args.query])
            file = "%s/stream_%s.json" % (args.data_dir, args.query)
            with open(file, 'r') as f:
                for i, l in enumerate(f):
                    pass
                if i == int(args.number):
                    streamer_monitor = False
        except http.client.IncompleteRead as e:
            print("http.client Incomplete Read error: %s" % str(e))
            print("~~~ Restarting stream search in 5 seconds... ~~~")
            time.sleep(5)
            continue
        except urllib3.exceptions.ProtocolError as e:
            print("urllib3 Incomplete Read error: %s" % str(e))
            print("~~~ Restarting stream search in 5 seconds... ~~~")
            time.sleep(5)
            continue
        except KeyboardInterrupt as e:
            streamer_monitor = False
