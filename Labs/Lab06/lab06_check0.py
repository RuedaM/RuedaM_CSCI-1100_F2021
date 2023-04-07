#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:58:06 2021

@author: maxrueda
"""

line = ""
for number in range(9):
    line += "{} ".format(number)
print(line)
print("")
print("")


line = ""
counter = 0
for coord1 in range(9):
    for coord2 in range(9):
        line += ("{},{} ".format(coord1, coord2))
        counter += 1
        if (counter % 3 == 0):
            line += " "
        if (counter % 9 == 0):
            print(line)
            line = ""
        if (counter == 27):
            print("")
            counter = 0
print("")
print("")


line = ""
for coord1 in range(9):
    for coord2 in range(9):
        if coord1 == 2:
            line += ("{},{} ".format(coord1, coord2))
print(line)
print("")
print("")


line = ""
for coord1 in range(9):
    for coord2 in range(9):
        if coord2 == 5:
            line += ("{},{} ".format(coord1, coord2))
print(line)
print("")
print("")


line = ""
counter = 0
for coord1 in range(3):
    for coord2 in range(3):
        line += ("{},{} ".format(coord1, coord2))
        counter += 1
        if counter == 3:
            print(line)
            line = ""
            counter = 0