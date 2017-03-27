import csv
from bs4 import BeautifulSoup
import urllib
import re

r = urllib.urlopen('https://en.wikipedia.org/wiki/List_of_geographic_centers_of_the_United_States').read()
soup = BeautifulSoup(r, "lxml")
for tr in soup.findAll('td'):
    print tr