#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:56:25 2021

@author: maxrueda

Rueda, Maximillian
10/21/21
CSCI 1100
Homework 5.1 - Getting Started

This code uses the hw5_util file to provide grids of values and other
 attributes of said grids that are read and iterated through to provide
 information about the grid itself and certain points of the grid. This code
 also acquires a set of start locations associated with each grid and provides
 the locations of neighboring locations of each start location. The code will
 detect if the path provided is made up of consecutive steps; if it is, total
 upward and downward elevation changes (going to a higher or lower value
 respectively) are each totaled based on the change from number to number in
 the grid
"""

#Imports:
#h5_util, imported as util for abbreviation, contains functions needed for the
# assignment
import hw5_util as util


#User-Defined Functions:

#Printing Grid:
#Based on the number grid provied by the user, the corresponding grid is
# printed
# Every row in the grid and every column in the row is iterated through
def print_grid(gridIndex):
    print("Grid", gridIndex)
    
    for row in util.get_grid(gridIndex):
        for number in row:
            print("{:4d}".format(number), end="")
        print("")


#Getting Neighbors:
#Based on a given location and the total number of rows and columns, the
# neighbors of the location found within the bounds of the grid are put into a
# list which is returned
def get_nbrs(rowLoc, columnLoc, rowNum, columnNum):
    neighList = []
    
    if (rowLoc-1 >= 0):
        upNeigh = (rowLoc-1, columnLoc)
        neighList.append(upNeigh)
    if (columnLoc-1 >= 0):
        leftNeigh = (rowLoc, columnLoc-1)
        neighList.append(leftNeigh)
    if (columnLoc+1 <= columnNum-1):
        rightNeigh = (rowLoc, columnLoc+1)
        neighList.append(rightNeigh)
    if (rowLoc+1 <= rowNum-1):
        downNeigh = (rowLoc+1, columnLoc)
        neighList.append(downNeigh)

    return neighList


#Main Code:
if __name__ == "__main__":
    
    #Continually Asking for Input:
    #This loop will continue infinitely until the user inputs 0, at which point
    # the code will break from the loop and end the code
    #If am invalid input is enterd, the loop will restart
    while True:
        gridIndex = input("Enter a grid index less than or equal to 3 (0 to end): ").strip()
        print(gridIndex)
        gridIndex = int(gridIndex)
        if (gridIndex == 0):
            break
        if (gridIndex > 3) or (gridIndex < 0):
            continue
        
        #Grid Print Option:
        #If the user inputs the correct character, the print_grid() function
        # is called
        showGrid = input("Should the grid be printed (Y or N): ")
        print(showGrid)
        showGrid = showGrid.strip("\r")
        
        if (showGrid.lower() == "y"):
            print_grid(gridIndex)
        
        
        #Grid Rows+Columns
        #The number of rows and columns in the grid are given and stored in
        # usable variables
        rowNum = len(util.get_grid(gridIndex))
        columnNum = len(util.get_grid(gridIndex)[0])
        print("Grid has",rowNum,"rows and",columnNum,"columns")
        
        
        #Getting Neighbors:
        #For every start location associated with the grid, its neighbors are
        # found with the get_nbrs() function above and stored in a list
        # For proper formatting, each item in the list is added to a string
        #  which is then printed
        #This loop repeats for every starting location
        for startLoc in util.get_start_locations(gridIndex):
            rowLoc, columnLoc = startLoc
            neighList = get_nbrs(rowLoc, columnLoc, rowNum, columnNum)
            neighString = ""
            for neighbor in neighList:
                neighString = neighString + " {}".format(neighbor)
            print("Neighbors of {}:".format(startLoc) + neighString)
        
        
        #Verifying Path Validity:
        #For every step of a given path (that is associated with the grid),
        # the next step is found and compared to all the neighbors of the
        # first step
        # If the next step is confirmed to be a neighbor of the first step, 
        #  a step difference is calculated; step is considered upward if it is
        #  a positive change and downward if it is a negative change
        # After looping through every step and its neighbors, the downward and
        #  upward totals are given if there were no issues with the path
        # If there is an issue with the step (i.e. the next step is not a
        #  neighbor of the first), the out-of-range step will be given and the
        #  path will be considered invalid
        pathList = util.get_path(gridIndex)
        upwardList = []
        downwardList = []
        validBooleanFlag = True
        
        for step in range(len(pathList)-1):
            rowStep1, columnStep1 = pathList[step]
            rowStep2, columnStep2 = pathList[step+1]
            stepNeighList = get_nbrs(rowStep1, columnStep1, columnNum, rowNum)
            
            if (pathList[step+1] in stepNeighList):
                valueStep1 = util.get_grid(gridIndex)[rowStep1][columnStep1]
                valueStep2 = util.get_grid(gridIndex)[rowStep2][columnStep2]
                
                stepDifference = (valueStep2 - valueStep1)
                if (stepDifference < 0):
                    downwardList.append(stepDifference)
                elif (stepDifference > 0):
                    upwardList.append(stepDifference)

            else:
                print("Path: invalid step from {} to {}".format(pathList[step], pathList[step+1]))
                validBooleanFlag = False
                break
        
        if (validBooleanFlag):
            print("Valid path")
            print("Downward {}".format(abs(sum(downwardList))))
            print("Upward {}".format(sum(upwardList)))
        
        break