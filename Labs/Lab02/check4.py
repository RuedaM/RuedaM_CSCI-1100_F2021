#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:15:47 2021

@author: maxrueda
"""

hello = "Hello,"
first = input("Please enter your first name: ")
last = input("Please enter your last name: ")
last = (last + "!")

maxlength = max(len(hello), len(first), len(last))


print(("*" * maxlength) + ("*" * 6))
print("** " + hello + (" " * (maxlength - len(hello))) + " **")
print("** " + first + (" " * (maxlength - len(first))) + " **")
print("** " + last + (" " * (maxlength - len(last))) + " **")
print(("*" * maxlength) + ("*" * 6))