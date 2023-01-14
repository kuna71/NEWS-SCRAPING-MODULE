import tweepy
import time
import re
from URLParser import CheckLink
from URLParser import resolve_url
from FeatureExtractor import ExtractText
from FeatureExtractor import ExtractTitle
import os
import time
from LanguageDetection import IsEnglish


import pandas as pd
import tweepy
from datetime import datetime
import re
from multiprocessing import Queue
from time import sleep

def PopularityScore(tweet):
    rtCount = tweet.retweet_count
    return rtCount
def info(title):
    print("PROCESS INFO")
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
def RemoveLink(text):
    processed_text = re.sub(r'http\S+', '', text)
    return processed_text
#function to authorize the twitter api
def Authorize():
    consumer_secret = "YOUR CONSUMER SECRET"
    consumer_key = "YOUR CONSUMER KEY"
    access_key = "YOUR ACCESS KEY"
    access_secret = "YOUR ACCESS SECRET"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return api

#function to find urls within a string
def Find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)
    temp = [x[0] for x in url]
    if(len(temp)<=1):
        return False
    else:
        return temp[0]
# function to display data of each tweet
def printtweetdata(article_tweet_data):
    for t in article_tweet_data:
        print("Text: "+ t[0])
        print("URL: "+ t[1])
        print("____________________________________________________________")

# function to perform data extraction
def ScrapeTwitter(words, numtweet):
        info(title='ScrapeTwitter')
        print("\n\n\n\n_______________________PERFORMING TWITTER SCRAPE________________________\n")
        totalRetweets = 0
        date_since = datetime.now().date()
        api = Authorize()
        article_tweet_data=[]
        non_article_tweet_data = []
        try:
            tweets = tweepy.Cursor(api.search_tweets,
                                   words, lang="en",
                                   since_id=date_since,
                                   tweet_mode='extended').items(numtweet)
        except Exception as e:
            print(e)
        list_tweets = [tweet for tweet in tweets]
        total = len(list_tweets)
        i = 1
        for tweet in list_tweets:
                score = PopularityScore(tweet)
                if(score<300):
                    continue
                totalRetweets = totalRetweets+score
                print("Score: "+str(score))
                # sleep(2)
                try:
                        text = tweet.retweeted_status.full_text
                except AttributeError:
                        text = tweet.full_text
                if(Find(text)):
                    url = Find(text)
                    try:
                        expandedURL = resolve_url(url)
                    except Exception as e:
                        print("Failed to get expanded URL")
                        print(e)
                        continue
                elif(not Find(text)):
                    try:
                        processed_text = RemoveLink(text)
                        print("Non article tweet: " + processed_text)
                        tweetObject = [processed_text, "Twitter"]
                        if(tweetObject not in non_article_tweet_data):
                            non_article_tweet_data.append(tweetObject)
                        continue
                    except Exception as e:
                        print(e)
                else:
                    continue
                try:
                    if(CheckLink(expandedURL)):
                        print("Valid link")
                        try:
                            text_content = ExtractText(expandedURL)
                            title = ExtractTitle(expandedURL)
                            if(not IsEnglish(title)):
                                print("Non english language detected--discarding")
                                continue
                            this_post = [title, expandedURL, text_content, "Twitter"]
                            if(this_post not in article_tweet_data):
                                article_tweet_data.append(this_post)
                            print("Article found:")
                            print([title, expandedURL, text_content])
                        except Exception as e:
                            print(e)
                            print("unable to extract text")
                            continue
                except Exception as e:
                    print(e)
        print(i)
        avg = totalRetweets/total
        print("average: " + str(avg))
        # return_queue.put([article_tweet_data, non_article_tweet_data])
        return article_tweet_data
# ScrapeTwitter("india ", 100)
