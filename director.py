__author__ = 'xyang'
import csv
from bs4 import BeautifulSoup
import urllib
import re
import pycountry
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAzH_ZabjZ3l0MOKIhniAM3sA9n81q8Pfw')

detail={}
director=[]

csvfile = file('//Users/xyang/Downloads/movie_metadata.csv', 'rb')
reader = csv.reader(csvfile)
for line in reader:
    if line[1] not in director:
        director.append(line[1])
csvfile.close()

doput = open('//Users/xyang/Downloads/director.txt', 'wb+')

count=0
for c in director:
    count=count+1
    print c
    cc=c+' (director)'
    print count
    r = urllib.urlopen('https://en.wikipedia.org/wiki/' + c).read()
    soup = BeautifulSoup(r, "lxml")
    flag=0
    for tr in soup.findAll('tr'):
        trText = tr.text
        if re.search(r"Born\n", trText):
            testText=trText.encode('utf-8')
            pl=testText.replace('\n',',').split(',')
            geocode_result = gmaps.geocode(pl[-3].lstrip(" ")+" "+pl[-2].lstrip(" "))
            try:
                short=geocode_result[0].get('address_components')[-1].get('short_name')
            except:
                short='NULL'
            if short!='NULL':
                try:
                    code=pycountry.countries.get(alpha_2=short).alpha_3
                except:
                    code='NULL'
            else:
                code='NULL'
            print short
            country=pl[-2].lstrip(" ")
            doput.write(c)
            doput.write(',')
            doput.write(pl[-3].lstrip(" "))
            doput.write(',')
            doput.write(pl[-2].lstrip(" "))
            doput.write(',')
            doput.write(code)
            doput.write('\n')
            detail.setdefault(c,trText)
            print testText
            print pl
            print geocode_result
            flag=1
    if flag==0:
        print cc
        rr = urllib.urlopen('https://en.wikipedia.org/wiki/' + cc).read()
        ssoup = BeautifulSoup(rr, "lxml")
        for tr in ssoup.findAll('tr'):
            print 'found'
            trText = tr.text
            if re.search(r"Born\n", trText):
                testText=trText.encode('utf-8')
                pl=testText.replace('\n',',').split(',')
                geocode_result = gmaps.geocode(pl[-3].lstrip(" ")+" "+pl[-2].lstrip(" "))
                try:
                    short=geocode_result[0].get('address_components')[-1].get('short_name')
                except:
                    short='NULL'
                if short!='NULL':
                    try:
                        code=pycountry.countries.get(alpha_2=short).alpha_3
                    except:
                        code='NULL'
                else:
                    code='NULL'
                print short
                country=pl[-2].lstrip(" ")
                doput.write(c)
                doput.write(',')
                doput.write(pl[-3].lstrip(" "))
                doput.write(',')
                doput.write(pl[-2].lstrip(" "))
                doput.write(',')
                doput.write(code)
                doput.write('\n')
                detail.setdefault(c,trText)
                print testText
                print pl
                print geocode_result
