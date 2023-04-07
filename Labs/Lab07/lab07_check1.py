#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:58:09 2021

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