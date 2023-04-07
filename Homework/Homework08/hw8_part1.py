#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 13:11:48 2021

@author: maxrueda

Rueda, Maximillian
12/08/21
CSCI 1100
Homework 8.1 - 

This code prints the initial state of the simulation without running it

bears_and_berries_1.json
"""


#importing json and all classes from files
import json
from BerryField import Berry_Field as bfClass
from Bear import Bear as bClass
from Tourist import Tourist as tClass

#pasing json file
jsonFileInput = input("Enter the json file name for the simulation => ").strip()
print(jsonFileInput)
print("")

jsonDict = json.loads(open(jsonFileInput).read())


#creation of berry field bject where most operations will go
berryfieldObj = bfClass(jsonDict)
print("Field has {} berries.".format(berryfieldObj.count()))
print(berryfieldObj)
print("")


#create separate bear objects, each with their own coords+direction
print("Active Bears:")
bearObjList = []
for bear in jsonDict["active_bears"]:
    bearObjList.append(bClass(bear))

for bearObj in bearObjList:
    print(bearObj)
print("")


#create separate tourists objects, each with their own coords+a copy of the list of all bear objects
print("Active Tourists:")
tourObjList = []
for tour in jsonDict["active_tourists"]:
    tourObjList.append(tClass(tour, bearObjList))

for tourObj in tourObjList:
    print(tourObj)