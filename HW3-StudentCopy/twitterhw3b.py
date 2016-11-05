# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "785666803141791745-Up8FcR38RsPhHWhboKLoq5I6SSnVypC"
access_token_secret = "N7VpAftHI8nWXsNccnf63WeSam9LEYZmQcJoJVoLqJmVy"
consumer_key = "5B5FJ0xi6wZug3sV8Uac51dDZ"
consumer_secret = "93kcKh8OjBq2K5a2wJjKhxE5EqeH8h64gNaRYhbwnEW4BBjaUh"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search(input("Enter your preferred search term:"))

numtweets = 0
# Two lists created to store polarity and subjectivity of each tweet
lst_pol = []
lst_sub = []

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    numtweets += 1
    lst_pol.append(analysis.sentiment.polarity)
    lst_sub.append(analysis.sentiment.subjectivity)
print ('Average polarity:', sum(lst_pol) / numtweets, 
	   'Average subjectivity:', sum(lst_sub) / numtweets)

# print ('Number of tweets:', numtweets, 'Total polarity:', sum(lst_pol),'Total subjectivity:', sum(lst_sub))


#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data

