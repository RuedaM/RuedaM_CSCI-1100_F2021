#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:21:50 2021

@author: maxrueda
12/07/21
CSCI 1100
Lect. Exercises 24.1 - Mapping an Absolute Value
"""

"""
1. Modify the code in prob1.py to generate a new list where all values are
    replaced by their absolute values. You must use map, but there is no need
    for a lambda function.
"""

values = [ -12, 0, 15, -16, -17.3, 8, 4, -5 ]
new_values =  list(map(abs , values))
print(new_values)