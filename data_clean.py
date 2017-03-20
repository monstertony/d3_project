import csv
import json

with open('film_place.json') as json_data:
    d = json.load(json_data)

print d
count=0
for each in d.keys():
    count=count+1
    print count
    print each

