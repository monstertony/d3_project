__author__ = 'xyang'
import csv
from bs4 import BeautifulSoup
import urllib
import re
import time
import pycountry
import json
import googlemaps
import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

gmaps = googlemaps.Client(key='AIzaSyAzH_ZabjZ3l0MOKIhniAM3sA9n81q8Pfw')
# geocode_result=gmaps.geocode('Vatican City')
# print geocode_result[0].get('address_components')[-2].get('short_name')

poster={}
links=[]
links_repeat=[]
film_name=[]
film_place={}
count=0
csvfile = file('data/movie_metadata.csv', 'rb')
reader = csv.reader(csvfile)
for line in reader:
    if line[17] not in links_repeat:
        count=count+1
        # print count
        join=[]
        links_repeat.append(line[17])
        join.append(line[17])
        join.append(line[11].replace('\xc2\xa0',''))
        # print join
        links.append(join)
csvfile.close()

count=0
for each in links[1:]:
    count=count+1
    print count
    movie_id=re.findall("title/.*?/\?ref",str(each[0]))
    # print type(movie_id)
    # print str(movie_id)
    number=str(movie_id).replace("['title/tt","").replace("/?ref']","")
    # print type(number)
    print number
# print links
