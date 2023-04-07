#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:16:48 2021

@author: maxrueda
11/02/21
CSCI 1100
Lect. Exercises 16.1
"""

"""
1. Write a Python program that forms a dictionary called countries that
    associates the population with each of the following countries (in
    millions):
Algeria 37.1
Canada 3.49
Uganda 32.9
Morocco 32.7
Sudan 30.9
Canada 34.9 # a correction to the error above.
    and then prints the length of the countries dictionary, the sorted list of
    the keys in countries and a sorted list of the values in countries. There
    should be six assignment statements in your program (seven if you include
    initializing the dictionary) and three lines of output from your program.
    Please initialize your dictionary using dict() rather than {}
"""

countries = dict()
countries["Algeria"] = 37.1
countries["Canada"] = 3.49
countries["Uganda"] = 32.9
countries["Morocco"] = 32.7
countries["Sudan"] = 30.9
countries["Canada"] = 34.9

print(len(countries))
print(sorted(countries.keys()))
print(sorted(countries.values()))