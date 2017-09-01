#here we perform  twitter sentiment analysis ans also 
#stores the tweets in csv file

import tweepy 
from textblob import TextBlob  #  textblob is a python library that lets you perform sentiment analysis
import csv


#authenticating with twitter
consumer_key = "QW9cu9ofCqq0AXWz8dmFxl2Xb"
consumer_secret_key = "pmKVCqIuN57nXn1q2P7EWFidghUrfiA38Vx6NtTqQgoQp1SQM4"


access_token = "327365009-DTtkWwCZbKmminXJynigubaXSONhrcSKYjTudxmV"
access_token_secret = "BASUmZdJc9Zwqcc0DyO27wGRp8pGpzAMwWetzAjlVLhCq"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key) # OAuthHandler is a method of tweepy 
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# here we retrieve tweets
public_tweets  =api.search("nepal")

#this code opens/creates a file to append data to
csvFile = open("result.csv","a")

# we use csv Writer
csvWriter = csv.writer(csvFile)


for tweets in public_tweets:
	print(tweets.text)


	# print ("\n")
# #here we tokenize each word from tweet
# 	print("Tokenized words ")
# 	slics = TextBlob(tweets.text)
# 	print(slics.words)	


# here we perform sentiment analysis
	analysis = TextBlob(tweets.text)
	print(analysis.sentiment)
	print("\n")
			

	#we write to CSv file. I use encode UTF-8
	csvWriter.writerow([tweets.created_at,tweets.text.encode('utf-8')])
	
	print (tweets.created_at,tweets.text)
	if analysis.sentiment.polarity>0:
		print ("**This tweet is Positive**")
	elif analysis.sentiment.polarity==0:
		print ("**This tweet is Neutral**")
	else:
		print ("**This tweet is Negative**")
	
	csvWriter.writerow([analysis.sentiment.polarity])
csvFile.close()
	


