#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 13:30:53 2021

@author: maxrueda
"""

import json

class Berry_Field(object):
    
    #All dictionary information stored here
    def __init__(self, trueDict):
        self.grid = trueDict["berry_field"]
        self.actBears = trueDict["active_bears"]
        self.resBears = trueDict["reserve_bears"]
        self.actTours = trueDict["active_tourists"]
        self.resTours = trueDict["reserve_tourists"]
    
    
    #prints the grid
    def __str__(self):
        printedGrid = ""
        for rowIndex in range(len(self.grid)):
            line = []
            for columnIndex in range(len(self.grid[rowIndex])):
                line.append("{:4d}".format(self.grid[rowIndex][columnIndex]))
            
            for index in range(len(self.actBears)):
                if (self.actBears[index][0] == rowIndex):
                    line[self.actBears[index][1]] = "   B"
            
            for index in range(len(self.actTours)):
                if (self.actTours[index][0] == rowIndex):
                    if (line[self.actTours[index][1]] == "   B"):
                        line[self.actTours[index][1]] = "   X"
                    else:
                        line[self.actTours[index][1]] = "   T"
            
            printedGrid += "".join(line)+"\n"
        return printedGrid.rstrip()
    
    
    #counts all grid values and retuns sum
    def count(self):
        totalCount = 0
        for row in self.grid:
            lineSum = sum(row)
            totalCount += lineSum
        return totalCount
    
    
    #will increase values on grid after meeting certain conditions
    def grow(self):
        for rowIndex in range(len(self.grid)):
            for columnIndex in range(len(self.grid[rowIndex])):
                if (str(self.grid[rowIndex][columnIndex]).isdigit()) \
               and (self.grid[rowIndex][columnIndex] >= 1) \
               and (self.grid[rowIndex][columnIndex] < 10):
                    self.grid[rowIndex][columnIndex] += 1
    
    
    #based on the "neighbors" of each location, berries will spread and begin to grow
    def spread(self):
        for rowIndex in range(len(self.grid)):
            for columnIndex in range(len(self.grid[rowIndex])):
                if (self.grid[rowIndex][columnIndex] == 0):
                    if ((rowIndex-1 >= 0) and (self.grid[columnIndex] == 10)) \
                    or ((rowIndex+1 <= len(self.grid)-1) and (self.grid[rowIndex+1][columnIndex] == 10)) \
                    or ((columnIndex-1 >= 0) and (self.grid[rowIndex][columnIndex-1] == 10)) \
                    or ((columnIndex+1 <= len(self.grid[rowIndex])-1) and (self.grid[rowIndex][columnIndex+1] == 10)) \
                    or ((rowIndex-1 >= 0) and (columnIndex-1 >= 0) and (self.grid[rowIndex-1][columnIndex-1] == 10)) \
                    or ((rowIndex+1 <= len(self.grid)-1) and (columnIndex-1 >= 0) and (self.grid[rowIndex+1][columnIndex-1] == 10)) \
                    or ((rowIndex-1 >= 0) and (columnIndex+1 <= len(self.grid[rowIndex])-1) and (self.grid[rowIndex-1][columnIndex+1] == 10)) \
                    or ((rowIndex+1 <= len(self.grid)-1) and (columnIndex+1 <= len(self.grid[rowIndex])-1) and (self.grid[rowIndex+1][columnIndex-1] == 10)):
                        self.grid[rowIndex][columnIndex] += 1
    
    
    #Based on bear's direction, a step will be made
    def step(self, bearObj):
        if bearObj.direction == "N":
            bearObj.rowLoc -= 1
        elif bearObj.direction == "S":
            bearObj.rowLoc += 1
        elif bearObj.direction == "E":
            bearObj.colLoc += 1
        elif bearObj.direction == "W":
            bearObj.colLoc -= 1
        elif bearObj.direction == "NE":
            bearObj.rowLoc -= 1
            bearObj.colLoc += 1
        elif bearObj.direction == "SE":
            bearObj.rowLoc += 1
            bearObj.colLoc += 1
        elif bearObj.direction == "SW":
            bearObj.rowLoc += 1
            bearObj.colLoc -= 1
        elif bearObj.direction == "NW":
            bearObj.rowLoc -= 1
            bearObj.colLoc -= 1
    
    
    #DISREGARD
    def bear_check(self, bearObj):
        rowIndex = bearObj.rowLoc
        columnIndex = bearObj.colLoc
        if ((rowIndex-1 >= 0)) \
       and ((rowIndex+1 <= len(self.grid)-1)) \
       and ((columnIndex-1 >= 0)) \
       and ((columnIndex+1 <= len(self.grid[rowIndex])-1)) \
       and ((rowIndex-1 >= 0) and (columnIndex-1 >= 0)) \
       and ((rowIndex+1 <= len(self.grid)-1) and (columnIndex-1 >= 0)) \
       and ((rowIndex-1 >= 0) and (columnIndex+1 <= len(self.grid[rowIndex])-1)) \
       and ((rowIndex+1 <= len(self.grid)-1) and (columnIndex+1 <= len(self.grid[rowIndex])-1)):
            return True
        else:
            return False
    
    #LARGE MOVE FUNCTION
    #Steps broken down within
    def move(self, bearObj, tourObjList):
        if (bearObj.rest):
            #print("Bear ({},{}){} resting, {} turns left".format(bearObj.rowLoc, bearObj.colLoc, bearObj.direction, bearObj.restCount))
            return bearObj
        #else:
            #print("Bear ({},{}){} not resting, moves".format(bearObj.rowLoc, bearObj.colLoc, bearObj.direction))
        
        berriesEaten = 0
        while (berriesEaten < 30):
            
            #Checks if bear runs into tourist - tourist removed from act.tour. list, bear stops
            for tourObj in tourObjList:
                if ([bearObj.rowLoc, bearObj.colLoc] == [tourObj.rowLoc, tourObj.colLoc]):
                    tourObj.gone = True
                    bearObj.rest = True
                    #print("Bear ({},{}){} eats tourists, rests".format(bearObj.rowLoc, bearObj.colLoc, bearObj.direction))
                    return bearObj
                
            #Berries at bear location are eaten - berries eaten until bear eats 30 then bear stops eating
            """if (self.bear_check(bearObj)):"""
            if (berriesEaten + self.grid[bearObj.rowLoc][bearObj.colLoc]) >= 30:
                berriesEaten += self.grid[bearObj.rowLoc][bearObj.colLoc]
                self.grid[bearObj.rowLoc][bearObj.colLoc] = (berriesEaten-30)
                berriesEaten = 30
                #print("Bear ({},{}){} ate {}, stops".format(bearObj.rowLoc, bearObj.colLoc, bearObj.direction, berriesEaten))
                #print("Berries left at location:", self.grid[bearObj.rowLoc][bearObj.colLoc])
                return bearObj
            else:
                berriesEaten += self.grid[bearObj.rowLoc][bearObj.colLoc]
                self.grid[bearObj.rowLoc][bearObj.colLoc] = 0
                #print("Bear ({},{}){} ate {} and moves".format(bearObj.rowLoc, bearObj.colLoc, bearObj.direction, berriesEaten))
                self.step(bearObj)
                #print("Bear moved to ({},{})".format(bearObj.rowLoc, bearObj.colLoc))
        
                #Checks if bear is off-grid
                if (bearObj.rowLoc < 0) \
                or (bearObj.colLoc < 0) \
                or (bearObj.rowLoc > len(self.grid)-1) \
                or (bearObj.colLoc > len(self.grid[0])-1):
                    bearObj.outside = True
                    #print("Bear ({},{}){} has left the field".format(bearObj.rowLoc, bearObj.colLoc, bearObj.direction))
                    return bearObj

    
    #Alters slef-variables if a reserve asset needs to become active
    def add_bear(self):
        self.actBears.append(self.resBears[0])
        self.resBears.pop(0)
    
    
    
    def add_tourist(self):
        self.actTours.append(self.resTours[0])
        self.resTours.pop(0)
    
        
        

if __name__ == "__main__":
    bb1Dict = json.loads(open("bears_and_berries_1.json").read())
    
    Info = Berry_Field(bb1Dict)
    print(Info.count())
    print(Info)
    
    Info.grow()
    print("after growing")
    print(Info.count())
    print(Info)
    
    Info.spread()
    print("after spreading")
    print(Info.count())
    print(Info)
    
    Info.grow()
    print("after growing")
    print(Info.count())
    print(Info)
    
    Info.spread()
    print("after spreading")
    print(Info.count())
    print(Info)