# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

# print("""No output necessary although you 
	# can print out a success/failure message if you want to.""")

import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "785666803141791745-Up8FcR38RsPhHWhboKLoq5I6SSnVypC"
access_token_secret = "N7VpAftHI8nWXsNccnf63WeSam9LEYZmQcJoJVoLqJmVy"
consumer_key = "5B5FJ0xi6wZug3sV8Uac51dDZ"
consumer_secret = "93kcKh8OjBq2K5a2wJjKhxE5EqeH8h64gNaRYhbwnEW4BBjaUh"

# Boilerplate code here - a lot of code
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
img_url = 'media/image.jpg'

# API.update_with_media tweets out a status with an image
api.update_with_media(img_url, '#UMSI-206 #Proj3')