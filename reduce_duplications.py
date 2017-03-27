__author__ = 'xyang'
import csv
poster={}
links=[]
links_repeat=[]
film_name=[]
film_place={}
count=0
# doput = open('data/doput.txt', 'wb+')
csvfile = file('data/movie_metadata.csv', 'rb')
reader = csv.reader(csvfile)
for line in reader:
    if line[11] not in links_repeat:
        # doput.write(str(count))
        # doput.write(',')
        # count=count+1
        # # print count
        # join=[]
        links_repeat.append(line[11])
    else:
        print line[11]
        # for i in range(0,28):
        #     if i == 11:
        #         doput.write(line[i].replace('\xc2\xa0','').replace(',',' '))
        #     else:
        #         doput.write(line[i].replace(',',' '))
        #     if i<27:
        #         doput.write(',')
        # doput.write('\n')
csvfile.close()
