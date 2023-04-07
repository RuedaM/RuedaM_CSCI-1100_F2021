#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:13:48 2021

@author: maxrueda
"""

def get_words(desc):
    desc = desc.strip().lower()
    
    for char in desc:
        if (char == (".")) or (char == (",")) or (char == ("(")) or (char == (")")) or (char == ('"')):
            desc = desc.replace(char, " ")
    
    descList = desc.split()
    
    for index in range(len(descList)-1,-1,-1):
        if not (descList[index].isalpha()):
            descList.remove(descList[index])

        if not len(descList[index]) >= 4:
            descList.remove(descList[index])
    
    descSet = set(descList)
    return descSet
    


file1Name = input("Give 1st file name: ").strip() + ".txt"
print(file1Name)
file2Name = input("Give 2nd file name: ").strip() + ".txt"
print(file2Name)


file1 = open(file1Name)
for line in file1:
    lineList = line.strip().split("|")
    desc1Set = get_words(lineList[-1])
    print("File", file1Name, len(desc1Set),"words")
    print(desc1Set)
print("")

file2 = open(file2Name)
for line in file2:
    lineList = line.strip().split("|")
    desc2Set = get_words(lineList[-1])
    print("File", file2Name, len(desc2Set),"words")
    print(desc2Set)
print("")


print("Comparing clubs", file1Name, "and", file2Name)

sameSet = desc1Set & desc2Set
print("Same words:", sameSet)

unique1Set = desc1Set - sameSet
print("Unique to {}:".format(file1Name), unique1Set)
unique2Set = desc2Set - sameSet
print("Unique to {}:".format(file2Name), unique2Set)