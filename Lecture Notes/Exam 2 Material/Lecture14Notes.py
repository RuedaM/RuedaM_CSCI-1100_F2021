#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:31:10 2021

@author: maxrueda
"""

"---Lecture 14 - Problem Solving and Design, Part 1---"

"Overview"
#This is the first of our lectures dedicated primarily to problem solving and
# design rather than on particular programming constructs and techniques

#Design:
#   Choice of container/data structure; choice of algorithm.
#       (At the moment, we don’t know too many containers, but we will think
#        about different ways to use the one container - lists - we do know
#        about.)
#   Implementation
#   Testing
#   Debugging

#We will discuss these in the context of several variations on one problem:
#   Finding the mode in a sequence of values — the value (or values) occuring
#    most often.

#There is no direct connect to a chapter in the text.
#We will start with a completely blank slate so that the whole process unfolds
# from scratch. This includes looking for other code to adapt.
#Working through problems like this is a good way to review what we’ve learned
# thus far.


"Example Problem"
#Given a numeric (ints or floats) list of values, find all pairs of indices of
# elements whose difference is equal to a user-provided value k
L = [-1, 5, 19, 9, 6, 2]
k = int(input("Give difference value: "))

#SOLUTION APPROACH:
#   1. Determine the type of container object
#       a. List of tuples where the difference of all tuple pairs == k ==> L1
#   2. Implementation
#       a. Find absolute value of difference between all pairs
#       b. Match each difference with value k
#       c. When match is found, update L1 to contain that tuple pair
#       d. Continue looping until the loop L is read through completely
#   3. Write the code in Python - while doing so: test, debug, etc.


"Problem: Finding the Mode"
#Given a series of values, find the one that occurs most often:

#Variation 1: is there a limited, indexable range of values?
#   Examples that are consistent with this variation include test scores or
#    letters of the alphabet
#   Examples not consistent include counting words and counting amino acids
#Variation 2: do we want just the modes or do we want to know how many times
# each value occurs?
#Variation 3: do we want a histogram where values are grouped?
#   Example: ocean temperature measurements, pixel intensities, income values

#In each of these cases, a specific value, the number of occurrences of a
# specific temperature, such as 2.314C, is not really of interest. More
# important is the number of temperature values in certain ranges
"""
Here is a short example to show the calculation of a mode where there is and
 is not and "enumerable" mapping between values and indices (For the
 non-enumerable, assume the values are floats or sparsely distributed).
We can assume all scores are positive.
"""
scores = [(3,2), (2,1), (9,1), (8,7), (2,0), (0,4), (1,7), (29,6), (27, 29), (30, 29), (2, 29)]

"Approach 1"
#Create a list where each index is the number and the index's corresponding
# value is the amount of times that index is seen
#   [3, 2, 4]   <--Values
#   (0)(1)(2)   <--Indices
#The number 0 occurs 3 times, 1 occurs 2 times, 2 occurs 4 times, etc.
#We should create a list of thee size+1 (to account for indices starting at 0)
# that's equal to the highest number

"Approach 2"
#Create a new list with each of the values in the tuples, then .sort() the list 
#   [(3,2), (2,1), ...]  -->  [3, 2, 2, 1, ...]  -->  [ 0, 1, 2, 2, 2, 3, ...]
#Each group of like-numbers would be put into separate variables, and the count
# of that variable would be found and compared to the previous variable's count
# If the previous element's count is found to be less than the current count,
#  update a varaible to reflect keep track of the highest count
#When the higher count is found, add that number to a list - if a higher count
# is found, replace that old number with the new number with the hgiher count
# If two numbers share the same highest count, simply append that number to
#  the list


"Our Focus: A Sequence of Numbers"
#   Integers, such as test scores
#   Floats, such as temperature measurements


"Sequence of Discussion"
#Brainstorm ideas for the basic approach. We’ll come with at least two.
#   We will discuss an additional approach when we learn about dictionaries.
#Algorithm / implementation
#Testing
#   Generate test cases
#   Which test cases we generate will depend on the choice of algorithm.
#   We will combine them.
#Debugging
#   If we find a failed test case, we will need to find the error and fix it.
#   Use a combination of carefully reading the code, working with a debugger,
#    and generating print statements.
#Evaluation
#   We can analyze using theoretical tools we will learn about later or
#    through experimental timing


"Discussion of Variations"
#Frequency of occurrence:
#   What are the ten most frequently occurring values? What are the top ten
#   percent most frequent values?
#   Output the occurrences for each value.
#Clusters / histograms:
#   Test scores in each range of 10
#Quantiles: bottom 25% of scores, median, top 25%


"Approach 1:"
high = scores[0][0]
for score in scores:
    if score[0] > high:
        high = score[0]
    if score[1] > high:
        high = score[1]

L = (high + 1) * [0]
for score in scores:
    L[score[0]] += 1
    L[score[1]] += 1
print(L)

most = max(L)
if most == 1:
    print("No Mode")
else:
    for index in range(len(L)):
        if (L[index] == most):
            print("Mode is", index)


"Approach 2:"
L = []
for score in scores:
    L.append(score[0])
    L.append(score[1])
L.sort()
print(L)

curr = 0
prev = -1
index = 0
count = 0
modes = []
while index < len(L):
    if (L(index) != prev):
        if (count > curr):
            modes = [prev]
            curr = count
        elif (count == curr):
            modes.append(prev)
        prev = L[index]
        count = 1
    else:
        count += 1
    index += 1
print(modes)