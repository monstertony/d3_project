__author__ = 'xyang'
import csv
import json
director={}
result=[]
count=0
with open('data/film_place.json') as json_data:
    d = json.load(json_data)

for each in d.keys():
    for states in d[each]['states']:
        print states
        if states in director.keys():
            director[states]=director[states]+1
        else:
            director[states]=0

with open('data/us-state-capitals.csv', 'rb') as states:
    s=csv.reader(states)
    for line in s:
        print line
        if line[1] in director.keys():
            data=[]
            data.append(director[line[1]])
            print director[line[1]]
            data.append(line[1])
            data.append(line[2])
            data.append(line[3])
            result.append(data)
print director['New York']
print result

with open("data/cities-lived_1.csv",'wb') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(result)