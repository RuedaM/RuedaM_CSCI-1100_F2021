#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:53:06 2021

@author: maxrueda

Rueda, Maximillian
10/7/21
CSCI 1100
Homework 3.3

This code computes a population balance of bears, area of berry fields, and
 visiting tourists. Based on initial user input, this code will calculated the
 changes in each population over the span of ten years based on certain
 calculations. In addition to this, the program outputs the maximum and minimum
 values of each population over the 10-year span.
"""

#Imports:
#Because this code utilizes the log() function, math must be imported
import math


#User-Defined Functions:

#Computing Tourists:
#Used to compute amount of tourists in a given year based on number of bears
# Tourist count starts at 0
# If there are <4 or >15 bears, there is 0 tourists - otherwise, tourists are present
#For each bear up to and including 10, there are 10,000 more tourists present
# For every bear after this, 20,000 more tourists are present
# The total amount of tourists will be returned
def computing_tourists(bears):
    touristCount = 0
    if (bears >= 4) and (bears <= 15):
        for bearCount in range(bears):
            if (bearCount <= 9):
                touristCount += 10000
            else:
                touristCount += 20000
    return touristCount

#Find Next Values:
#Used to find number of bears and berries next year based on current number of bears, berries, and tourists
# No values can be negative; any that are willbe clipped to 0
# The next year's count of bears and berries is returned as one tuple
def find_next(bears, berries, tourists):
    bears_next = berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1)
    berries_next = (berries*1.5) - (bears+1)*(berries/14) - (math.log(1+tourists,10)*0.05)
    
    if (bears_next < 0):
        bears_next = 0
    if (berries_next < 0):
        berries_next = 0
    """
    WHY DOES THIS WORK TOO
    if (bears_next > 0):
        bears_next == 0
    if (berries_next > 0):
        berries_next == 0    
    """
    
    return bears_next, berries_next


#User Inputs:
#Immediately after getting user input, the strings are placed in new variables
# bears will be a whole number integer and berries will be a floating-point decimal
bears = input("Number of bears => ")
print(bears)
bears = int(bears)

berries = input("Size of berry area => ")
print(berries)
berries = float(berries)


#Varibles:
#A counter and three empty lists are declared
# yearCount will be used to iterate through the below while-loop a certain number of times
# The lists will be used to find the min/max of each population over 10 years
yearCount = 1
bearsList = []
berriesList = []
touristsList = []


#Main Code:

#Preliminary Print Statement:
#This code will be printing a table of values with 10 spaces across each column
# This print statement is like the titles of each of the below columns
print(("Year" + " "*6) + ("Bears" + " "*5) + ("Berry" + " "*5) + ("Tourists" + " "*2))

#While-Loop for 10 Years:
#This while loop will retiterate the encapsulated code while yearCount is less than 11
# First, the number of tourists is calculated based on the population of bears
# Then all four values, yearCount, bears, berries, and tourists, are printed
# They are printed in such a way to format the text like a table of values
# After this, the values of bears, berries, and tourists are appended to their corresponding lists
# The three variables are then put into the find_next() function to calculate next year's bear and berry counts
# These values, stored in a tuple, are returned to a tuple variable whose oth and 1st indices are stored in the existing bears and berries variables
# This way, they can be used when the while-loop reiterates again
# To retiterate properly, yearCount is increased by one to signify another year
while yearCount < 11:
    tourists = computing_tourists(bears)
    
    print(("{}".format(yearCount).ljust(10)) \
        + ("{}".format(bears).ljust(10)) \
        + ("{:.1f}".format(berries).ljust(10)) \
        + ("{}".format(tourists).ljust(10)) \
         )
    
    bearsList.append(bears)
    berriesList.append(berries)
    touristsList.append(tourists)
    
    nextTuple = find_next(bears, berries, tourists)
    bears = int(nextTuple[0])
    berries = nextTuple[1]
    
    yearCount += 1
print()

#Mins/Maxs from Lists:
#Lists that store bears, berries, and tourists populations will be used
# mins and maxs of each list will be stored in appropriate variables
# Semicolons used to separate lines of code
minBears = min(bearsList); maxBears = max(bearsList)
minBerries = min(berriesList); maxBerries = max(berriesList)
minTourists = min(touristsList); maxTourists = max(touristsList)


#Printed Output:
#Similar to While-Loop for 10 Years, min and max values are printed in such a way to format the text like a table of values
print("Min:      " + ('{}'.format(minBears).ljust(10)) \
                   + ("{:.1f}".format(minBerries).ljust(10)) \
                   + ("{}".format(minTourists).ljust(10)) \
     )

print("Max:      " + ("{}".format(maxBears).ljust(10)) \
                   + ("{:.1f}".format(maxBerries).ljust(10)) \
                   + ("{}".format(maxTourists).ljust(10)) \
     )

    
#EXTRA CODE - DO NOT GRADE
"""
print(("{}".format(yearCount) + (" "*(10-len(str(yearCount))))) \
    + ("{}".format(bears) + (" "*(10-len(str(bears))))) \
    + ("{:.1f}".format(berries) + (" "*(10-len(str(berries))))) \
    + ("{}".format(tourists)) \
     )

print("Min:      " + ("{}".format(minBears) + (" "*(10-len(str(minBears))))) \
                   + ("{:.1f}".format(minBerries) + (" "*(10-len(str(minBerries))))) \
                   + ("{}".format(minTourists)) \
     )
print("Max:      " + ("{}".format(maxBears) + (" "*(10-len(str(maxBears))))) \
                   + ("{:.1f}".format(maxBerries) + (" "*(10-len(str(maxBerries))))) \
                   + ("{}".format(maxTourists)) \
     )


print("Min: {} {:.1f} {}".format(minBears, minBerries, minTourists))
print("Max: {} {:.1f} {}".format(maxBears, maxBerries, maxTourists))


"""