from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string


# function split all words separated by space first
# then base on the value n pass in the function, combine words
# (result[1:1 + 2]) means start from index 1, add two more words (result will be [index 1, index 2]
def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")

    cleanInput = []
    input = input.split(' ')
    for item in input:
        # any punctuation characters on either side of the word will be stripped
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def ngrams(input, n):
    input = cleanInput(input)
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i + n])
    return output


# open wiki page
# find all div that has id tag with certain values, pass it to ngrams function
html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()

ngrams = ngrams(content, 2)
print (ngrams)

print("2-grams count is: " + str(len(ngrams)))

# testing a shorter string
testing = "How are you doing man"
result = ngrams(testing, 3)
