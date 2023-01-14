from facebook_scraper import get_posts
from datetime import datetime
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

from URLParser import CheckLink
from FeatureExtractor import ExtractText
from FeatureExtractor import ExtractTitle
from LanguageDetection import IsEnglish
import re
listposts = []

# 'indianavaz', 428218115129201,

# grp = ['indianavaz']
def Find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)
    temp = [x[0] for x in url]
    if(len(temp)==0):
        return False
    else:
        return temp[0]
def ScrapeFacebook(grps):
    print(print("\n\n\n\n_______________________PERFORMING FACEBOOK SCRAPE________________________\n"))
    for group in grps:
        try:
            for post in get_posts(group, pages=10):
                    print(group)
                    # print("__________________________________________________________________________________________________________")
                    # print(post['link'])
                    if(post['link']!= None):
                        url = post['link']
                        date = post['time']
                        if(date.date() == datetime.now().date):
                            if(CheckLink(url)):
                                print("URL:" + url + "\n")
                                text_content = ExtractText(url)
                                title = ExtractTitle(url)
                                if(not langdetect(title)):
                                    continue
                                listposts.append([title, url, text_content, "Facebook"])
                                print([title, url, text_content, "Facebook"])

                                
                    # temp = post['time']
                    # if temp.date() == a.date():
        except Exception as e:
            print(e)
    return listposts
# print(ScrapeFacebook())
