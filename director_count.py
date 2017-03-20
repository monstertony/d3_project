__author__ = 'xyang'
import csv
director={}
result=[]
count=0
with open('//Users/xyang/Downloads/director_1.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[3]=='USA':
            count=count+1
            print row[1]
            if row[1] not in director.keys():
                director[row[1]]=1
            else:
                a=director[row[1]]
                director[row[1]]=a+1

print count
with open('//Users/xyang/Downloads/us_map/us-state-capitals.csv', 'rb') as states:
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
# csvstcfile=file('//Users/xyang/Downloads/us_map/cities-lived.csv', 'ab')
# writers = csv.writer(csvstcfile,delimiter=',')
# for each in result:
#     writers.writerows(each)
# csvstcfile.close()

with open("//Users/xyang/Downloads/us_map/cities-lived_1.csv",'wb') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(result)
f.close()