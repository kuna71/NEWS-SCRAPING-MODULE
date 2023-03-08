[ReadMe.txt](https://github.com/kuna71/NEWS-SCRAPING-MODULE/files/10417161/ReadMe.txt)
# NEWS-SCRAPING-MODULE
This module scrapes Twitter, Facebook, Reddit and Google News for specific articles as per choice.

STEPS: 

    1. ENVIRONMENT:
        Install dependencies by executing "pip install -r requirements.txt" in the terminal
    2. TWITTER SETUP:
        a. Set up twitter developer account and ask for api keys. 
        b. Follow Getting Twitter API authentication in this article for reference: https://towardsdatascience.com/how-to-access-twitters-api-using-tweepy-5a13a206683b
        c. Once you have received neccessary access keys, assign respective values in TwitterScraper.py script [34,37]
        d. 
    3. REDDIT SETUP:
        a. Create a reddit account and create an app here https://www.reddit.com/prefs/apps
        b. Obtain Client ID, Client Secret and User Agent
        c. Assign respective values in RedditScraper.py [11,12,13]
    3. Execute ScrapeDaddy with neccessary parameters
        a. Enter words to search for on twitter as space seperated string in TWITTER_SEARCH_WORDS (eg: "US Government"(13)
        b. Enter subreddits to parse through for articles (eg: "USpolitics) in a list of strings REDDIT_SUBREDDIT_LIST
        c. Search your topic of choice on google news, copy URL of page and paste in GOOGLE_NEWS_LINK
        d. Get group ids of facebook groups to search for articles and put in FACEBOOK_GROUPS as list of strings

OUTPUT WILL BE IN CSV FORMAT, saved as "(date)_scrape_output.csv"
