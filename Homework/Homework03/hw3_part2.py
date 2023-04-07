#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:53:05 2021

@author: maxrueda

Rueda, Maximillian
10/7/21
CSCI 1100
Homework 3.2

This code runs a simple game simulation in which a user moves a Pokemon chracter
 around a 150x150 area looking for other Pokemon. starting in the middle at
 (75,75). The game is interactive, letting the user pick the amount of moves
 they can make, the name of their Pikachu, and the amount of times their Pikachu
 encounters Water- or Ground-type Pokemon. The game will run for the indicated
 amount of times,a dn the user will pick which Pokemon their Pikachu will encounter
"""

#User-Defined Functions:

#Moving:
#This function takes a tuple (pokemon's coordinates), the direction, and the amount of steps
# The tuple is split into two separate variables to be altered separately
# Based on direction, it will "move" a certain amount up, down, left, or right on the 150x150 space
# If direction is anything other than n, s, e, or w, the pokemon doesn't move and the same tuple is returned
#The pokemon can't go beyond the borders, so all values that are <0 and >150 snap back to 0 and 150 respectively
#row and column are put back into the tuple locationTuple which is returned
def move_pokemon(locationTuple, direction, steps):
    
    row = locationTuple[0]
    column = locationTuple[1]
    
    if (direction == "n"):
        row -= steps
    elif (direction == "s"):
        row += steps
    elif (direction == "e"):
        column += steps
    elif (direction == "w"):
        column -= steps
    else:
        return (locationTuple)
        
    if (row < 0):
        row = 0
    elif (row > 150):
        row = 150
    if (column < 0):
        column = 0
    elif (column > 150):
        column = 150
    
    locationTuple = (row, column)
    
    return (locationTuple)


#User Input:
#Immediately after getting user input, the strings are placed in new variables
#Turns and oftenEncounters are whole number integers and are converted to such
turns = input("How many turns? => ")
print(turns)
turns = int(turns)

name = input("What is the name of your pikachu? => ")
print(name)

oftenEncounters = input("How often do we see a Pokemon (turns)? => ")
print(oftenEncounters)
oftenEncounters = int(oftenEncounters)


#Variables:
#Two variables to dictate location, a counter variable, and an empty list are declared
# row and column start at the default (75,75) which represents the center of the 150x150 space
# currentTurn acts as a counter whrough which the below while-loop iterates
# record is a collection of the results of each encounter the pokemon goes through
row = 75
column = 75
currentTurn = 0
record = []


#Main Code:

#Preliminary Print Statement:
#This code will be printing statements that record a simple type of game simulation
# This print statement tells the user its starting location and status
print()
print("Starting simulation, turn {} {} at ({}, {})".format(currentTurn, name, row, column))

#Game While-Loop:
#This while-loop will reiterate the encapsulated code while turns is greater than 0
# As soon as the loop starts, currentTurn will increase by 1
# It then asks the user for a direction - to account for all letter cases, the string is made lowercase
# The pokemon will move 5 spaces in the given direction
# The four values, row, column, direction, and steps, are then put through the function move_pokemon()
# The returned tuple is stored into row and column again
#The code then reads if an encounter should occur
# If the remainder between currentTurn and oftenEncounters is equal to 0, then an encounter should occur
# If there is an encounter, the code will ask the user if the pokemon fought a water/ground type
# If the pokemon fights a water type, you win the encounter
# The pokemon will move forward by one space in the same direction
# If the pokemon fights a ground type, you lose the encounter
# The pokemon will move backward by 10 spaces in the opposite direction
# If another value besides (w)ater, (g)round is given, the pokemon did not actually have an encounter
#Regardless of the choice, the result (Win, Lose, or No Pokemon) is appended to record
#To retiterate properly, turns is decreased by one to signify another turn
while turns > 0:
    currentTurn += 1
    direction = input("What direction does {} walk? => ".format(name))
    print(direction)
    direction = direction.lower()
    
    steps = 5
    row, column = move_pokemon((row, column), direction, steps)
    
    if (currentTurn % oftenEncounters == 0):
        print("Turn {}, {} at ({}, {})".format(currentTurn, name, row, column))
        encounter = input("What type of pokemon do you meet (W)ater, (G)round? => ")
        print(encounter)
        if (encounter.lower() == "w"):
            steps = 1
            row, column = move_pokemon((row, column), direction, steps)
            print("{} wins and moves to ({}, {})".format(name, row, column))
            record.append("Win")
        
        elif (encounter.lower() == "g"):
            steps = -10
            row, column = move_pokemon((row, column), direction, steps)
            print("{} runs away to ({}, {})".format(name, row, column))
            record.append("Lose")
        
        else:
            record.append("No Pokemon")
    turns -= 1


#Printed Output:
#Similar to Game While-Loop, the user-inputted name and current coordinates are given
# Additionally, the user's record of encouters is given
print("{} ends up at ({}, {}), Record: {}".format(name, row, column, record))