# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 09:46:16 2020

@author: Funmi
"""


#IMPORTING PACKAGES
import tweepy
import re  
import random
import time


#API ACCESS
auth = tweepy.OAuthHandler("consumerKey","consumerSecret")
auth.set_access_token("accessToken","accessTokenSecret")
api = tweepy.API(auth)


#TARGET TWITTER HANDLES
usernames = ["vanguardngrnews", "mobilepunch", "SaharaReporters", "GuardianNigeria", "DailyPostNGR", "PremiumTimesng", "daily_trust", "TheNationNews", "THISDAYLIVE"]


#CREATING A LIST FOR TWEETS TEXT
tweets = []
for name in usernames:
  tweet = api.user_timeline(screen_name = name, tweet_mode = "extended")
  tweets.append(tweet[0].full_text.lower())
#print(tweets)


#REPLACEMENT DICTIONARY
KeywordAndReplacement = {"lagos": "lasgidi", "warri": "wafi"...............................}


#REPLACING KEYWORDS AND REMOVING URLS
new_tweets = []

for each in tweets:
    for key, value in KeywordAndReplacement.items():
        if key in each:
            each = each.replace(key, KeywordAndReplacement[key])
    each = re.sub(r"http\S+", "", each)
    new_tweets.append(each)
    #print(each)
#print(new_tweets)


#SELECTING RANDOM TWEETS    
i = 0
unique_tweet = []
reference = dict(zip(usernames, new_tweets))

while i < len(new_tweets):
    random_username = random.choice(usernames)
    
    if random_username not in unique_tweet:
        time.sleep(10)
        i += 1
        unique_tweet.append(random_username)
        finalTweet = random_username + "---" + reference[random_username].capitalize()
        print(finalTweet)


#TWEET OUT 
#api.update_status(finalTweet)
