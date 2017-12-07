from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# set is used for unordered list to check uniqueness
pages = set()


# main function
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        paragraph = bsObj.find(id="mw-content-text").findAll("p")[0]
        print(paragraph.get_text())
        # print (paragraph.get_text().partition('.')[0] + '.')
        # print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")

    # find all links in this page with certain restrictions
    # for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        print(link.attrs["href"])
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # We have encountered a new page
                newPage = link.attrs['href']
                print("----------------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("/wiki/Kevin_Bacon")
