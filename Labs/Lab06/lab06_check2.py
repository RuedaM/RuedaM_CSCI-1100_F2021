#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:02:07 2021

@author: maxrueda
"""

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
    if not (str(userNumber) in columnList):
        pass
    else:
        return addVerify
    
    
    while not userRow % 3 == 0:
        userRow -= 1
    while not userColumn % 3 == 0:
        userColumn -= 1
    
    for coord1 in range(userRow, userRow+3):
        for coord2 in range(userColumn, userColumn+3):
            if not (bd[coord1][coord2] == userNumber):
                addVerify = True
                return addVerify
    
    
    return addVerify
            

bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

while True:
    print_board(bd)
    
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