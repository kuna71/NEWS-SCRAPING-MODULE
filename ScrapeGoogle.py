import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from FeatureExtractor import ExtractText
from FeatureExtractor import ExtractTitle
from URLParser import CheckLink
import re

def Find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)
    temp = [x[0] for x in url]
    return temp[0]

def ScrapeGoogle(link):
    root = "www.google.com"
    # result = Request.get(link)
    request_result=requests.get(link)
    soup = BeautifulSoup(request_result.text, features='html.parser')
    # print(soup)
    headings= soup.find_all('h4')
    print("____")
    first = 'https://news.google.com/'
    i=0
    google_data =[]
    for h in headings:
        second = h.a['href']
        url = first+second
        if(CheckLink(url)):
            title = ExtractTitle(url)
            full_text=  ExtractText(url)
            text = ExtractText(Find(full_text))
            google_data.append([title, url, text, "Google"])
            print([title, url, text, "Google"])
    return google_data
    # content = soup.find('div', attrs={'class':"xuvV6b BGxR7d"})
    # print(content)
# ScrapeGoogle()
# print(ScrapeGoogle("https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"))
