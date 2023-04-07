#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 14:43:30 2021

@author: maxrueda
"""

"---Lecture 21 - Sorting---"

"Overview"
#Sorting is a fundamental operation
#Provides good practice in implementing and testing small functions
#Leads to a better understanding of algorithm efficiency
#Allows us to consider the fundamental notion of a merge of two sorted
# sequences.
#During testing, we will see an example of the important notion of passing
# functions as arguments.


"Algorithms to Study"
#Insertion sort
#Merge sort - This is our primary focus.
#Python’s built-in sort


"Experimental Analysis"
#The code lec21_test_sort.py in zip file lec21_files.zip posted in Course
# Materials on the Submitty site, and attached to the end of these notes, will
# be used to do timing experiments on all the sorts we write.

#Makes use of the random module
#Includes two main functions:
#   run_and_time
#   generate_local_perm
#We will discuss each of these in turn.

#The sorting functions themselves are functions in the module sorts
#Notice that the sorting function is passed as an argument to run_and_time:
#   First time that we have passed a function as an argument to another
#    function!
#We will start with experiments to analyze selection sort (see textbook) and
# insertion sort.


"Selection Sort"
#Idea:
#   Sorting an array by repeatedly finding the minimum element (considering
#    ascending order) from unsorted part and putting it at the beginning
#   Find the minimum value in the list, swap it with the value in the current
#    position, and repeat this process for the entire list until it is
#    completely sorted

#Algorithm:
#  qwerty

#Code:
def sel_sort(v):
    for i in range(0, len(v)-1):
        k = i
        for j in range(i+1, len(v)):
            if (v[j] < v[k]):
                k = j
        v[i], v[k] = v[k], v[i]


"Insertion Sort"
#Idea:
#   Based on the idea of updating a given list by analyzing each element and
#    inserting it at its correct position
#   If we already have a sorted list and we want to insert a new value, we can
#    shift values one location higher until we find the proper location for
#    the new value
#   Insert the new value
#   Start with a just a list of length 1 and repeat until all values have been
#    inserted

#Algorithm:
"""
for each index i in the list, starting at 1 do
    Save the value stored at location i in variable x
    Initialize j at location i-1
    while j is non-negative and the location to insert x has not been found do
        Shift the value at location j up to location j+1
        Decrement j
    Insert the value stored in x in location j+1
