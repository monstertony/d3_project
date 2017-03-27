import json
import csv

with open('data/film_place.json', 'r') as f:
    movie = json.load(f)

csvfile = file('data/movie_without_duplication.csv', 'rb')
reader = csv.reader(csvfile)
place = {}
for line in reader:
    # print line
    try:
        place[line[0]]={'country':[],'states':[]}
        place[line[0]]['country']=movie[line[12]]['short']
        place[line[0]]['states']=movie[line[12]]['states']
        print line[0]
        print movie[line[12]]['short']
        print movie[line[12]]['states']
    except:
        continue


# for each in movie.keys():
#     print each
    # place['key']=each
    # place['country']=movie[each]['short']
    # place['states']=movie[each]['states']
    # for s in movie[each]['short']:
    #     if len(s) == 3:
    #         if s in place.keys():
    #             place[s].append(movie[each].get('key'))
    #         else:
    #             place[s] = []
    #             place[s].append(movie[each].get('key'))
    # for states in movie[each]['states']:
    #     if states in place.keys():
    #         place[states].append(movie[each].get('key'))
    #     else:
    #         place[states] = []
    #         place[states].append(movie[each].get('key'))
#
for p in place.keys():
    print place[p]
#
with open('data/place_key.json', 'w') as f:
    config = json.dump(place, f)
