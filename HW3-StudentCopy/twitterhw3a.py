# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

# print("""No output necessary although you 
	# can print out a success/failure message if you want to.""")

import tweepy, stuff
from textblob import TextBlob

# Boilerplate code here
auth = tweepy.OAuthHandler(stuff.consumer_key,stuff.consumer_secret)
auth.set_access_token(stuff.access_token,stuff.access_token_secret)

api = tweepy.API(auth)
img_url = 'media/image.jpg'

# API.update_with_media tweets out a status with an image
api.update_with_media(img_url, '#UMSI-206 #Proj3')