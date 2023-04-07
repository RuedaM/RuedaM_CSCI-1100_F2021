#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:22:57 2021

@author: maxrueda
12/07/21
CSCI 1100
Lect. Exercises 24.3 - Lambda Distance
"""

"""
3. Modify the code in prob3.py to sort the points in a list by their distance
    from the origin (i.e. by the magnitude of the points). This will require
    use of a lambda function.
"""

points = [ (4,2), (1,-3), (-4, -6), (4,9), (-7,8), (-5,2), (6,2) ]
s_points = sorted(points, key=lambda x:(x[0]**2 + x[1]**2)**0.5, reverse=True)
print(s_points)