import tweepy
from tweepy import OAuthHandler
from pymongo import MongoClient


#searchQuery = ' #Smog OR #MyRightToBreathe OR #CropBurning OR #MumbaiRains OR #CycloneOckhi OR  #delhismog OR #teaminstinct OR #teamvalor OR'


def auth(consumer_key, consumer_secret, access_token, access_secret):
        # Authenticate
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)
        return (api)

def dTweets( api, hashtag, number):
        curs = tweepy.Cursor(api.search, q=hashtag).items(number)
        for c in curs:
                cJson = c._json
                saveToMongo(cJson)
        return ("All done")


def saveToMongo(result):
        MONGO_HOST = 'mongodb://localhost/twitterdb'
        client = MongoClient(MONGO_HOST)
        db = client.twitterdb
        db.twitter_mumbai.insert(result)


def main():
        CONSUMER_KEY = "sniGt6dU1HfH8cgkwZfGteAyu"
        CONSUMER_SECRET = "Wu99GU7W7BIdF1GjtrRn8MHreOJJpLt0tOodIgMCoLNCgauG8I"
        ACCESS_TOKEN = "925715961788764160-xhzCZHYhGYXbxz0cC7bSPVOmroBVdr8"
        ACCESS_TOKEN_SECRET = "bcQrRhoU8fCbqEif6IuKQSqnn4uYOpQSSRzB7JytIrxoX"
        hashtag = "SaveFishermen"
        number_items = 4000
        api = auth(CONSUMER_KEY,CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        print( dTweets(api, hashtag, number_items))


if __name__ == "__main__":
        main()