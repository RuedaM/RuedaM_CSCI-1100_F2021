#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:18:41 2021

@author: maxrueda

Rueda, Maximillian
10/5/21
CSCI 1100
Lect. Exercises 10.3
"""

"""
3. The solution to this problem and the two that follow should start with the
    assignment:

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

    Write a Python program that prints the number of values that are greater
    than the average of the list. For this you may use Python’s sum and len
    functions and you must use a for loop. Do NOT use a range, however, and do
    not use indexing.
   Your output should simply be:

Average: 351.14
Num above average: 5
"""

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

avg = (sum(co2_levels) / len(co2_levels))
print("Average: {0:.2f}".format(avg))

NumAboveAvg = 0
for value in co2_levels:
    if value > avg:
        NumAboveAvg += 1

print("Num above average:", NumAboveAvg)