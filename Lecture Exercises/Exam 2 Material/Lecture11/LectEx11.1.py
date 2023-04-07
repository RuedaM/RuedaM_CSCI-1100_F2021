#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:36:10 2021

@author: maxrueda
10/8/21
CSCI 1100
Lect. Exercises 11.1
"""

"""
1. Suppose you have a tuple that stores the semester and year a course was
    taken, as in

when = ('Spring',2015)

   Write a function called earlier_semester() that takes two such tuples as
    arguments and returns True if the first tuple represents an earlier
    semester and False otherwise. The possible semesters are 'Spring' and
    'Fall'. (Just to be clear, Fall 2013 is later than Spring 2013.) Test it
    using the following main code (you can cut-and-paste from the browser),
    which should be your only print function calls.

# Insert your function def here...

w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w1,w3)))

False
False
True
False
True
False
"""


def earlier_semester(semester1, semester2):
    if (semester1[1] > semester2[1]):
        return False
    elif (semester1[1] == semester2[1]):
        if (semester1[0] == semester2[0]):
            return False
        elif (semester1[0] != semester2[0]):
            if (semester1[0] == "Fall") and (semester2[0] == "Spring"):
                return False
    return True


w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w1,w3)))