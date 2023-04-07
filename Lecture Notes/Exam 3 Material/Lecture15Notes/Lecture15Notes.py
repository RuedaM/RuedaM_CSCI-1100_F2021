#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:31:12 2021

@author: maxrueda
"""

"---Lecture 15 Notes - Sets---"

"Overview"
#Example: finding all individuals listed in the Internet Movie Database (IMDB)
#A solution based on lists
#Sets and set operations
#A solution based on sets
#Efficiency and set representation

#Reading is Section 11.1 of Practical Programming.


"Finding All Persons in the IMDB file"
#We are given a file extracted from the Internet Movie Database (IMDB) called
# imdb_data.txt containing, on each line, a person’s name, a movie name, and a
# year. For example:
"""
Kishiro, Yukito   | Battle Angel    | 2016
"""

#Goal:
#   Find all persons named in the file
#   Count the number of different persons named.
#   Ask if a particular person is named in the file

#The challenge in doing this is that many names appear multiple times

#First solution: store names in a list. We’ll start from the following code,
# lec15_find_names_start.py:
"""
import time
    
imdb_file = input("Enter the name of the IMDB file (imdb_data.txt) ==> ").strip()
name_list = []
start_time = time.time()

for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    
    if not (name in name_list):
        name_list.append(name)
        if len(name_list)%1000 == 0:
            end_time = time.time()
            print("list is {} and time is {:.2f}".format(len(name_list), (end_time - start_time)))
            start_time = end_time

for n in name_list:
    print("\t{}".format(n))
