#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 22:18:53 2021

@author: maxrueda

Rueda, Maximillian
9/21/21
CSCI 1100
Lect. Exercises 7.2
"""

"""
Write a function called add_tuples that takes three tuples, each with two
 values, and returns a single tuple with two values containing the sum of the
 values in the tuples. Test your function with the following calls:

print(add_tuples( (1,4), (8,3), (14,0) ))
print(add_tuples( (3,2), (11,1), (-2,6) ))

Note that these two lines of code should be at the bottom of your program.

This should output:
(23, 7)
(12, 9)
"""

def add_tuples(tuple1, tuple2, tuple3):
    tuplesum1 = tuple1[0] + tuple2[0] + tuple3[0]
    tuplesum2 = tuple1[1] + tuple2[1] + tuple3[1]
    tupletotal = (tuplesum1, tuplesum2)
    return tupletotal

print(add_tuples( (1,4), (8,3), (14,0) ))
print(add_tuples( (3,2), (11,1), (-2,6) ))