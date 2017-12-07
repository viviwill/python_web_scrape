# pg63

import json
from urllib.request import urlopen


def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")

links = getLinks("/wiki/Python_(programming_language)")

while(len(links) > 0):
    for link in links:
        print("-------------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
    for historyIP in historyIPs:
        country = getCountry(historyIP)
        if country is not None:
            print(historyIP+" is from "+country)
    newLink = links[random.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newLink)



jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],' \
             '"arrayOfFruits":[{"fruit": "apple"}, {"fruit": "banana"}, {"fruit": "pear"}]}'

jsonObj = json.loads(jsonString)
print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1].get("number") + jsonObj.get("arrayOfNums")[2].get("number"))
print(jsonObj.get("arrayOfFruits")[2].get("fruit"))