"""
#The challenge is that we need to check that a name is not already in the list
# before adding it.

#You may access the data files we are using from and the starting code .py
# file from lec15_files.zip on the Course Resources page of the Submitty site


"How To Test?"
#The file imdb_data.txt has about 260K entries. How will we know our results
# are correct?
#Even if we restrict it to movies released in 2010-2012 (the file
# imdb_2010-12.txt), we still have 25K entries!
#We need to generate a smaller file with results we can test by hand

#I have generated hanks.txt for you and will use it to test our program before
# testing on the larger files.


"What Happens?"
#Very slow on the large files because we need to scan through the list to see if a name is already there.
#We’ll write a faster implementation based on Python sets.
#We’ll start with the basics of sets.


"Sets"
#A Python set is an implementation of the mathematical notion of a set:
#   No order to the values (and therefore no indexing)
#   Contains no duplicates
#   Contains whatever type of values we wish; including different-type values
#This is all very similar to a list, save for a few things

#Python set methods are exactly what you would expect: Each has a function
# call syntax and many have operator syntax in addition


"Set Methods"
#Initialization comes from a list, a range, or from just set():

s1 = set()
print(type(s1))
print("")

s2 = set(range(0,11,2))
print(s2)   #Lists are denoted by curly braces {}
print("")

v = [4, 8, 4, 'hello', 32, 64, 'spam', 32, 256]
print(len(v))
s3 = set(v)
#You can also get the length of a set as you would a list
print(len(s3))
print(s3)
#But notice how there are two less elements in the set s3 - all repeated
# values in v were deleted when v was made into a list
print("")
print("")


#The actual methods are:
#   s.add(x) — add an element if it is not already there
#   s.clear() — clear out the set, making it empty
#   s1.difference(s2) — create a new set with values from s1 that aren't in s2
s4 = set()
s4.add(10)
print(s4)
print("")
s4.clear()
print(s4)   #Would only print set(), which means nothing is in the set
print("")
s5 = set(range(0,11,2))
s6 = {10, 2}
print(s5, s6)

print("")
print("")


#Set methods with Opperator Syntax:
#   s1.difference(s2)           or  s1 - s2:  subtract all values of smaller
#                                              set from bigger set
#   s1.intersection(s2)         or  s1 & s2:  create a new set that contains
#                                              only the values that are in
#                                              both sets
#   s1.union(s2)                or  s1 | s2:  create a new set that contains
#                                              values that are in either set
#   s1.issubset(s2)             or  s1 <= s2: are all items of s1 also in s2?
#   s1.issuperset(s2)           or  s1 >= s2: are all items of s2 also in s1?
#   s1.symmetric_difference(s2) or  s1 ^ s2:  create a new set that contains
#                                              values that are in s1 or s2 but
#                                              not in both

#x in s - evaluates to True if the value associated with x is in set s.

#We will explore the intuitions behind these set operations by considering:
#   s1 to be the set of actors in comedies,
#   s2 to be the set of actors in action movies
#and then consider who is in the sets
"""
s1 - s2
s1 & s2
s1 | s2
s1 ^ s2
"""


"Back to Our Problem"
#We’ll modify our code to find the actors in the IMDB. The code is actually
#very simple and only requires a few set operations:
import time

imdb_file = input("Enter the name of the IMDB file (imdb_data.txt) ==> ").strip()
start_time = time.time()

name_list = []
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    name_list.append(name)
    
name_list.sort()

count = 1
for i in range(1, len(name_list)):
    if (name_list[i-1] != name_list[i]):
        count += 1
        
        if len(name_list)%1000 == 0:
            end_time = time.time()
            print("list is {} and time is {:.2f}".format(len(name_list), (end_time - start_time)))
            start_time = end_time

end_time = time.time()
print("Total time required: {:.2f} seconds".format((end_time - start_time)))
print("Number ofunique names in the IMDb:", count)


"Side-by-Side Comparison of the Two Solutions"
#Neither the set nor the list is ordered - We can fix this at the end by
# sorting

#The list can be sorted directly, but the set must be converted to a list
# first The function sorted does this for us

#What about speed? The set version is MUCH FASTER — to the point that the list
# version is essentially useless on a large data set

#We’ll use some timings to demonstrate this quantitatively
#We’ll then explore why in the rest of this lecture.


"Comparison of Running Times for Our Two Solutions"
#List-based solution:
#Each time before a name is added, the code — through the method in — scans
# through the entire list to decide if it is there
#Thus, the work done is proportional to the size of the list
#The overall running time is therefore roughly proportional to the square of
# the number of entries in the list (and the file)
#Letting the mathematical variable N represent the length of the list, we
# write this more formally as O(N^2), or “the order of N squared”

#Set-based code:
#For sets, Python uses a technique called hashing to restrict the running time
# of the add method so that it is independent of size of the set
#   (The details of hashing are covered in CSCI 1200, Data Structures)
#The overall running time is therefore roughly proportional to the length of the set (and number of entries in the file).
#We write this as O(N)

#We will discuss this type of analysis more later in the semester.
#It is covered in much greater detail in Data Structures and again in Intro.
# to Algorithms


"Set-Based Solution"
import time

imdb_file = input("Enter the name of the IMDB file (imdb_data.txt) ==> ").strip()
start_time = time.time()

names = set()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    names.add(name)

end_time = time.time()
print("Total time required: {:.2f} seconds".format((end_time - start_time)))
print(len(names))


"Discussion"
#Python largely hides the details of the containers — set and list in this case — and therefore it is hard to know which is more efficient and why.
#For programs applied to small problems involving small data sets, efficiency rarely matters.
#For longer programs and programs that work on larger data sets, efficiency does matter, sometimes tremendously. What do we do?
#In some cases, we still use Python and choose the containers and operations that make the code most efficient.
#In others, we must switch to programming languages, such as C++, that generate and use compiled code.


"---SUMMARY---"
#Sets in Python realize the notion of a mathematical set, with all the associated operations.
#Operations can be used as method calls or, in many cases, operators.
#The combined core operations of finding if a value is in a set and adding it to the set are much faster when using a set than the corresponding operations using a list.
#We will continue to see examples of programming with sets when we work with dictionaries.