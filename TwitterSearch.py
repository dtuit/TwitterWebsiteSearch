import twitter
import os
import json

keys = {}

with open('keys.json') as keys_file:
    keys = json.load(keys_file)

api = twitter.Api(keys['CONSUMER_KEY'],
                keys['CONSUMER_SECRET'],
                keys['ACCESS_TOKEN'],
                keys['ACCESS_TOKEN_SECRET'])

USERS = ['$AAPL']

def main():
    with open('output.txt', 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(track=USERS):
            f.write(json.dumps(line))
            f.write('\n')

if __name__ == '__main__':
    main()