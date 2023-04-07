#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 22:01:13 2021

@author: maxrueda

Rueda, Maximillian
9/2/21
CSCI 1100
Lect. Exercises 2.2
"""

"""
Write Python code that creates three variables called length, width and height
to store the dimensions of a 16.5 x 12.5 x 5 box. Write additional code that
calculates the volume of the box and calculates its surface area, storing each
in a variable. Print the values of these variables. Your code must use five
assignment statements and two print function calls. Submit a file containing
these seven lines of Python code. Your output should be:
volume = 1031.25
area = 702.5
"""

length = 16.5
width = 12.5
height = 5
volume = length * width * height
area = 2 * ((length * width) + (width * height) + (height * length))
print("volume =", volume)
print("area =", area)