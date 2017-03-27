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
film_name=[]
film_place={}
count=0
csvfile = file('data/movie_metadata.csv', 'rb')
reader = csv.reader(csvfile)
for line in reader:
    if line[17] not in links:
        count=count+1
        # print count
        join=[]
        join.append(line[17])
        join.append(line[11].replace('\xc2\xa0',''))
        # print join
        links.append(join)
csvfile.close()

failure=0
count=0
for each in links[1:]:
    count=count+1
    print count
    if count%500==0:
        print 'sleep 25s'
        time.sleep(25)
    # print each[0]
    print each[1]
    # r = urllib.urlopen(each[0]).read()
    try:
        http = httplib2.Http()
        status, response = http.request(each[0])
        soup = BeautifulSoup(response, parseOnlyThese=SoupStrainer('img'))
    except:
        failure=failure+1
        with open('data/%s.json'%failure, 'w') as f:
            config = json.dump(poster, f)
    line=0
    for tr in soup:
        line=line+1
        if line==3:
            src_1=re.findall("src=\".*?\"",str(tr))
            src=src_1[0].replace("src=","").replace("\"","")
            print src
            poster[each[1]]=src
print poster
with open('data/poster.json', 'w') as f:
    config = json.dump(poster, f)
