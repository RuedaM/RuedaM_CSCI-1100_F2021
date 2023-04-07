#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 13:30:53 2021

@author: maxrueda

Rueda, Maximillian
12/08/21
CSCI 1100
Homework 8.2 - 

This code runs the simulation 5 times and outputs a summary of the status after each turn

bears_and_berries_1.json
"""



import json
from BerryField import Berry_Field as bfClass
from Bear import Bear as bClass
from Tourist import Tourist as tClass



jsonFileInput = input("Enter the json file name for the simulation => ").strip()
print(jsonFileInput)
print("")

jsonDict = json.loads(open(jsonFileInput).read())



berryfieldObj = bfClass(jsonDict)

bearObjList = []
for bear in berryfieldObj.actBears:
    bearObjList.append(bClass(bear))

tourObjList = []
for tour in berryfieldObj.actTours:
    tourObjList.append(tClass(tour, bearObjList))



print("Starting Configuration")
print("Field has {} berries.".format(berryfieldObj.count()))
print(berryfieldObj)
print("")


print("Active Bears:")
for bearObj in bearObjList:
    print(bearObj)
print("")


print("Active Tourists:")
for tourObj in tourObjList:
    print(tourObj)
print("")


"""
bears_and_berries_1.json
"""
#will run with updates to all assets and summary of status after each turn
for turn in range(5):
    print("Turn: {}".format(turn+1))
    
    #Field Operations
    berryfieldObj.grow()
    berryfieldObj.spread()
    
    
    #Bear operations
    i = 0
    while (i < len(bearObjList)):
        berryfieldObj.move(bearObjList[i], tourObjList)
        berryfieldObj.actBears[i] = [bearObjList[i].rowLoc, bearObjList[i].colLoc, bearObjList[i].direction]
        
        for tourObj in tourObjList:
            tourObj.bearObjList[tourObj.bearObjList.index(bearObjList[i])] = bearObjList[i]
        
        if bearObjList[i].outside:
            print("Bear at ({},{}) moving {} - Left the Field".format(bearObjList[i].rowLoc, bearObjList[i].colLoc, bearObjList[i].direction))
            bearObjList.pop(i)
            berryfieldObj.actBears.pop(i)
        else:
            i += 1
    
    
    #Tourist Operations
    i = 0
    while (i < len(tourObjList)):
        tourObjList[i].leave(bearObjList)
        
        if tourObjList[i].gone:
            print("Tourist at ({},{}), {} turns without seeing a bear. - Left the Field".format(tourObjList[i].rowLoc, tourObjList[i].colLoc, tourObjList[i].turnCount))
            tourObjList.pop(i)
            berryfieldObj.actTours.pop(i)
        else:
            i += 1
    
    """
    bears_and_berries_1.json
    """
    #-------------------------------------------------------------------------
    #Updated Info printed after all operations completed above
    print("Field has {} berries.".format(berryfieldObj.count()))
    print(berryfieldObj)
    print("")


    print("Active Bears:")
    for bearObj in bearObjList:
        """print("Bear resting:", bearObj.resting())"""
        if (bearObj.resting()):
            print("Bear at ({},{}) moving {} - Asleep for {} more turns".format(bearObj.rowLoc, bearObj.colLoc, bearObj.direction, bearObj.restCount-1))
        else:
            print(bearObj)
    print("")


    print("Active Tourists:")
    for tourObj in tourObjList:
        print(tourObj)
    
    
    print("")
    if not (turn == 4):
        print("")


"""
bears_and_berries_1.json
"""