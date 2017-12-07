import re
import requests
from bs4 import BeautifulSoup


def get_page(page_url):
    with requests.Session() as s:
        page = s.get(page_url)
        return page.text


def crawl(url):
    page_content = get_page(url)
    soup = BeautifulSoup(page_content, "html.parser")
    print(soup.findAll('h1').get_text())


url = 'https://www.nytimes.com/2017/01/13/world/asia/china-internet-addiction-electroshock-therapy.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=second-column-region&region=top-news&WT.nav=top-news'
crawl(url)
