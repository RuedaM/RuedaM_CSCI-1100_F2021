#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 13:30:53 2021

@author: maxrueda

Rueda, Maximillian
12/08/21
CSCI 1100
Homework 8.3 - 

This code runs the siumulation to completion and will stop when certain conditions are met
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
bears_and_berries_2.json
"""

#Will run until conditions below are met
turnCounter = 0
while (len(berryfieldObj.actBears) > 0) or (len(berryfieldObj.resBears) > 0) and not (berryfieldObj.count() == 0):
    turnCounter += 1
    print("Turn: {}".format(turnCounter))
    """
    print("#------------------------------#")
    print(berryfieldObj.actBears)
    print(bearObjList)
    print("#------------------------------#")
    """
    
    
    #Field Operations
    berryfieldObj.grow()
    berryfieldObj.spread()
    
    
    
    #Bear operations
    i = 0
    while (i < len(berryfieldObj.actBears)):
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
    while (i < len(berryfieldObj.actTours)):
        tourObjList[i].leave(bearObjList)
        
        if tourObjList[i].gone:
            print("Tourist at ({},{}), {} turns without seeing a bear. - Left the Field".format(tourObjList[i].rowLoc, tourObjList[i].colLoc, tourObjList[i].turnCount))
            tourObjList.pop(i)
            berryfieldObj.actTours.pop(i)
        else:
            i += 1
    
    
    
    #checks certain conditions to add assests from reserve lists into active lists
    #all places where the objects/information is stored are updated
    #Reserve Assets Operations
    if ((len(berryfieldObj.resBears) > 0) and (berryfieldObj.count() >= 500)):
        berryfieldObj.add_bear()
        newBearObj = bClass(berryfieldObj.actBears[-1])
        print("Bear at ({},{}) moving {} - Entered the Field".format(newBearObj.rowLoc, newBearObj.colLoc, newBearObj.direction))
        bearObjList.append(newBearObj)
        for tourObj in tourObjList:
            tourObj.bearObjList.append(newBearObj)
    
    tempList = []
    for bearObj in bearObjList:
        if bearObj not in tempList:
            tempList.append(bearObj)
    bearObjList = tempList
        
    
    
    if ((len(berryfieldObj.resTours) > 0) and (len(berryfieldObj.actBears) > 0)):
        berryfieldObj.add_tourist()
        newTourObj = tClass(berryfieldObj.actTours[-1], bearObjList)
        print("Tourist at ({},{}), {} turns without seeing a bear. - Entered the Field".format(newTourObj.rowLoc, newTourObj.colLoc, newTourObj.turnCount))
        tourObjList.append(newTourObj)
    
    
    print("")
    
    """
    bears_and_berries_1.json
    """
    #-------------------------------------------------------------------------
    #Updated Info printed only every 5 turns and after the simulation stops (big while-loop breaks)
    for bearObj in bearObjList:
        bearObj.resting()
    
    if (turnCounter % 5 == 0):
        print("Field has {} berries.".format(berryfieldObj.count()))
        print(berryfieldObj)
        print("")
    
    
        print("Active Bears:")
        for bearObj in bearObjList:
            if (bearObj.rest):
                print("Bear at ({},{}) moving {} - Asleep for {} more turns".format(bearObj.rowLoc, bearObj.colLoc, bearObj.direction, bearObj.restCount))
            else:
                print(bearObj)
        print("")
    
    
        print("Active Tourists:")
        for tourObj in tourObjList:
            print(tourObj)
            
        print("")
    
    
    
print("Field has {} berries.".format(berryfieldObj.count()))
print(berryfieldObj)
print("")


print("Active Bears:")
for bearObj in bearObjList:
    if (bearObj.rest):
        print("Bear at ({},{}) moving {} - Asleep for {} more turns".format(bearObj.rowLoc, bearObj.colLoc, bearObj.direction, bearObj.restCount-1))
    else:
        print(bearObj)
print("")


print("Active Tourists:")
for tourObj in tourObjList:
    print(tourObj)


"""
bears_and_berries_1.json
bears_and_berries_2.json
"""