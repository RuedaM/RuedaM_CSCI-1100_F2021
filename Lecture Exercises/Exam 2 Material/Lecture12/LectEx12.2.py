#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 13:03:32 2021

@author: maxrueda
10/15/21
CSCI 1100
Lect. Exercises 12.2
"""

"""
2. Write a function called first_day_greater that takes two lists, L1 and L2,
    representing the daily measured weights of rat 1 and rat 2, respectively,
    and returns the index of the first day for which the weight for the first
    rat is greater than the weight of the second rat. If there are no such
    days then the function should return -1. You may NOT assume that L1 and L2
    are the same length.

    Use the following to test your program:

if __name__ == "__main__":
    L1 = [ 15.1, 17.3, 12.3, 16.4 ]
    L2 = [ 15.0, 17.7, 12.5, 16.9 ]
    print("Test 1: {}".format( first_day_greater(L1,L2) ))
    L2 = [ 15.6, 17.9, 18.2, 16.5, 12.7 ]
    print("Test 2: {}".format( first_day_greater(L1,L2) ))
    L2 = [ 15.9, 18.8, 11.4 ]
    print("Test 3: {}".format( first_day_greater(L1,L2) ))
"""

def first_day_greater(list1, list2):
    for i in range(len(min(list1, list2))):
        if list1[i] > list2[i]:
            return i
    return -1



if __name__ == "__main__":
    L1 = [ 15.1, 17.3, 12.3, 16.4 ]
    L2 = [ 15.0, 17.7, 12.5, 16.9 ]
    print("Test 1: {}".format( first_day_greater(L1,L2) ))
    L2 = [ 15.6, 17.9, 18.2, 16.5, 12.7 ]
    print("Test 2: {}".format( first_day_greater(L1,L2) ))
    L2 = [ 15.9, 18.8, 11.4 ]
    print("Test 3: {}".format( first_day_greater(L1,L2) ))