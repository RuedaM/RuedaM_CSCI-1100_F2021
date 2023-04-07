#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:18:41 2021

@author: maxrueda

Rueda, Maximillian
10/5/21
CSCI 1100
Lect. Exercises 10.4
"""

"""
4. Use the following list in the code:
    
    co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

   Suppose we discovered that the measurement of CO2 values was uniformly too
    low by a small fraction p. Write a function that increases each value in
    co2_levels by the fraction p. (In other words if x is the value before the
    increase then x*(1+p) is the value after.) For this problem you need to
    use a range, len() and indexing. Start by asking the user for the
    percentage. Output the first and last values of the revised list. Your
    program should end with the lines:

print('First: {:.2f}'.format(co2_levels[0]))
print('Last: {:.2f}'.format(co2_levels[-1]))

   Here is an example of running your program:

Enter the fraction: 0.03
First: 329.63
Last: 404.74
"""

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

p = float(input("Enter the fraction: "))
print(p)
    
for value in range(len(co2_levels)):
    co2_levels[value] = (co2_levels[value] * (1 + p))
    

print('First: {:.2f}'.format(co2_levels[0]))
print('Last: {:.2f}'.format(co2_levels[-1]))