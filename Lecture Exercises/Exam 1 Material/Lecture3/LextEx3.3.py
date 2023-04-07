#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 09:10:33 2021

@author: maxrueda

Rueda, Maximillian
9/8/21
CSCI 1100
Lect. Exercises 3.3
"""

"""
Write a program that assigns the value 4 to the variable x, the value 2 to the
variable y and then uses exactly three print function calls to generate the
output below (four lines, with the second line blank). The print calls must
use the variables x and y rather than the values 4 and 2. The trick is to
change the assignment of the sep and end parameters in the call to print. The
character 4 is the first character on the 1st, 3rd and 4th lines of output.

4 2

4,2
42
"""


x = 4
y = 2
print(x, y, end="\n\n")
print(x, y, sep=",")
print(x, y, sep="")