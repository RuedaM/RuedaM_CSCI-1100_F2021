#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:21:47 2021

@author: maxrueda

Rueda, Maximillian
9/13/21
CSCI 1100
Homework 1.3
"""



FrameChar = input("Enter frame character ==> ")
print(FrameChar)
FC = FrameChar
Height = input("Height of box ==> ")
print(Height)
Width = input("Width of box ==> ")
print(Width)
Height = int(Height)
Width = int(Width)
print()


DimensionLine1 = " " * ((Width - (2 + (len(str(Width) + "x" + str(Height))))) // 2)
DimensionLine2 = (" " * ((Width - (2 + (len(str(Width) + "x" + str(Height))))) // 2)) + (" " * ((Width - (2 + (len(str(Width) + "x" + str(Height))))) % 2))


print("Box:")
print(FC * Width)
print(((FC + (" "*(Width-2)) + FC) + "\n") * ((Height-3) // 2), end="")
print(FC + DimensionLine1 + str(Width) + "x" + str(Height) + DimensionLine2 + FC)



print(((FC + (" "*(Width-2)) + FC) + "\n") * ((Height-3) // 2) + ((FC + (" "*(Width-2)) + FC) + "\n") * ((Height-3) % 2), end="")
print(FC * Width)


"""
print(((FC + (" "*(Width-2)) + FC) + "\n") * (Height-2),end="")
"""


