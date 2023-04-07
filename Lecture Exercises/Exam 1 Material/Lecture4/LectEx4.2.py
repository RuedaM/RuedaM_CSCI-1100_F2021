#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:07:04 2021

@author: maxrueda

Rueda, Maximillian
9/12/21
CSCI 1100
Lect. Exercises 4.2
"""

"""
One of the challenges of programming is that there are often many ways to
solve even the simplest problem. Consider computing the area of the circle
with the standard formula 𝑎(𝑟)=𝜋𝑟2

Fortunately, we now have pi from the math module, but to compute the square of
the radius we now can use ** or pow() or we can just multiply the radius times
itself. To print the area accurate to only a few decimal places we can now use
the string format() method or the round() built-in function, which includes an
optional second argument to specify the number of decimal places.

Write a short Python program that computes and prints the areas of two
circles, one with radius 5 and the other with radius 32. Your code must use **
once and pow() once and it must use format() once and round() once. The output
should be exactly:

Area 1 = 78.54
Area 2 = 3216.99
"""


import math

Radius1 = 5
Radius2 = 32
Area1 = (math.pi * (Radius1 ** 2))
Area2 = (math.pi * pow(Radius2, 2))
print("Area 1 = {0:.2f}".format(Area1))
print("Area 2 = ", round(Area2,2))