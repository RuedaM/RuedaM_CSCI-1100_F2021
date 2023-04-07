#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 17:28:03 2021

@author: maxrueda
10/26/21
CSCI 1100
Lect. Exercises 15.2
"""

"""
2. Write a Python program that asks the user for two strings: (1) the name of
    a file formatted in the same way as the IMDB data, and (2) a string that
    is the start of a last name. Remember to strip the input strings before
    using them. A number of you are still losing points because of the \r
    character on some of the input strings. The program should output the
    number of different last names that are in the file and it should output
    the number of different names that start with the string. Your program
    must use a set and you may / are encouraged to start from the code written
    during lecture.

   We define a last name to be everything up to the first comma in the name.
    (Some names will not have commas in them, and be careful to avoid adding
     empty last names to the set.) For example:
Downey Jr., Robert | Back to School |      1986
Downey Sr., Robert   | Moment to Moment  | 1975
Downey, Elsie    | Moment to Moment     |  1975
    would result in three different last names, Downey Jr., Downey Sr. and
    Downey.

   Here is one example of running our solution:
Data file name: imdb/imdb_data.txt
Prefix: Down
48754 last names
10 start with Down

   Before uploading your Python file to Submitty you should test using the
    data files (or restricted versions of them!) we provided for Lecture 15 on
    the Submitty Course Materials page. On Submitty we will test with
    different files and examples.
"""

fileName = input("Data file name: ").strip()
print(fileName)

prefix = input("Prefix: ").strip()
print(prefix)

namesSet = set()
for line in open(fileName, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    
    name = name.split(",")[0].strip()
    namesSet.add(name)


prefixStarting = 0
for name in namesSet:
    if (name.find(prefix) == 0):
        prefixStarting += 1


print("{} last names".format(len(namesSet)))
print("{} start with {}".format(prefixStarting, prefix))