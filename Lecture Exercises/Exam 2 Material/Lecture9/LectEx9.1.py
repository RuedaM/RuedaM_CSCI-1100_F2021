#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:44:31 2021

@author: maxrueda

Rueda, Maximillian
9/28/21
CSCI 1100
Lect. Exercises 9.1
"""

"""
1. Write a program that asks the user for a single integer n and prints the
    non-negative multiples of 3 that are less than n. Here is an example run
    of the program on Submitty:
Enter a positive integer: 12
0
3
6
9
"""

Integer = input("Enter a positive integer: ")
print(Integer)
Integer = int(Integer)

counter = 0
while counter < Integer:
    print(counter)
    counter += 3