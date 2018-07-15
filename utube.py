import sys
import bs4 as bs
import urllib.request
from urllib.parse import quote_plus
import re
from requests_html import HTMLSession

def download(url):
    #base_url = "https://9xbuddy.app/process?url="
    base_url = "https://qdownloader.net/download?video="
    #url = input()
    #url = quote_plus(url)
    final_url = base_url + url
    #print(final_url)
    session = HTMLSession()
    r = session.get(final_url)
    r.html.render()
    #print(client_response.html)
    soup = bs.BeautifulSoup(r.text,"lxml")
    links = []

    for i in soup.find_all('a',href=True):
        link = i['href']
        if 'itag=18' in link or 'itag=22' in link:
            links.append(link)
    return links
