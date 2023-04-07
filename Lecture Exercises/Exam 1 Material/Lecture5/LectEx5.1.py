#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:43:19 2021

@author: maxrueda

Rueda, Maximillian
9/15/21
CSCI 1100
Lect. Exercises 5.1
"""

"""
Write a function called convert2fahren that takes a Celsius temperature and
 converts it to Fahrenheit, returning the answer. Write code that calls the
 function three times to convert temperatures 0, 32, and 100 to Fahrenheit,
 printing the result each time. To keep things simple for these exercises, the
 output should be:
0 -> 32.0
32 -> 89.6
100 -> 212.0
 Submitty will check that a function exists with exactly the given name, that
 it does the calculation, and that it is called three times.
"""

def convert2fahren(fahrenheit):
    celsius = (fahrenheit * (9/5)) + 32
    return celsius

fahren1 = 0
fahren2 = 32
fahren3 = 100
print(fahren1, "->", convert2fahren(fahren1))
print(fahren2, "->", convert2fahren(fahren2))
print(fahren3, "->", convert2fahren(fahren3))