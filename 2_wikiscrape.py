from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))


# return a list of links under KB page
# then randomly select a link from the return list, use getlink function to get all links in there
links = getLinks("/wiki/Kevin_Bacon")

# .attrs["href"] will strip the sub url
# print(links[2])
# print (links[2].attrs["href"])

while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
