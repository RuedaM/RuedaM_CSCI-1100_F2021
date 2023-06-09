#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:22:58 2021

@author: maxrueda
12/07/21
CSCI 1100
Lect. Exercises 24.4 - Comprehending Temperature
"""

"""
4. Modify the code in prob4.py to use a list comprehension statement to
convert a list of Fahrenheit temperatures to Celsius, while eliminating those
that are below freezing.
"""

f_list = [ 19.4, 45.8, 25.2, -16, 82.19, 63.6, 45.1 ]
c_list = [(x-32)*(5/9) for x in f_list if x>=32]
line = ''
for c in c_list:
    line += '{:.2f}'.format(c) + ' '
print(line.strip())