#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 21:26:40 2021

@author: maxrueda
12/03/21
CSCI 1100
Lect. Exercises 23.3 - Iterative Fibonacci
"""

"""
3. Looking carefully at the Fibonacci definition shows that calculating
    Fibonacci number f(n−1) requires calculating Fibonacci number f(n−2),
    which is also required for calculating Fibonacci number f(n). This means
    there is redundant computation. This redundancy gets worse for numbers
    f(n−3), f(n−4), etc.

   Fortunately, the Fibonacci sequence is relatively easy to compute
    non-recursively. That is your problem here. The trick is to build up the
    solution using a for-loop that calculates f(2), then f(3), then f(4), etc.
    Implement your solution in prob3.py.

   Out of curiosity, you could run your solutions to the previous two problems
    on large values of n and time the difference.
"""

def fib(n):
    num1 = 1
    num2 = 1
    if n == 0:
        return 0
    else:
        for i in range(n-2):
            num1, num2 = num2, (num1+num2)
            n += 1
        return num2


if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
