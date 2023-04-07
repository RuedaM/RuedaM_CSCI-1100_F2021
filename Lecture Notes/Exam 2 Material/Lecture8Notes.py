#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:24:39 2021

@author: maxrueda
"""

"---Lecture 8 Notes - Lists (Part 1)---"

"Overview"
#So far we’ve looked at working with individual values and variables; this is
# cumbersome even for just two or three variables, so we need a way to
# aggregate multiple values and refer to them using a single variable.
#We have done a little bit of this with strings and tuples, but now we are
# going to get started for real.
#This lecture is largely based on Sections 8.1-8.3 of Practical Programming.


"Lists are Sequences of Values"
#Gather together values that have common meaning.
#As a first example, here are scores of 7 judges for the free skating part of
# a figure skating competition:
Scores = [ 59, 61, 63, 63, 68, 64, 58 ]

#As a second example, here are the names of the planets in the solar system
# (including Pluto, for now):
Planets = [ 'Mercury', 'Venus', 'Earth', 'Mras', 'Jupiter',
    'Saturn', 'Neptune', 'Uranus', 'Pluto' ]

#Notes on syntax:
#Begin with [ and end with ]
#Commas separate the individual values
#The spaces between values are optional and are used for clarity here.
#Any type of object may be stored in a list, and each list can mix different
# types - ints can be stored in a list with a float or even a string:
Everything = [420, "Hello.?", (4,5,6), 6.9]


"Why bother?"
#Gather common values together, providing them with a common name, especially
# when we don’t know how many values we will have.
#Apply an operation to the values as a group.
#Apply an operation to each value in the group.

#Examples of computations on lists:
#   Average and standard deviation
#   Which values are above and below the average
#   Correct mistakes
#   Remove values (Pluto)
#   Look at differences

#Watch for these themes throughout the next few lectures.


"Accessing Individual Values — Indexing"
#Notice that we made the mistake in typing 'Mras'. How do we fix this? We’ll
# start by looking at indexing.

#The following line
print(Planets[1])
# accesses + prints the string at what’s known as index 1 of the list planets
print("")

#Each item/value in the list is associated with a unique index - Indexing in
# Python (and most other programming languages) starts at 0.
#The notation is again to use [ and ] with an integer (non-negative) to
# indicate which list item.

#What is the last index in planets?
#We can find the length using len() and then figure out the answer:
print(len(Planets))
#This returns 9, but we know indices start at 0, so the last index is 8.
print(Planets[8])
#You could also find ththe last index by simply having list[-1] - if indices
# start at 0, then the last in the list by this logic should be -1
print(Planets[-1])
print("")
print("")

"A Memory Model for Lists"
#We’ll draw a memory model in class that illustrates the relationship among:
#   The name of the list
#   The indices
#   The values stored in the list

#Let's say I want to collect data for whale sightings over rthe span of a year

#One method could be to store the amount seen in a day into a variable that
# represents the day: Day1 = 5, Day2 = 7, Day3 = 3, ... , Day365 = 10.
#Creating a variable like Day1 creates a memory location in Python somewhere
# that we can call id1 that has a value of 5. This process would be repeated
# 365 times into id2, id3, etc., eating up much of Python's memory.

#Alternatively, we could store each of the amounts seen in a day into list
# values in a single list called Whales[] where each index is a day.
#Because Whales[] is one variable, only one memory location id1 with all of
# these values stored in them. There is no need to jump from one memory
# location to another like with the single-variable storage method


"Changing Values in the List"
#Once we know about indexing, changing a value in a list is easy:
Planets[3] = 'Mars'
#This makes item 3 of planets now refer to the string 'Mars'
#And we can check the output:
print(Planets)
# to make sure we got it right.

"Strings are similar in many ways."
s = 'abc'
print(s[0])
print(s[1])

#Big difference: you can change a part of a list; you cannot change part of a
# string! For example, s[1] = 'A' would result in:
#   TypeError: 'str' object doesnot support item assignment
print("")
print("")


"All Indices Are Not Allowed"
#If t is a list, then the items are stored at indices from 0 to len(t)-1.
#If you try to access indices at len(t) or beyond, you get a run-time error.
# We’ll take a look and see.
#If you access negative indices, interesting things happen:
print(Planets[-1])

#More specifically, for any list t, if i is an index from 0 to len(t)-1 then
# t[i] and t[i-len(t)] are the same spot in the list.

print("")
print("")


"Functions on Lists: Computing the Average"
#There are many functions (methods) on lists. We can learn all about them
# using the help command.

#This is just like we did for strings and for modules, e.g.
'''
import math
help(math)

help(str)
'''
#Interestingly, we can run help in two ways, one
'''help(list)'''
# gives us the list methods, and the second
'''help(Planets)'''
# tells us that planets is a list before giving us list methods.


#First, let’s see some basic functions on the list values.
#The basic functions max, sum and min may be applied to lists as well.
#This gives us a simple way to compute the average of our list of scores.

print("Average Scores = {:.2f}".format( sum(Scores) / len(Scores) ))
print("Max Score =", max(Scores))
print("Min Score =", min(Scores))

#Exploring, we will look at what happens when we apply sum, max and min to our
# list of planet names. Can you explain the result?
#       Using sum() would result in an error because strings are unsupported
#        variable types for sum()
#       Using max() would return the last term in lexicographic order
#       Using min() would return the first term in lexicographic order
print("")
print("")


"Functions that modify the input: Sorting a list"
#We can also sort the values in a list by sorting it. Let’s try the following:
Planets = [ 'Mercury', 'Venus', 'Earth', 'Mras', 'Jupiter', \
           'Saturn', 'Neptune', 'Uranus', 'Pluto' ]
print(Planets)
Planets.sort()
print(Planets)
print("")
#Note that we did not assign the value returned by sort to a new variable.
# This is the first function we have learned outside of our Image module that
# modifies the input, the variable data itself, but returns nothing.

#Try the following and see what happens:
Scores = [ 59, 61, 63, 63, 68, 64, 58 ]
print(Scores)
New_Scores = Scores.sort()
print(New_Scores)
print("")
#So, the function returns nothing! But, it does change the value of the input
# list.

#It does so because lists are containers, and functions can manipulate what is
# inside containers. Functions cannot do so for simple types like integer and
# float.

#If we want a new list that is sorted without changing the original list then
# we use the sorted() function:
Scores = [ 59, 61, 63, 63, 68, 64, 58 ]
new_scores = sorted(Scores)
print(New_Scores)
#And this is different from the variable Scores
print(Scores)
print("")
print("")


"More Functions: Appending Values, Inserting Values, Deleting"
#Now, we will see more functions that can change the value of a list without
# returning anything.
#Armed with this knowledge, we can figure out how to add and remove values
# from a list:
#   .append() - will add another value defined in the parenthesis to the end
#                of the list
#   .insert() - will add another value to the list at a specified point - the
#                first argument is the index at which the new value will be
#                inserted, the second is what you want to insert
#   .pop() - will remove  the last value of the list
#   .remove() - will remove a value from the list at the specified index
#                defined in the parenthesis

#These operations are fundamental to any “container” — an object type that
# stores other objects. Lists are our first example of a container


"Lists of Lists"
#Note that lists can contain ANY mixture of values, including other lists.

#For example, in
L = [ 'Alice', 3.75, ['MATH', 'CSCI', 'PSYC' ], 'PA' ]
#L[0] is the name Alice
#L[1] is the GPA 3.75
#L[2] is a list of courses ['MATH', 'CSCI', 'PSYC']
#L[2][0] is the 0th course, 'MATH'
#L[3] is a home state abbreviation PA

#We will write code to print the courses, to change the math course to a stats
# course, and to append a zipcode:
print(L[2])
L[2][0] = "STATS"
L.append(12180)
print(L)
print("")
print("")


"---SUMMARY---"
#Lists are sequences of values, allowing these values to be collected and
# processed together.
#Individual values can be accessed and changed through indexing.
#Functions and methods can be used to return important properties of lists
# like min(), max(), sum().
#Functions and methods can be also used to modify lists, but not return
# anything.



"---Lecture 8 Practice Problems 1---"

'''
1. What is the index of the first value in scores that is greater than 65?


Scores = [ 59, 61, 63, 63, 68, 64, 58 ]
68 > 65, so:
Scores[4] is the first value greater than 65
'''


'''
2. Write a line of Python code to print this value and to print the previous
    and next values of the list.
'''
print(Scores[4], Scores[3], Scores[5])
print("")


'''
3. What is the index of the middle value in a list that is odd length? For
    even length lists, what are the indices of the middle two values?


Index of the middle value of an odd-length list: List[ len(List) + 1 ]
Indices of the middle value of an even-length list: List[len(List)], List[len(List)+1]
'''


"---Lecture 8 Practice Problems 2---"

'''
1. Write three different ways of removing the last value — 'Pluto' — from the
    list of planets. Two of these will use the method .pop().


Planets = [ 'Mercury', 'Venus', 'Earth', 'Mras', 'Jupiter',
    'Saturn', 'Neptune', 'Uranus', 'Pluto' ]
Planets.pop()
-OR-
Planets.remove("Pluto")
-OR-
Planets.pop(8)
'''


'''
2. Write code to insert 'Asteroid belt' between 'Mars' and 'Jupiter'.
'''
Middle = ["Mars","Jupiter"]
Middle.insert(1, "Asteroid Belt")
print(Middle)