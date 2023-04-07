#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:16:48 2021

@author: maxrueda
11/02/21
CSCI 1100
Lect. Exercises 16.1
"""

"""
2. Our solution to the IMDB problem thus far has not actually told us who is
    the busiest individual in the Internet movie database. Your job in this
    part is to complete this task. Starting from the code produced in class,
    which will be immediately posted on the course website (in the code
    written in class area), write a program that finds and prints the name of
    the individual who appears the most times in the IMDB file you are given.
    Also, count and output the number of individuals who appear only 1 time in
    the IMDB.

   For example if the answer were Thumb, Toni and this person had appeared 100
    times, and if 2,000 people had only appeared once, then your output should
    be:

Enter the name of the IMDB file ==> imdb_data.txt
Thumb, Toni appears most often: 100 times
2000 people appear once

   We strongly suggest that you test your solution on the hanks.txt dataset
    first! We will test on multiple files. You do not need to worry about the
    possibility of a tie for the most commonly occuring name. Please
    initialize your dictionary using dict() rather than {}
"""

fileName = input("Enter the name of the IMDB file ==> ").strip()
print(fileName)
namesDict = dict()
for line in open(fileName, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if (name in namesDict):
        namesDict[name] += 1
    else:
        namesDict[name] = 1

nameList = list(namesDict.keys())
appList = list(namesDict.values())

mostApps = max(appList)
mostAppsIndex = appList.index(mostApps)
mostName = nameList[mostAppsIndex]

onceCounter = 0
for value in appList:
    if value == 1:
        onceCounter += 1


print("{} appears most often: {} times".format(mostName, mostApps))
print("{} people appear once".format(onceCounter))