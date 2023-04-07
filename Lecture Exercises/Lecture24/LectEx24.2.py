#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:22:56 2021

@author: maxrueda
12/07/21
CSCI 1100
Lect. Exercises 24.2 - Y Sort?
"""

"""
2. Modify the code in prob2.py to determine the minimum x value of all points
    that are in the first quadrant (x and y values both positive). This will
    require you to use map, filter and min. You can write this in a single
    line, but for clarity you are welcome to write it on two or three. Do not
    create a new list.
"""

points = [ (4,2), (1,-3), (-4, -6), (6,9), (3,8), (-5,2), (6,2) ]
min_x = min(map(lambda x:x[0] , filter(lambda x:x[0]>0 and x[1]>0 , points)))
print(min_x)