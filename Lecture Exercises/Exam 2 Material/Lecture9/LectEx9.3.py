#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:45:29 2021

@author: maxrueda

Rueda, Maximillian
9/28/21
CSCI 1100
Lect. Exercises 9.3
"""

"""
3. Write a program that inputs integer values that the user types until the
    user types a 0. Each value (other than 0) should be stored in a list. The
    program should then output the minimum, maximum and average of the values
    in the list. Your program must start by creating an empty list to store
    the values. Here’s an example of how it might look on Submitty:
Enter a value (0 to end): 5
Enter a value (0 to end): 3
Enter a value (0 to end): 11
Enter a value (0 to end): 0
Min: 3
Max: 11
Avg: 6.3
"""

total = 0
end_found = False
Integers = []

while not end_found:
    Value = input("Enter a value (0 to end): ")
    print(Value)
    Value = int(Value)
    if Value == 0:
        end_found = True
    else:
        Integers.append(Value)
print("Min:", min(Integers))
print("Max:", max(Integers))
print("Avg:", round((sum(Integers) / len(Integers)), 1))