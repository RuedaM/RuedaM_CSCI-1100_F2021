#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:18:42 2021

@author: maxrueda

Rueda, Maximillian
10/5/21
CSCI 1100
Lect. Exercises 10.5
"""

"""
5. Use the following list in the code:
    
    co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

   Write a function called is_increasing that returns True if the values in
    the list it is passed are in increasing order and False otherwise. Use a
    for loop and indexing to accomplish this. Test the function with the
    following main code:

print('co2_levels is increasing: {}'.format(is_increasing(co2_levels)))
test_L1 = [ 15, 12, 19, 27, 45 ]
print('test_L1 is increasing: {}'.format(is_increasing(test_L1)))
test_L2 = [ 'arc', 'circle', 'diameter', 'radius', 'volume', 'area' ]
print('test_L2 is increasing: {}'.format(is_increasing(test_L2)))
test_L3 = [ 11, 21, 19, 27, 28, 23, 31, 45 ]
print('test_L3 is increasing: {}'.format(is_increasing(test_L3)))

   These should be the only print() function calls in the code you submit.
"""

def is_increasing(ListOfItems):
    for item in range(len(ListOfItems)-1):
        if ListOfItems[item] > ListOfItems[item+1]:
            return False
    return True


co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
print('co2_levels is increasing: {}'.format(is_increasing(co2_levels)))

test_L1 = [ 15, 12, 19, 27, 45 ]
print('test_L1 is increasing: {}'.format(is_increasing(test_L1)))

test_L2 = [ 'arc', 'circle', 'diameter', 'radius', 'volume', 'area' ]
print('test_L2 is increasing: {}'.format(is_increasing(test_L2)))

test_L3 = [ 11, 21, 19, 27, 28, 23, 31, 45 ]
print('test_L3 is increasing: {}'.format(is_increasing(test_L3)))