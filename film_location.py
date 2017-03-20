__author__ = 'xyang'
import csv
from bs4 import BeautifulSoup
import urllib
import re
import time
import pycountry
import json
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAzH_ZabjZ3l0MOKIhniAM3sA9n81q8Pfw')
# geocode_result=gmaps.geocode('Vatican City')
# print geocode_result[0].get('address_components')[-2].get('short_name')

links=[]
film_name=[]
film_place={}
count=0
csvfile = file('//Users/xyang/Downloads/movie_metadata.csv', 'rb')
reader = csv.reader(csvfile)
for line in reader:
    if line[17] not in links:
        count=count+1
        print count
        join=[]
        join.append(line[17])
        join.append(line[11].replace('\xc2\xa0',''))
        # print join
        links.append(join)
csvfile.close()


count=0
for each in links[1:-1]:
    count=count+1
    print count
    if count%500==0:
        print 'sleep 25s'
        time.sleep(25)
    print each[0]
    film_place[each[1]]={'country':[],'states':[],'short':[]}
    r = urllib.urlopen(each[0].replace('?ref_=fn_tt_tt_1','locations?ref_=tt_dt_dt')).read()
    soup = BeautifulSoup(r, "lxml")
    for tr in soup.findAll('dt'):
        trText = tr.text.encode('utf-8')
        places=trText.replace('\n','').split(',')
        print places
        print places[-1].strip(' ')
        if places[-1].strip(' ')=='USA':
            if places[-1].strip(' ') not in film_place[each[1]]['country']:
                film_place[each[1]]['country'].append(places[-1].strip(' '))
                try:
                    c=pycountry.countries.lookup(places[-1].strip(' '))
                    film_place[each[1]]['short'].append(c.alpha_3)
                except:
                    film_place[each[1]]['short'].append(places[-1])
                try:
                    if places[-2].strip(' ') not in film_place[each[1]]['states']:
                        film_place[each[1]]['states'].append(places[-2].strip(' '))
                except:
                    continue
            else:
                try:
                    if places[-2].strip(' ') not in film_place[each[1]]['states']:
                        film_place[each[1]]['states'].append(places[-2].strip(' '))
                except:
                    continue
        else:
            if places[-1].strip(' ') not in film_place[each[1]]['country']:
                try:
                    c=pycountry.countries.lookup(places[-1].strip(' '))
                    film_place[each[1]]['short'].append(c.alpha_3)
                except:
                    if places[-1].strip(' ')=='UK':
                        c = pycountry.countries.lookup('United Kingdom')
                        film_place[each[1]]['short'].append(c.alpha_3)
                    else:
                        geocode_result = gmaps.geocode(trText.replace('\n',''))
                        print geocode_result
                        try:
                            short=geocode_result[0].get('address_components')[-2].get('short_name')
                            code=pycountry.countries.get(alpha_2=short).alpha_3
                        except:
                            try:
                                short = geocode_result[-2].get('address_components')[-2].get('short_name')
                                code = pycountry.countries.get(alpha_2=short).alpha_3
                            except:
                                try:
                                    short = geocode_result[0].get('address_components')[-1].get('short_name')
                                    code = pycountry.countries.get(alpha_2=short).alpha_3
                                except:
                                    code=places[-1].strip(' ')
                        film_place[each[1]]['short'].append(code)
                film_place[each[1]]['country'].append(places[-1].strip(' '))



with open('//Users/xyang/Downloads/film_place.json', 'wb+') as f:
    json.dump(film_place,f)
print film_place