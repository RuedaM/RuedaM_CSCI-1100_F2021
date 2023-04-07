#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:30:15 2021

@author: maxrueda
"""

import lab06_util as util


def print_board(bd):
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


def ok_to_add(bd, userRow, userColumn, userNumber):
    addVerify = False
    
    for coord1 in range(9):
        for coord2 in range(9):
            if coord1 == userRow:
                if not (str(userNumber) in bd[coord1]):
                    break
                else:
                    return addVerify
    columnList = []
    for coord1 in range(9):
        for coord2 in range(9):
            if coord2 == userColumn:
                columnList.append(bd[coord1][coord2])
    if (str(userNumber) in columnList):
        return addVerify
    
    boxList = []
    while not userRow % 3 == 0:
        userRow -= 1
    while not userColumn % 3 == 0:
        userColumn -= 1
    for coord1 in range(userRow, userRow+3):
        for coord2 in range(userColumn, userColumn+3):
            boxList.append(bd[coord1][coord2])
            if not (userNumber in boxList):
                addVerify = True
                return addVerify
    print("Adding to this box is ok")
    
    return addVerify


def verify_board(bd, userRow, userColumn, userNumber):
    boardVerify = False
    
    for coord1 in range(9):
        for coord2 in range(9):
            if (bd[coord1][coord2] == "."):
                return boardVerify
            else:
                if (ok_to_add(bd, userRow, userColumn, userNumber) == False):
                    print("This is not ok to add")
                    return boardVerify
                else:
                    boardVerify = True
                    return boardVerify
            
            


fileName = input('Give file name ("board"): ').strip()
print(fileName)
bd = util.read_sudoku(fileName+".txt")
print_board(bd)

while True:
    userRow = int(input("Enter row index: ").strip())
    print(userRow)
    userColumn = int(input("Enter column index: ").strip())
    print(userColumn)
    userNumber = int(input("Enter number: ").strip())
    print(userNumber)
    
    
    ok_to_add(bd, userRow, userColumn, userNumber)
    if (ok_to_add(bd, userRow, userColumn, userNumber) == True):
         bd[userRow][userColumn] = str(userNumber)
         print_board(bd)
    else:
        print("This number cannot be added")
    
    if (verify_board(bd, userRow, userColumn, userNumber) == True):
        break