from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


# Retrieves a list of all Internal links found on a page
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []

    # Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        print ("Looking into: ", link)
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# Retrieves a list of all external links found on a page
def getExternalLinks(bsObj, excludeUrl):
    print ("Find external links among internals, exclude:", excludeUrl)
    externalLinks = []
    # Finds all links that start with "http" or "www" that do not contain the current URL
    for link in bsObj.findAll("a",
                              href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])

    for row in externalLinks:
        print(row)

    if len(externalLinks) == 0:
        print ("Didn't find external")
        internalLinks = getInternalLinks(bsObj, startingPage)
        return getExternalLinks(bsObj, internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        print("found")
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


# Pass the starting site
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: " + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("https://en.wikipedia.org/wiki/Main_Page")
