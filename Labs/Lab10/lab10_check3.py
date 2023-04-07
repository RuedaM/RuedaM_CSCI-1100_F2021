#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 12:15:51 2021

@author: maxrueda
"""

import random as r
import time as t

def closest1(L):
    '''
    Returns the two closest numbers in a list

    >>> closest1([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (5.4, 4.3)
    >>> closest1([ 1, 5, 9000, 400, 379, 90, 23.999999, 9001 , 9000.1 ])
    (9000, 9000.1)
    >>> closest1([7000])
    (None, None)
    '''
    if (len(L) < 2):
        return (None,None)
    else:
        close1 = L[0]
        close2 = L[1]
        distance = abs(L[0]-L[1])
        for index1 in range(len(L)-1):
            for index2 in range(index1+1, len(L)):
                if (abs(L[index1] - L[index2]) < distance):
                    distance = abs(L[index1] - L[index2])
                    close1 = L[index1]
                    close2 = L[index2]
        return (round(close1, 3), round(close2, 3))


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
        return (round(close1, 3), round(close2, 3))


if __name__ == '__main__':
    L1 = [ 1, 5, 9000, 400, 379, 90, 23.999999, 9001 , 9000.1 ]
    
    Lists = []
    randList1 = []
    
    for i in range(100):
        randList1.append(r.uniform(0.0, 1000.0))
    Lists.append(randList1)
    
    randList2 = []
    for i in range(1000):
        randList2.append(r.uniform(0.0, 1000.0))
    Lists.append(randList2)
    
    randList3 = []
    for i in range(10000):
        randList3.append(r.uniform(0.0, 1000.0))
    Lists.append(randList3)
    
    for randList in Lists: 
        start1 = t.time()
        value1 = closest1(randList)
        end1 = t.time() - start1
        print("Result: {}\nTime taken: {:.7f}".format(value1, end1))
        start2 = t.time()
        value2 = closest2(randList)
        end2 = t.time() - start2
        print("Result: {}\nTime taken: {:.7f}".format(value2, end2))
        print("")
    