#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:45:28 2021

@author: maxrueda

Rueda, Maximillian
9/28/21
CSCI 1100
Lect. Exercises 9.2
"""

"""
2. The following list represents the population of New York State (in hundreds
    of thousands of people) for the US Census in 1790, 1800, 1810, etc., all
    the way through 2010.
census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
            5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
            8236, 17558, 17990, 18976, 19378 ]
    
   Copy and paste this list into the start of a new program file. Then write
    code to find the average percentage change from one decade to the next,
    across all decades. For example, the change from 1790 to 1800 is
    (589 - 340) / 340 * 100 = 73.2% and the change from 1800 to 1810 is
    (959 - 589) / 589 * 100 = 62.8% so the average across just these two
    decades is 68.0%. The output of your program would then simply be:
Average = 68.0%

Your answer will be different because it is taken from all decades.
"""

census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
            5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
            8236, 17558, 17990, 18976, 19378 ]

counter = 0
SumOfPercentages = 0

while counter < len(census)-1:
    Percentage = (((census[counter+1]-census[counter]) / census[counter]) * 100)
    SumOfPercentages += Percentage
    counter += 1
    
Average = SumOfPercentages / (len(census) - 1)

print("Average = " + str(round(Average, 1)) + "%")