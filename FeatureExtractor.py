import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import trafilatura
import json
import spacy
from requests.models import MissingSchema
import numpy as np
def ExtractTitle(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    paras = soup.findAll('title')
    content = " "
    for ele in paras:
        content = content + (ele.text)
    return content

def FallbackFunction(response_content):

    soup = BeautifulSoup(response_content, 'html.parser')

    # Finding the text:
    text = soup.find_all(text=True)

    # Remove unwanted tag elements:
    cleaned_text = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script',
        'style',]

    for item in text:
        if item.parent.name not in blacklist:
            cleaned_text += '{} '.format(item)

    # removing tabs and end of lines
    cleaned_text = cleaned_text.replace('\t', '')
    cleaned_text = cleaned_text.replace('\n', '')
    cleaned_text = cleaned_text.replace('\r', '')

    return cleaned_text.strip()


def ExtractText(url):

    downloaded_url = trafilatura.fetch_url(url)
    try:
        a = trafilatura.extract(downloaded_url, output_format='json', with_metadata=True, include_comments = False,
                            date_extraction_params={'extensive_search': True, 'original_date': True})
    except AttributeError:
        a = trafilatura.extract(downloaded_url, output_format='json', with_metadata=True,
                            date_extraction_params={'extensive_search': True, 'original_date': True})
    if a:
        json_output = json.loads(a)
        return json_output['text']
    else:
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                return FallbackFunction(resp.content)
            else:

                return np.nan
        except MissingSchema:
            return np.nan
