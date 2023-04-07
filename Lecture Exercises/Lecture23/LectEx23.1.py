#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 21:26:39 2021

@author: maxrueda
12/03/21
CSCI 1100
Lect. Exercises 23.1 - Recursive Add
"""

"""
1. The following code recursively calculates the maximum value in a list:
def recursive_max_impl( L, i ):
    '''
    The actual recursive function.
    '''
    if i == len(L)-1:
        return L[i]
    else:
        return max(L[i], recursive_max_impl(L,i+1) )

def recursive_max( L ):
    '''
    The driver for the recursive function.  This handles the special
    case of an empty list and otherwise makes the initial call to the
    recursive function.
    '''
    if len(L) == 0:
        return -99999    # By convention
    else:
        return recursive_max_impl( L, 0 )

if __name__ == "__main__":
    L1 = [ 5 ]
    print(recursive_max( L1 ))
    L2 = [ 24, 23.1, 12, 15, 1 ]
    print(recursive_max( L2))
    L2.append( 55 )
    print(recursive_max( L2 ))

    Using this as a guide, write a recursive function to add the values in a
     list. You should have to change very little code. Implement your code in
     the provided file prob1.py
"""

def recursive_add_impl( L, i ):
    if i == len(L)-1:
        return L[i]
    else:
        return (L[i] + recursive_add_impl(L,i+1))

def recursive_add(L):
    if len(L) == 0:
        return 0
    else:
        return recursive_add_impl(L, 0)

if __name__ == "__main__":
    L1 = [ 5 ]
    print(recursive_add(L1))
    L2 = [ 24, 23.1, 12, 15, 1 ]
    print(recursive_add(L2))
    print(recursive_add([ ]))
