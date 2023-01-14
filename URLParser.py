from urllib.parse import *
from bs4 import BeautifulSoup
import requests
import metadata_parser  
import re
import selenium
def resolve_url(twitter_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(url = twitter_url,headers=headers)
    data = r.text
    url = re.search("(?P<url>https?://[^\s]+)\"", data).group("url")
    return url

def CheckLink(link):
    print("CHECKING LINK")
    parse = urlparse(link)
    if(parse.netloc=='imgur.com'):
        return False
    try:
        response = requests.get(link)
    except Exception as e:
        print(e)
        return False
    soup = BeautifulSoup(response.text, features = 'lxml')
    metas = soup.find_all('meta')
    for m in metas:
        if(m.get('property')=='og:type'):
            desc = m.get('content')
            if(desc=='article'):
                return True
    return False
