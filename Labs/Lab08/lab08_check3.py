#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:27:21 2021

@author: maxrueda
"""

def get_words(desc):
    desc = desc.strip().lower()
    
    for char in desc:
        if (char == (".")) or (char == (",")) or (char == ("(")) or (char == (")")) or (char == ('"')) or (char == ("?")) or (char == ("!")):
            desc = desc.replace(char, " ")
    
    descList = desc.split()
    for index in range(len(descList)-1,-1,-1):
        if not (descList[index].isalpha()):
            descList.remove(descList[index])
    for index in range(len(descList)-1,-1,-1):
        if not len(descList[index]) >= 4:
            descList.remove(descList[index])
    
    descSet = set(descList)
    return descSet
    


fileName = input("Give file name: ").strip() + ".txt"
print(fileName)


file = open(fileName)
for line in file:
    lineList = line.strip().split("|")
    descSetSingle = get_words(lineList[-1])
    print("File", fileName, len(descSetSingle),"words")
    print(descSetSingle)
print("")
print("")
print("")


clubFile = open("allclubs.txt")
clubString = ""
for line in clubFile:
    clubString += line

clubList = clubString.strip().split("\n")
newClubList = []
for club in clubList:
    clubInfoList = club.strip().split("|")
    newClubList.append(clubInfoList)

descSetList = []
for club in newClubList:
    descSetList.append(get_words(club[-1]))

commonCountList = []
for index in range(len(descSetList)):
    if (descSetList[index] != descSetSingle):
        commonCountList.append((len(descSetList[index] & descSetSingle), newClubList[index][0]))

commonCountList.sort(reverse=True)
print("Top 5 most similar clubs to {}:".format(fileName))
for i in range(5):
    print(commonCountList[i][1])