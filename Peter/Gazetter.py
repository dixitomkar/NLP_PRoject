# -*- coding: utf-8 -*-

testFile = open("testData.txt", 'r')
evalFile = open("testLabels.txt", 'r')

testList = [line.split("\t") for line in testFile.readlines()]

evalList = [line.strip() for line in evalFile.readlines()]

engList = [line.split(' ') for line in open("eng.list")]

tag = "NNP"

named = ["O"] *len(testList)


x=-1
y=1
for row in testList:
    x+=1
    if(tag in row[2]):
        for list in engList:
            for l in list:
                if(row[0] in l):
                    named[x]  = "I-" +list[0]
#                    print(list[0])


correct=0
for a, b in zip(named, evalList):
    if(a==b):
        correct+=1
    
    
print("The percent correct is " )
print(correct/len(named)*100)
        
