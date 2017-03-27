from bs4 import BeautifulSoup
import urllib
import re


r = urllib.urlopen('http://www.funda.nl/koop/1183am/+2km/125000-1500000/').read()
soup = BeautifulSoup(r, "lxml")
for each in soup.findAll('search-result'):
    print each
    # print re.findall("src=\".*?\"",str(each))
# print soup