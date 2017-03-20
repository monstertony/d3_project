__author__ = 'xyang'
import json
import csv
c={}
with open('//Users/xyang/Downloads/director_1.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[3] not in c.keys():
            c[row[3]]=1
        else:
            a=c[row[3]]
            c[row[3]]=a+1
print c
def readJson():
    # Reading data back
    with open('//Users/xyang/Downloads//director_world/mockelasticdata.json', 'r') as f:
         config= json.load(f)
    return config

def writeJson(data):
    # Reading data back
    with open('//Users/xyang/Downloads//director_world/mockelasticdata_1.json', 'w') as f:
         config= json.dump(data, f)
    return config

p=readJson()
# p1=p['aggregations']
# p2=p1['world_map']
# p3=p2['buckets']
# p3=p.get('aggregations').get('world_map').get('buckets')
for each in p.get('aggregations').get('world_map').get('buckets'):
    a=each.get('doc_count')
    b=each.get('key')
    if b in c.keys():
        each['doc_count']=c[each.get('key')]
    else:
        each['doc_count']=0
    print each
print p
writeJson(p)