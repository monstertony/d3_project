__author__ = 'xyang'
__author__ = 'xyang'
import csv
from bs4 import BeautifulSoup
import urllib
import re
import pycountry

detail = {}
actor = []

csvfile = file('//Users/xyang/Downloads/movie_metadata.csv', 'rb')
reader = csv.reader(csvfile)
for line in reader:
    if line[6]not in actor:
        actor.append(line[6])
    if line[10] not in actor:
        actor.append(line[10])
    if line[14] not in actor:
        actor.append(line[14])
csvfile.close()
print actor

doput = open('//Users/xyang/Downloads/actor.txt', 'wb+')
count=0
for c in actor:
    count=count+1
    print count
    r = urllib.urlopen('https://en.wikipedia.org/wiki/' + c).read()
    soup = BeautifulSoup(r, "lxml")
    for tr in soup.findAll('tr'):
        trText = tr.text
        if re.search(r"Born\n", trText):
            testText = trText.encode('utf-8')
            pl = testText.replace('\n', ',').split(',')
            country = pl[-2].lstrip(" ")
            doput.write(c)
            doput.write(',')
            doput.write(pl[-3].lstrip(" "))
            doput.write(',')
            doput.write(country)
            doput.write(',')
            try:
                doput.write(pycountry.countries.lookup(country).alpha_3)
            except:
                doput.write('NULL')
            doput.write('\n')
            detail.setdefault(c, trText)
            print testText
            print pl
            print pl[-4].lstrip(" ") + " " + pl[-3].lstrip(" ") + " " + pl[-2].lstrip(" ")
