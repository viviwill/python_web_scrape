from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

# my_url = "http://www.pythonscraping.com/pages/page1.html"
# my_url = "http://www.pythonscraping.com/pages/warandpeace.html"
my_url = "http://www.ebay.com/sch/i.html?_odkw=iPhone+6s+apple+care&Storage%2520Capacity=64GB%7C128GB%7C256GB&_udlo=400&Model=iPhone%25206s&_sop=10&_udhi=540&_mPrRngCbx=1&LH_BIN=1&_dcat=9355&_osacat=9355&_from=R40&_trksid=m570.l1313&_nkw=iPhone+6s+apple+care&_sacat=9355"

html = urlopen(my_url)
bsObj = BeautifulSoup(html, "html.parser")

# nameList = bsObj.findAll("span", {"class":"green"})
nameList = bsObj.findAll("h3", {"class": "lvtitle"})
# nameList = bsObj.findAll(text="the prince")

# print(len(nameList))

for name in nameList:
    print(name.get_text())

# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html, "html.parser")
# for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#     print(sibling)
