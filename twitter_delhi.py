from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient

MONGO_HOST = 'mongodb://localhost/twitterdb'  # assuming you have mongoDB installed locally
# and a database called 'twitterdb'
#WORDS = ['#Smog', '#MyRightToBreathe', '#SmogInDelhi', '#DelhiSmog', '#CropBurning', '#MumbaiRains', '#CycloneOckhi', '#CycloneOkhi', '#ockhicyclone']
WORDS = ['#Smog', '#MyRightToBreathe', '#SmogInDelhi', '#DelhiSmog', '#CropBurning']
CONSUMER_KEY = "sniGt6dU1HfH8cgkwZfGteAyu"
CONSUMER_SECRET = "Wu99GU7W7BIdF1GjtrRn8MHreOJJpLt0tOodIgMCoLNCgauG8I"
ACCESS_TOKEN = "925715961788764160-xhzCZHYhGYXbxz0cC7bSPVOmroBVdr8"
ACCESS_TOKEN_SECRET = "bcQrRhoU8fCbqEif6IuKQSqnn4uYOpQSSRzB7JytIrxoX"


class StreamListener(tweepy.StreamListener):

    def on_connect(self):
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        try:
            client = MongoClient(MONGO_HOST)

            db = client.twitterdb
            datajson = json.loads(data)
            created_at = datajson['created_at']
            print("Tweet collected at " + str(created_at))
            db.twitter_search.insert(datajson)
        except Exception as e:
            print(e)


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)
