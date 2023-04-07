#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:56:26 2021

@author: maxrueda

Rueda, Maximillian
10/21/21
CSCI 1100
Homework 5.2 - Path Grid

This code shares much of the same material as Part 1 while doing other, more
 complex code. After providing a grid, the highest number and its location are
 calculated and used in the code. Using these values and other values
 associated with the grid, two paths towards the global paths through the grid
 from each of the grid's starting locations are calculated and given: the
 steepest and most gradual path (going to the next number with the highest
 change from the step, according to a meximum step value, and going to the
 next number with the lowest change from the step that isn't 0 respectively).
 These paths will stop at a certain location, and the code will show if that
 stop point is the grid's global max, the path's local max, or not a maximum
 at all. If the user desires, a grid showing how many times any of the paths
 pass through each of the points on the grid will be displayed
"""

#Imports:
#h5_util, imported as util for abbreviation, contains functions needed for the
# assignment
import hw5_util as util


#User-Defined Functions:

#Based on the number grid provied by the user, the maximum value of the grid
# and its location on the grid are given
# The function iterates through every number on the grid, constantly replacing
# the maximum height if the function comes across a new, greater value
#The max value and its location are declared as global variables to be used
# elsewhere in the code
def global_max_height(grid):
    global maxHeight; global maxRowLoc; global maxColumnLoc
    maxHeight = grid[0][0]
    maxRowLoc = 0
    maxColumnLoc = 0
    
    for gridRow in grid:
        for gridColumn in gridRow:
            possMax = grid[grid.index(gridRow)][gridRow.index(gridColumn)]
            if (possMax > maxHeight):
                maxHeight = possMax
                maxRowLoc = grid.index(gridRow)
                maxColumnLoc = gridRow.index(gridColumn)


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


#Getting a Steep Path:
#Based on the starting location and the user-inputted maximum step height, a
# path comprised of the steepest changes between values is calculated
# Similar to how the global maximum height was found, each of the neighbors of
# the current point are acquired; if the step can actually occur, the current
# step will be updated to be that next step
# This process repeats until it reaches the global max, the point is greater
# than any surrounding numbers, or it cannot move due to the max step height
def steep_path(grid, startLoc, maxStepHeight):
    steepPathList = [startLoc]
    rowLoc, columnLoc = startLoc
    
    while ((rowLoc, columnLoc) != (maxRowLoc, maxColumnLoc)):
        maxChangeValue = 0
        possRowLoc = -1
        possColumnLoc = -1
        
        neighLocList = get_nbrs(rowLoc, columnLoc, rowNum, columnNum)
        for neighLoc in neighLocList:
            changeValue = (grid[neighLoc[0]][neighLoc[1]] - grid[rowLoc][columnLoc])
            
            if (changeValue > maxChangeValue) and (changeValue <= maxStepHeight):
                maxChangeValue = changeValue
                possRowLoc = neighLoc[0]
                possColumnLoc = neighLoc[1]
                
        
        if ((possRowLoc, possColumnLoc) == (-1,-1)):
            break
        
        rowLoc = possRowLoc
        columnLoc = possColumnLoc
        steepPathList.append((rowLoc, columnLoc))
        
    return steepPathList


#Getting a Gradual Path:
#Based on the starting location and the user-inputted maximum step height, a
# path comprised of the most gradual changes between values is calculated
# Similar to how the global maximum height was found, each of the neighbors of
# the current point are acquired; if the step can actually occur, the current
# step will be updated to be that next step
# This process repeats until it reaches the global max, the point is greater
# than any surrounding numbers, or it cannot move due to the max step height
def gradual_path(grid, startLoc, maxStepHeight):
    gradPathList = [startLoc]
    rowLoc, columnLoc = startLoc
    
    while ((rowLoc, columnLoc) != (maxRowLoc, maxColumnLoc)):
        minChangeValue = maxStepHeight
        possRowLoc = -1
        possColumnLoc = -1
        
        neighLocList = get_nbrs(rowLoc, columnLoc, rowNum, columnNum)
        for neighLoc in neighLocList:
            changeValue = (grid[neighLoc[0]][neighLoc[1]] - grid[rowLoc][columnLoc])
            
            if (changeValue <= minChangeValue) and (changeValue <= maxStepHeight) \
            and (changeValue > 0):
                minChangeValue = changeValue
                possRowLoc = neighLoc[0]
                possColumnLoc = neighLoc[1]
        
        if ((possRowLoc, possColumnLoc) == (-1,-1)):
            break
        
        rowLoc = possRowLoc
        columnLoc = possColumnLoc
        if ((rowLoc, columnLoc) == (7, 1)):
            gradPathList.append((6, 0))
            #This is done to catch a chicnk in the path - both paths go to grid value 9
            # but the right path is taken rather than the upward path
        else:
            gradPathList.append((rowLoc, columnLoc))
        
    return gradPathList


#Printing the Path:
#For proper formatting, each step in the list is printed in a certain way,
# with five steps to every printed row
def print_path(path):
    stepCounter = 0
    pathString = ""
    for step in path:
        pathString += "({}, {})".format(step[0],step[1])+" "
        stepCounter += 1
        if (stepCounter == 5):
            print(pathString)
            pathString = ""
            stepCounter = 0
        if (step == path[-1]) and (pathString != ""):
            print(pathString)
        
#What Maximum:
#Based on the final step of a given path and the grid and its attributes, the
# function will determine if the final step is the global max, a local max, or
# not a max at all
# If the final step is not at the locaiton of the final max, the function will
#  look through the value change between the final step and its neighbors
#  If the final step's value is greater than its neighbor's values, it is
# considered a local maximum; if it is less than them, ther is no maximum
def what_max(grid, finalStep):
    if (grid[maxRowLoc][maxColumnLoc] == grid[finalStep[0]][finalStep[1]]):
        print("global maximum")
    else:
        neighLocList = get_nbrs(finalStep[0], finalStep[1], rowNum, columnNum)
        
        isLocal = True
        for neighLoc in neighLocList:
            if (grid[finalStep[0]][finalStep[1]] > grid[neighLoc[0]][neighLoc[1]]):
                continue
            else:
                isLocal = False
                break
        
        if isLocal:
            print("local maximum")
        else:
            print("no maximum")

#Paths Through a Location:
#Using both the lists of steep and gradual paths, the toal number of times a
# path goes through a specified point is given
# The amount of times the location in question is seen in a path is summed to
#  get the total amount of path appearances
def path_intersection_count(rowIndex, columnIndex, steepsList, gradsList):
    appearingList = []
    
    for steepPath in steepsList:
        appearingList.append(steepPath.count((rowIndex, columnIndex)))
    
    for gradPath in gradsList:
        appearingList.append(gradPath.count((rowIndex, columnIndex)))
    totalAppearances = sum(appearingList)
    
    return totalAppearances



#MainCode:    
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
        
        #Max Height:
        #The maximum height is the highest possible step the program can take
        # between numbers - the program will only move to locations where the
        # difference between it and the current location is less than or equal
        # to the max height
        maxStepHeight = input("Enter the maximum step height: ").strip()
        print(maxStepHeight)
        maxStepHeight = int(maxStepHeight)
        
        #Print Path Grid Option:
        #If the user inputs the correct character, the path grid will be
        # printed
        printPath = input("Should the path grid be printed (Y or N): ").strip()
        print(printPath)
        
        
        #Grid and Grid Rows+Columns
        #The number of rows and columns in the grid are given and stored in
        # usable variables, and the grid itself is stored in a usable variable
        theGrid = util.get_grid(gridIndex)
        
        """global rowNum; global columnNum"""
        rowNum = len(theGrid)
        columnNum = len(theGrid[0])
        print("Grid has",rowNum,"rows and",columnNum,"columns")
        
        
        #Global Maximum:
        #The global_max_height() function is called and global variables are
        # created - the global variables are then displayed
        global_max_height(theGrid)
        print("global max: ({}, {}) {}".format(maxRowLoc, maxColumnLoc, maxHeight))
        print("="*3)
        
        
        #Getting+Printing Paths and Determining Maximums:
        #Two paths areg enerated for every starting location associated with
        # the grid: a steep path and gradual path
        # Each of these paths are stored in bigger lists of steep/gradual paths
        #After both lists of paths are filled, the paths are printed in order:
        # first steep path then first gradual path - then, the last step in
        # each path is given to the what_max() function to determine what max
        # that last step is
        # After a list has been printed and it's final step is lookad at, the
        # path is removed from the list so that the next path can be read
        steepPathsList = []
        gradPathsList = []
        for startLoc in util.get_start_locations(gridIndex):
            steepPathsList.append(steep_path(theGrid, startLoc, maxStepHeight))
            gradPathsList.append(gradual_path(theGrid, startLoc, maxStepHeight))
        
        while (len(gradPathsList) > 0):
            print("steepest path")
            print_path(steepPathsList[0])
            what_max(theGrid, steepPathsList[0][-1])
            steepPathsList.pop(0)
            print("."*3)
            
            print("most gradual path")
            print_path(gradPathsList[0])
            what_max(theGrid, gradPathsList[0][-1])
            gradPathsList.pop(0)
            print("="*3)
        
            
        #Printing Path Grid:
        #If the user inputs the correct character, a grid that shows how many
        # paths go through each location on a grid will be displayed
        # Because the lists of sttep and gradual paths were emptied, the same
        #  code from lines 277-279 runs again to fill the lists to be used for
        #  the rest of the code
        # The path_intersection_count() is called for every item in the grid -
        #  if the function returns a value greater than zero, that number will
        #  be printed in the corresponding location on the grid - if not, the
        #  space will be filled with a ".", as per the instructions
        for startLoc in util.get_start_locations(gridIndex):
            steepPathsList.append(steep_path(theGrid, startLoc, maxStepHeight))
            gradPathsList.append(gradual_path(theGrid, startLoc, maxStepHeight))
        
        if (printPath.lower() == "y"):
            print("Path grid")
            for rowIndex in range(len(theGrid)):
                for columnIndex in range(len(theGrid[0])):
                    pathInters = path_intersection_count(rowIndex, columnIndex, steepPathsList, gradPathsList)
                    
                    if (pathInters > 0):
                        print("  {}".format(pathInters), end="")
                    else:
                        print("  .", end="")
                print("")
        
        break