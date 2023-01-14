from RedditScraper import ScrapeReddit
from TwitterScraper import ScrapeTwitter
from facebookScraper import ScrapeFacebook
from ScrapeGoogle import ScrapeGoogle
import pandas as pd
import itertools
from datetime import datetime
from multiprocessing import Process
from multiprocessing import Manager
import tweepy
from time import sleep

TWITTER_SEARCH_WORDS = ""       #list of words to search on Twitter
REDDIT_SUBREDDIT_LIST = [""]    #list of subreddits to scrape as strings
GOOGLE_NEWS_LINK = ""           #link of news.google.com page with search performed
FACEBOOK_GROUPS =[""]             #list of facebook group ids to search in as strings

def ScrapeAll():
    print("______________________INITIATING SCRAPE_________________________")
    numtweets = 900
    cumulative_article_tweet_data = []
    try:
        cumulative_article_tweet_data = ScrapeTwitter(TWITTER_SEARCH_WORDS, numtweets)
        print(cumulative_article_tweet_data)
    except Exception as e:
        print("Twitter Scrape failed due to" + str(e))

    #-------------------------------------REDDIT-------------------------------------------ScrapeReddit
    try:
        reddit_data = ScrapeReddit(REDDIT_SUBREDDIT_LIST)
    except Exception as e:
        print("Reddit scrape failed due to " + str(e))
        reddit_data =  [[], [], [], []]
    try:
        facebook_data = ScrapeFacebook(grps = FACEBOOK_GROUPS)
    except Exception as e:
        print("Facebook scrape failed due to: "+str(e))
        facebook_data = [[], [], [], []]
    try:
        google_data = ScrapeGoogle(GOOGLE_NEWS_LINK)
    except Exception as e:
        print("Google scrape failed due to: "+str(e))
        google_data = [[], [], [], []]

    data = cumulative_article_tweet_data + reddit_data + facebook_data + google_data
    return data

def ToCSV():
    columns = ['Title', 'URL', 'Text', 'Source']
    data = ScrapeAll()
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(str(datetime.now().date()) + "_scrape_output.csv")
ToCSV()
