#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:51:12 2021

@author: maxrueda

Rueda, Maximillian
9/24/21
CSCI 1100
Lect. Exercises 8.2
"""

"""
2. Write a short Python program that starts with the list

values = [ 14, 10, 8, 19, 7, 13 ]
(The above statement list should be the first line of your program.)
Then add code that does the following steps:

    1. Reads an integer, prints it (as we have done for input when using
        Submitty), and appends it to the end of values.
    2. Reads another integer, prints it and inserts it at index location 2 of
        values.
    3. Prints the integer at index 3 of values and print the integer at
        index -1 of values, both on one line.
    4. Prints the difference between the maximum and minimum of the integers
        in values.
    5. Prints the average of the integers in values, accurate to one decimal
        place. This must use the functions sum() and len().
    6. Prints the median of the numbers in values. Since the list is even
        length (a fact that you are allowed to use, just for this exercise),
        this is the average of the two middle integers after values is sorted.

Here is an example of running our solution (as it would look on Submitty):

Enter a value: 15
Enter another value: 23
8 15
Difference: 16
Average: 13.6
Median: 13.5
"""


values = [ 14, 10, 8, 19, 7, 13 ]


Value1 = input("Enter a value: ")
print(Value1)
Value1 = int(Value1)
values.append(Value1)

Value2 = input("Enter another value: ")
print(Value2)
Value2 = int(Value2)
values.insert(2, Value2)

print(values[3], values[-1])

Difference = (max(values) - min(values))
print("Difference:", Difference)

Average = (sum(values) / len(values))
print("Average: {0:.1f}".format(Average))

values.sort()
Median = ((values[3] + values[4]) / 2)
print("Median:", Median)