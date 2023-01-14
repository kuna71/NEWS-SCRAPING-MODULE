import praw
import pandas as pd
from URLParser import CheckLink
from FeatureExtractor import ExtractText
from FeatureExtractor import ExtractTitle
from urllib.parse import *
import bs4
from LanguageDetection import IsEnglish
count=0
reddit = praw.Reddit(
    client_id = "YOUR CLIENT ID",
    client_secret = "YOUR CLIENT SECRET",
    user_agent = 'YOUR USER AGENT',
)

def ScrapeReddit(subreddit_list):
    print("\n\n\n\n_______________________PERFORMING REDDIT SCRAPE________________________\n")
    # subreddit_list = ["DesiMeta", "India"]
    subreddits =[]
    for sub in subreddit_list:
        subreddits.append(reddit.subreddit(sub))
    posts = []
    urls = []
    post_data = []
    total_score=0
    count=0
    for s in subreddits:
        for submission in s.top(time_filter = "day", limit=None):
            try:
                if(submission.selftext=="" and CheckLink(submission.url)):
                    count= count+1
                    posts.append(submission)
                    score = submission.score
                    if(score<3):
                        continue
                    print("score:"+str(score))
                    total_score = total_score + score
                    try:
                        text = ExtractText(submission.url)
                        title = ExtractTitle(submission.url)
                        if(not IsEnglish(title)):
                            print("Non english language detected--discarding")
                            continue
                    except Exception as e:
                        print("Error whilst extracting features: " + str(e))
                        continue
                    print(submission.title)
                    this_post = [title, submission.url, text, "Reddit"]
                    if(this_post not in post_data):
                        post_data.append([title, submission.url, text, "Reddit"])
                    # count=count+1
            except Exception as e:
                print(e)
        print("Average: ")
        print(total_score/count)
        return post_data