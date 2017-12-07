import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory + path
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path


downloadDirectory = "downloaded"
baseUrl = "http://www.nytimes.com/"

# Open the website and find everything has "src" in it
html = urlopen(baseUrl)
bsObj = BeautifulSoup(html, "html.parser")
downloadList = bsObj.findAll(src=True)

for row in downloadList:
    print(row)

# for download in downloadList:
#     # clean up the url (ie. www. http. etc...)
#     fileUrl = getAbsoluteURL(baseUrl, download["src"])
#     if fileUrl is not None:
#         print(fileUrl)
#
# urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
