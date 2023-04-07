#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:56:45 2021

@author: maxrueda
"""

def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1

print("add() function:")
print(add(5,3))
print("")

#----------------------------------------

def mult(m,n):
    if n == 0:
        return 0
    else:
        return add(mult(m,n-1),m)

print("mult() function:")
print(mult(8,3))
print(mult(3,8))
print(mult(5,4))
print("")

#----------------------------------------

def power(x,n):
    if n == 0:
        return 1
    else:
        return mult(power(x, n-1),x)

print("power() function:")
print(power(6,3))