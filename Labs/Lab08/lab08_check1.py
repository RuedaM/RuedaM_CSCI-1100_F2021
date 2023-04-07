#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 10:41:06 2021

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
    descSet = get_words(lineList[-1])
    print("File", fileName, len(descSet),"words")
    print(descSet)
    