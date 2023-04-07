#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:30:43 2021

@author: maxrueda
"""

def parse_line(line):
    if (line.count("/") >= 3):
        lineList = line.split("/")
        
        var3 = lineList[-1]
        lineList.pop(-1)
        var2 = lineList[-1]
        lineList.pop(-1)
        var1 = lineList[-1]
        lineList.pop(-1)
        
        if (line.count("/") >= 4):
            string = "/".join(lineList)
        else:
            string = lineList[0]
        
        if (var1.isdigit()) and (var2.isdigit()) and (var3.isdigit()):
            return (int(var1), int(var2), int(var3), string)
    
    return

s = "    Again some spaces\n/12/12/12"
print(parse_line(s))



def get_line(fname, parno, lineno):
    text = open(fname, encoding="utf8")
    parCount = 1
    lineCount = 1
    booleanFlag = False
    
    for line in text:
        if (parCount == parno) and (lineCount == lineno):
            return line.rstrip()
        if (line == "\n") and not (booleanFlag):
            booleanFlag = True
            parCount += 1
            lineCount = 1
            continue
        elif (line != "\n"):
            booleanFlag = False
        elif (line == "\n") and (booleanFlag):
            lineCount = 1
            continue
        lineCount += 1
        

fileNum = input("Please enter the file number ==> ").strip()
print(fileNum)
fileName = fileNum+".txt"
parNum = int(input("Please enter the paragraph number ==> ").strip())
print(parNum)
lineNum = int(input("Please enter the line number ==> ").strip())
print(lineNum)
print(get_line(fileName, parNum, lineNum))