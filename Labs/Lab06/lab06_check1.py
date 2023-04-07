#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:02:05 2021

@author: maxrueda
"""

bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

print(len(bd))
print(len(bd[0]))
print(bd[0][0])
print(bd[8][8])

print("-"*25)
line = "| "
counter = 0
for row in bd:
    for column in row:
        line += ("{} ".format(column))
        counter += 1
        if (counter % 3 == 0):
            line += "| "
        if (counter % 9 == 0):
            print(line)
            line = "| "
        if (counter == 27):
            print("-"*25)
            counter = 0
print("")

"""DIFFERENT WAY"""
print("-"*25)
line = "| "
counter = 0
for coord1 in range(9):
    for coord2 in range(9):
        line += (bd[coord1][coord2] + " ")
        counter += 1
        if (counter % 3 == 0):
            line += "| "
        if (counter % 9 == 0):
            print(line)
            line = "| "
        if (counter == 27):
            print("-"*25)
            counter = 0