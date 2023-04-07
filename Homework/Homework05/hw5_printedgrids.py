#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:57:48 2021

@author: maxrueda
"""

import hw5_util as util

print("Grid 1")
for row in util.get_grid(1):
    for number in row:
        print("{:4d}".format(number), end="")
    print("")
print("")


print("Grid 2")
for row in util.get_grid(2):
    for number in row:
        print("{:4d}".format(number), end="")
    print("")
print("")


print("Grid 3")
for row in util.get_grid(3):
    for number in row:
        print("{:4d}".format(number), end="")
    print("")