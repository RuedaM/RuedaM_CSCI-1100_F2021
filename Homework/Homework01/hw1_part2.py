#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:12:17 2021

@author: maxrueda

Rueda, Maximillian
9/13/21
CSCI 1100
Homework 1.2
"""



Minutes = input("Minutes ==> ")
print(Minutes)
Seconds = input("Seconds ==> ")
print(Seconds)
Miles = input("Miles ==> ")
print(Miles)
MileGoal = input("Target Miles ==> ")
print(MileGoal)
Minutes = int(Minutes)
Seconds = int(Seconds)
Miles = float(Miles)
MileGoal = float(MileGoal)
print()

TotalTimeSec = Seconds + (Minutes*60)

TotalSecsPerMile = TotalTimeSec / Miles


MinPerMile = TotalSecsPerMile // 60
SecLeftPerMile = TotalSecsPerMile % 60
print("Pace is",int(MinPerMile),"minutes and",int(SecLeftPerMile),"seconds per mile.")

MilesPerHr = (Miles / float(TotalTimeSec)) * 3600.0
print("Speed is {0:.2f} miles per hour.".format(MilesPerHr))

MilesPerSec = (MilesPerHr / 60) / 60

GoalTimeMin = (MileGoal / MilesPerHr) * 60
GoalTimeSec = ((MileGoal / MilesPerHr) * 3600) % 60
print("Time to run the target distance of {0:.2f} miles is".format(MileGoal),str(int(GoalTimeMin)),"minutes and",str(int(GoalTimeSec)),"seconds.")