#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:14:49 2021

@author: maxrueda
"""

def closest2(L):
    '''
    Returns the two closest numbers in a sorted list

    >>> closest2([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (4.3, 5.4)
    >>> closest2([ 1, 5, 9000, 400, 379, 90, 23.999999, 9001 , 9000.1 ])
    (9000, 9000.1)
    >>> closest2([7000])
    (None, None)

    '''
    if (len(L) < 2):
        return (None,None)
    else:
        newL = sorted(L)
        close1 = newL[0]
        close2 = newL[1]
        distance = abs(L[0]-L[1])
        for index in range(len(newL)-1):
            if (abs(newL[index] - newL[index+1]) < distance):
                distance = abs(newL[index] - newL[index+1])
                close1 = newL[index]
                close2 = newL[index+1]
        return (close1, close2)

if __name__ == "__main__":
    L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    print(closest2(L1))
    print(closest2([ 1, 5, 9000, 400, 379, 90, 23.999999, 9001 , 9000.1]))
    print(closest2([7000]))