"""

#Code (in-class exercise):
def ins_sort(v):
    for i in range(1, len(v)):
        j = i-1
        x = v[i]
        while (j>=0) and (x < v[j]):
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x
    return v


"Steps to Testing"
#1. Re-read and mentally simulate
#2. Insert print statements and/or view with debugger to see what it is
#    actually doing.
#3. Run on “test cases” that capture challenging conditions:
#       Empty list
#       Singleton list
#       List of repeated values
#       List where the largest value is at the beginning or the smallest value
#        is at the end.


"Rough Analysis of Time Required"
#For any particular value of i in the outer for loop, there can be up to i-1
# comparisons/shifts.
#   When i==1 this is not much, but
#   When i==N-1, this is a lot.
#Adding across the different values of i, this results in at most (roughly)
# (N^2)/2 comparisons.

#We write this as O(N^2) because (informally) the number of comparisons done
# is proportional to N^2.


"Breaking the N-Squared Barrier"
#The fundamental problem with both selection sort (discussed in the textbook,
# but not in these notes) and insertion sort:
#   We need to do up to N comparisons by scanning through the list to find the
#    proper location of the next value in the sorted list.
#   For insertion sort, we could use binary search to find the insertion
#    location, but we would still have up to N shifts of values.

#Do better than selection sort and insertion sort by using algorithms that
# don’t scan the entire list to assign one value.
#Examples:
#   Quick sort
#   Heap sort
#   Merge sort
#We’ll study merge sort, in part because it is the easiest of these to
# understand and in part because of the importance of the idea of a merge.


"Merging Two Sorted Lists"
#Given two lists that are each already sorted, our problem is to generate a
#new sorted list containing all of the items from both lists.
#For example,
L1 = [ 9, 12, 17, 25 ]
L2 = [ 3, 5, 11, 13, 16 ]
#must be merged into a new list containing
[ 3, 5, 9, 11, 12, 13, 16, 17, 25 ]

#Idea:
#   Since both lists are sorted, the first item in the new list must be the
#    first item in one of the lists!
#   If we “remove” the smallest item (3 in L1 in this case), the next item
#    will again be the first non-copied item in one of the two lists!
#   We repeat this process until one of the lists has no more items to copy.
#   Then, copy the remainder of the other list to the back of our new list.

#We don’t actually remove the items from L1 or L2. Instead we keep an index to
# the next location of L1 and L2 that has not yet been copied.

#We’ll write the code in class, starting from here:
def merge(L1, L2):
    i1 = 0
    i2 = 0
    L = []
    while (i1 < len(L1)) and (i2 < len(L2)):
        if (L1[i1] < L2[i2]):
            L.append(L1[i1])
            i1 += 1
        else:
            L.append(L2[i2])
            i2 += 1
    L.extend(L1[i1:])
    L.extend(L2[i2:])
    return L

#Studying the solution:
#1. Write the values of the index variables, i1 and i2, each time through the
#    loop for lists L1 and L2 above.
#2. What are the values of i1 and i2 when the loop terminates?


"Merge Sort"
#Key observation: all lists of length 1 are sorted
#Therefore, for a list of length N that is to be sorted:
#   Create N lists of length 1 from the values in the list
#   Start to merge these “singleton” lists in pairs to create longer, sorted
#    lists.
#   Repeat on pairs of longer lists in succession
#Requires:
#   Keeping a list of sorted sublists, initialized with each singleton list
#   Rather than deleting the sorted sublists, just keep track of which we need
#    to work on.
#Code (in class):
def merge_sort(v):
    if len(v) <= 1:
        return
    lists = []
    for item in v:
        lists.append([item])
    i = 0
    while (i < len(lists)-1):
        new_list = merge(lists[i], lists[i+1])
        lists.append(new_list)
        i += 2
        """print(lists)"""
    v[::] = lists[-1]
    return v

m = [10, 3, 8, -5, 0, 1]
print("Final Result:", merge_sort(m))
print("")
print("")
print("")


"Analysis of Merge Sort"
#Check for correctness
#We’ll give an informal analysis explaining why there are only O(Nlog(⁡N))
# comparisons.
#Experimental timings
#Can you think of ways to improve our implementation of the merge sort idea?


"Final Comparison Across All Sorts"
#Selection sort and insertion sort are dramatically slower than merge sort,
# which in turn is dramatically slower than Python’s built-in sort, a highly
# optimized, C language implementation of merge sort.
#Shows:
#   the difference between O(N^2) sorting and O(NlogN) sorting
#   the difference between a straight-forward Python implementation and a
#    careful, optimized implementation of the same algorithm.
#Both of these are important!

if (__name__ == "__main__"):
    v = [10, 5, 3, 2, -4]
    ins_sort(v)
    print(v)
    v = []
    ins_sort(v)
    print(v)
    v = [5, 6, 7, 6, 5, 5]
    ins_sort(v)
    print(v)
    print("")
    
    v0 = [26, 35, 145]
    v1 = [0, 0, 9, 9, 9.4, 9.6, 15, 21]
    print(v0)
    print(v1)
    print(merge(v0, v1))
    print("")
    
    v = [9.1, 17.5, 9.8, 6.3, 12.4, 1.7]
    merge_sort(v)
    print(v)


#Final question: what happens when values are “almost” sorted?
#Experimentally, we can explore this using the generate_local_perm function in
# test_sort.py.
#Insertion sort becomes much faster, far outstripping selection sort. Why?


import lec21_sorts as sorts
import time
import random


def run_and_time(name, sort_fcn, v, known_v):
    '''
    Run the function passed as sort_fcn, timing its performance and
    double-checking if it correct.  The correctness check is probably
    not necessary.
    '''
    print("Testing " + name)
    t0 = time.time()
    sort_fcn(v)
    t1 = time.time()
    print("Time: {:.4f} seconds".format(t1-t0))
    # print("Is correct?", v==known_v
    print()



def generate_local_perm(v,max_shift):
    '''
    This function modifies a list so values are only a small amount
    out of order.  Each one  Generate a local permutation by randomly moving each
    value up to max_shift locations in the list.
    '''
    for i in range(len(v)):
        min_i = max(0,i-max_shift)
        max_i = min(len(v)-1, i+max_shift)
        new_i = random.randint( min_i, max_i )
        v[i], v[new_i] = v[new_i], v[i]


####################################################

if __name__ == '__main__':
    n = int(input("Enter the number of values ==> "))
    print("----------")
    print("Running on {:d} values".format(n))
    print("----------")

    v = list(range(n))
    v1 = v[:]
    random.shuffle(v1)
    # generate_local_perm(v1, 10)
    v2 = v1[:]
    v3 = v1[:]
    v4 = v1[:]

    run_and_time("merge sort", sorts.merge_sort, v3, v )   # passing functions as an arg to a fcn
    run_and_time("python sort", list.sort, v4, v )
    run_and_time("selection sort", sorts.sel_sort, v1, v )
    run_and_time("insertion sort", sorts.ins_sort, v2, v )
