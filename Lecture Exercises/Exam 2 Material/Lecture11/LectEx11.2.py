#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:36:11 2021

@author: maxrueda
10/8/21
CSCI 1100
Lect. Exercises 11.2
"""

"""
2. Suppose three siblings, Dale, Erin and Sam, have heights hd, he and hs,
    respectively. Write a program that reads in integer values of their
    heights and outputs the ordering from tallest to shortest. (For simplicity
    of this exercises, you may assume that the three heights you will be given
    are all different.) Try writing your solution using nested if statements
    and trying writing it without nested if statements; either is acceptable
    on Submitty and trying both is good practice. Here is an example as the
    code would look on Submitty.

Enter Dale's height: 124
Enter Erin's height: 112
Enter Sam's height: 119
Dale
Sam
Erin
"""

heightD = input("Enter Dale's height: ")
print(heightD)
heightD = int(heightD)
heightE = input("Enter Erin's height: ")
print(heightE)
heightE = int(heightE)
heightS = input("Enter Sam's height: ")
print(heightS)
heightS = int(heightS)


if (heightD > heightE) and (heightD > heightS):
    print("Dale")
    if (heightE > heightS):
        print("Erin")
        print("Sam")
    else:
        print("Sam")
        print("Erin")

elif (heightE > heightD) and (heightE > heightS):
    print("Erin")
    if (heightD > heightS):
        print("Dale")
        print("Sam")
    else:
        print("Sam")
        print("Dale")

else:
    print("Sam")
    if (heightD > heightE):
        print("Dale")
        print("Erin")
    else:
        print("Erin")
        print("Dale")