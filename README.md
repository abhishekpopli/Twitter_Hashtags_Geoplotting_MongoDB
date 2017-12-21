# Twitter_Hashtags_Geoplotting_MongoDB
Analysed the data collected from Twitter of 10k tweets each for Delhi Smog and Ockhi Cyclone and stored them in MongoDB. 
Tweepy library used with both streaming and past tweets gathering.
Extracted and analysed locations of the tweets and plotted them using Google charts. 

Evaluated tweets of non-Delhi and non-Mumbai locations and tried to find the top 10 hashtags used.
Using Twitter_locations.py, I extracted the locations and then saved that in Twitter_locations.txt, which is used in HTML file for  plotting it.

Different collection for Delhi and Mumbai were made and twitter-delhi, twitter-mumbai.py are Twitter stream listeners saving respective tweets in MongoDB database "twitterdb". While twitter_nostreaming.py extracts previous tweets of particluar hashtags.

To be done:
1.Distribution of Original Tweets vs Retweeted Tweets
2.Distribution of favorite counts on Original Tweets
3.Distribution of Type of Tweet i.e. Text, Image, Text+Image
