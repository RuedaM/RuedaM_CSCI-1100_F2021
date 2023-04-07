#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:43:20 2021

@author: maxrueda

Rueda, Maximillian
9/15/21
CSCI 1100
Lect. Exercises 5.2
"""

"""
Write a function called frame_string that takes a string as an argument. Its
 job is to print that string with a frame around it, just like in Lab 2.
 Unlike the other functions we have written frame_string does not need and
 therefore should not have a return statement. Write code to call the function
 two times. For the first call pass the string Spanish Inquisition. For the
 second call, pass the string Ni. Print a blank line between calls. The output
 should be:
*************************
** Spanish Inquisition **
*************************

********
** Ni **
********
 In addition to checking the output, we will check that you wrote a function
 called frame_string and that your code calls this function twice.
"""

def frame_string(string):
    count = len(string)
    print(("*" * count) + "******")
    print("** " + string + " **")
    print(("*" * count) + "******")
    
string1 = "Spanish Inquisition"
string2 = "Ni"
frame_string(string1)
print("")
frame_string(string2)