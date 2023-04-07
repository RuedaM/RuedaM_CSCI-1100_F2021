#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 19:47:09 2021

@author: maxrueda
"""

def line_parse(fileName):
    file = open(fileName)
    fileList = []
    
    for line in file:
        line.strip()
        newLine = ""
        for char in line:
            if (char.isalpha()) or (char == " "):
                newLine += char
        lineList = newLine.strip().lower().split(" ")
        fileList += lineList
    
    newFileList = []
    for word in fileList:
        if not (len(word) == 0):
            newFileList.append(word)
    
    file.close()
    
    return newFileList


def stop_removal(fileList):
    fileListNoStop = []
    for word in fileList:
        if not (word in stopSet):
            fileListNoStop.append(word)
    
    return fileListNoStop


file1Name = "ex1.txt"
file2Name = "ex2.txt"

file1List = line_parse(file1Name)
file2List = line_parse(file2Name)
print(file1List)
print(file2List)

StopList = line_parse("stop.txt")
stopSet = set(StopList)

file1List = stop_removal(file1List)
file2List = stop_removal(file2List)

print(file1List)
print(file2List)