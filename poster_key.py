import json
import csv
with open('data/new_poster.json', 'r') as f:
    poster = json.load(f)


for each in poster.keys():
    print poster[each]

# csvfile = file('data/movie_without_duplication.csv', 'rb')
# reader = csv.reader(csvfile)
#
# new_poster={}
#
#
# for line in reader:
#     try:
#         if line[12] not in new_poster.keys():
#             new_poster[line[0]]=[]
#             new_poster[line[0]].append(line[12].encode('utf-8'))
#             new_poster[line[0]].append(poster[line[12]].encode('utf-8'))
#     except:
#         continue
# count=0
# for each in new_poster.keys():
#     count=count+1
#     print count
#     print new_poster[each]
#
# with open('data/new_poster.json', 'w') as f:
#     config = json.dump(new_poster, f)


