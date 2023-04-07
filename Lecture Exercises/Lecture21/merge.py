#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:09:58 2021

@author: maxrueda
11/23/21
CSCI 1100
Lect. Exercises 21.2 - merge.py
"""

"""
2. The file merge.py contains an implementation of the merge function that is
    the heart of merge sort. We only consider merge here and not the full
    sort. Modify the merge function so that if the same value appears in both
    lists then only one copy of the value is in the final merged list. You may
    assume that each of the sublists contain no duplicates. Work within the
    context of the merge function itself, meaning that you should not use a
    set and you should not use an extra list. You need to only change a few
    lines of code.

   For example, if the two lists are:
L1 = [ 2, 7, 9, 12, 17, 18, 22, 25 ]
L2 = [ 1, 5, 6, 8, 13, 14, 15, 18, 19, 23, 25 ]

    then the result merge(L1,L2) should be the list:
[ 1, 2, 5, 6, 7, 8, 9, 12, 13, 14, 15, 17, 18, 19, 22, 23, 25 ]

   Do not change the name of the function and do not change the name of the
    file. On Submitty we will run code that importsmerge.py and calls the
    function merge passing two lists as arguments.
"""

def merge(L1,L2):
    '''
    Merge the contents of two lists, each of which is already sorted
    into a single sorted list.
    '''
    i1 = 0
    i2 = 0
    L = []

    '''
    Repeated choose the smallest remaining item from the lists until one
    list has no more items that have not been merged.
    '''
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            if L1[i1] not in L:
                L.append( L1[i1] )
            i1 += 1
            
        elif L1[i1] > L2[i2]:
            if L2[i2] not in L:
                L.append( L2[i2] )
            i2 += 1
        else:
            L.append( L1[i1] )
            i1 += 1
            i2 += 1
    L.extend(L1[i1:])   #  copy remaining items from L1, if any
    L.extend(L2[i2:])   #  copy remaining items from L2, if any
    return L

if __name__ == "__main__":
    L1 = [ 2, 7, 9, 12, 17, 18, 22, 25 ]
    L2 = [ 1, 5, 6, 8, 13, 14, 15, 18, 19, 23, 25 ]

    merged_L = merge(L1, L2)
    print(merged_L)