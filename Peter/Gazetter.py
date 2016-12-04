# -*- coding: utf-8 -*-
import csv


testFile = open("trainData.txt", 'r')
evalFile = open("trainLabels.txt", 'r')
output = "output.txt"

testList = [line.split("\t") for line in testFile.readlines()]

evalList = [line.strip() for line in evalFile.readlines()]

engList = [line.split(' ') for line in open("eng.list")]
locList = [line.split(' ') for line in open("loc.list")]
miscList = [line.split(' ') for line in open("misc.list")]
perList = [line.split(' ') for line in open("per.list")]
orgList = [line.split(' ') for line in open("org.list")]

tag = "NNP"

named = [["O"]*4 for _ in range(len(testList))]


x= -1
y=1
for row in testList:
    x+=1
    if(tag in row[2]):
        for list in locList:
            for l in list:
                if(row[0] in l):
                    named[x][0]  = "1"
        for list in miscList:
            for l in list:
                if(row[0] in l):
                    named[x][1]  = "1"
        for list in perList:
            for l in list:
                if(row[2] in l):
                    named[x][2]  = "1"
        for list in orgList:
            for l in list:
                if(row[0] in l):
                    named[x][3]  = "1"
                    
with open(output, "w") as lines:
    writer = csv.writer(lines, lineterminator='\n')
    writer.writerows(named)

print(named[7])

#correct=0
#for a, b in zip(named, evalList):
#    if(a==b):
#        correct+=1
#    
#    
#print("The percent correct is " )
#print(correct/len(named)*100)
        
