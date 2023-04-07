#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 21:26:40 2021

@author: maxrueda
12/03/21
CSCI 1100
Lect. Exercises 23.2 - Recursive Fibonacci
"""

"""
2. Implement a recursive solution to the Fibonacci number function definition
    given during lecture. Implement your code in the provided file prob2.py
"""

def fib(n):
    if (n < 1):
        return 0
    elif (n == 1) or (n == 2):
        return 1
    else:
        return (fib(n-1) + fib(n-2))


if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
