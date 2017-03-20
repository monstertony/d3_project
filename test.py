__author__ = 'xyang'
import csv
from bs4 import BeautifulSoup
import urllib
import re
import pycountry
import geograpy
# import pickle
import nltk
import jellyfish
from fuzzywuzzy import process


detail={}
director=[]
# choices=[]
# for country in pycountry.countries:
#     choices.append(country.name)
#     # try:
#     #     print country.official_name
#     #     choices.append(country.official_name)
#     # except:
#     #     print country.name
#     #     choices.append(country.name)
# print choices

print pycountry.countries.lookup('united kingdom')

csvfile = file('//Users/xyang/Downloads/movie_metadata.csv', 'rb')
reader = csv.reader(csvfile)
for line in reader:
    if line[1] not in director:
        director.append(line[1])
csvfile.close()

doput = open('//Users/xyang/Downloads/doput.txt', 'wb+')


for c in director:
    r = urllib.urlopen('https://en.wikipedia.org/wiki/' + c).read()
    soup = BeautifulSoup(r, "lxml")
    for tr in soup.findAll('tr'):
        trText = tr.text
        if re.search(r"Born\n", trText):
            testText=trText.encode('utf-8')
            pl=testText.replace('\n',',').split(',')
            country=pl[-2].lstrip(" ")
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
            detail.setdefault(c,trText)
            print testText
            print pl
            print pl[-4].lstrip(" ")+" "+pl[-3].lstrip(" ")+" "+pl[-2].lstrip(" ")