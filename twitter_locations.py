import json
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.twitterdb
geodata = {}
cursor = db.twitter_mumbai.find()
for result_object in cursor:
    tweet = result_object
    user_location = tweet['user']['location']
    if user_location:
        if user_location in geodata:
            geodata[user_location] += 1
        else:
            geodata[user_location] =  1
print("The file included " + str(len(geodata)) + " location of unique users who tweeted.")

with open('twitter_location.txt', 'w', encoding='utf-8') as fout:
    for x, y in geodata.items():
        string = "['" + str(x) + "'," + str(y) +  "],\n"
        fout.write(string)