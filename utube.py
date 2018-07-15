import sys
import bs4 as bs
import urllib.request
from urllib.parse import quote_plus
import re
import requests

def download(url):
    #base_url = "https://9xbuddy.app/process?url="
    base_url = "https://qdownloader.net/download?video="
    #url = input()
    #url = quote_plus(url)
    final_url = base_url + url
    #print(final_url)
    r = requests.get(final_url)
    #print(client_response.html)
    soup = bs.BeautifulSoup(r.text,"lxml")
    links = []

    for i in soup.find_all('a',href=True):
        link = i['href']
        if 'itag=18' in link or 'itag=22' in link:
            links.append(link)
    return links
