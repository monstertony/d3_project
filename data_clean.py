import csv
import json

with open('data/film_place.json') as json_data:
    d = json.load(json_data)

country_short={}
for k in d.keys():
    for s in d[k]['short']:
        if len(s)==3:
            if s in country_short.keys():
                country_short[s]=country_short[s]+1
            else:
                country_short[s]=1
        print s
print country_short

def readJson():
    # Reading data back
    with open('data/mockelasticdata.json', 'r') as f:
         config= json.load(f)
    return config

def writeJson(data):
    # Reading data back
    with open('data/mockelasticdata.json', 'w') as f:
         config= json.dump(data, f)
    return config

p=readJson()

total=0
for cs in country_short.keys():
    total=total+country_short[cs]
    p.get('aggregations').get('world_map').get('buckets').append({'key':cs,'doc_count':country_short[cs]})

p.get('hits')['total']=total
# for each in p.get('aggregations').get('world_map').get('buckets'):
#     a=each.get('doc_count')
#     b=each.get('key')
#     each['doc_count']=country_short[b]

# for each in d.keys():
#     for s in d[each]['short']:
#         print len(s.encode('utf-8'))
#         if len(s.encode('utf-8'))==3:
#             if s in count.keys():
#                 count[s]=count[s]+1
#             else:
#                 count[s]=1
#     # print d[each]['short']

print p
writeJson(p)

