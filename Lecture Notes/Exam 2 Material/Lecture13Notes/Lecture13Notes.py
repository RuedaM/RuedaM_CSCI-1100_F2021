#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:46:19 2021

@author: maxrueda
"""

"---Lecture 13 - Controlling Loops---"

"Overview"
#Review of string operations
#Files on your computer
#   Opening and reading files
#   Closing
#   Writing files
#Accessing files across the web
#Parsing basics
#Parsing html


"Review — String operations often used in file parsing"
#Let’s review and go over some very common string operations that are
# particularly useful in parsing files.

#Remove characters from the beginning, end or both sides of a string with
# lstrip, rstrip and strip:

x = "red! Let's go red! Go red! Go red!"
print(x.strip("red!"))      #Can strip a whole collection of characters
print(x.strip("edr!"))      #Stripped characters don't have to be in order!
print(x.lstrip("red!"))     #Only strips from left
print(x.rstrip("red!"))     #Only strips from right
print("")
print("    Go red!      ".strip())
print(" \n   Go red!    \t  ".strip())
print(" \n   Go red!    \t  ".strip(' '))

#With no arguments, the .strip() functions remove ALL white space characters
#The last example here specifies the stripping of " ", so both \n and \t stay
print("")
print("")

#.split() a string using a delimiter character and get a list of strings:
# (Whitespace is the default delimiter)
x = "Let's go red! Let's go red! Go red! Go red!"
print(x.split())
print(type(x.split()))      #Shows that the function changes x to a list
print("")
print(x.split("!"))         #Deletes any "!" + splits string at these pts
print(x.split("red!"))      #Deletes any "red!" + splits string at these pts
print("")
print("Let's go red! \n Let's go    red! Go red! \t Go red!".split(" "))
print("Let's go red! \n Let's go    red! Go red! \t Go red!".split())

#split returns the strings before and after the delimiter string in a list.
print("")
print("")

#The .find() function returns the first location of a substring in a string,
# and returns -1 if the substring is not found. You can also optionally give
# a starting and end point to search from:
x = "Let's go red! Let's go red! Go red! Go red!"
print(x.find('red'))
print(x.find('Red'))        #Nothing found - returns -1
print(x.find("edr!"))       #Nothing found - returns -1
print("")
print(x.find('red',10))
print(x.find('red',10,12))
print("")
print('red' in x)       #Usually used in a for-loop, in can be used to see if
print('Red' in x)       # substrings exist in a string - outputs booleans
print("")
print("")
print("")



"Opening and Reading Files"
#On to our main topic….

#Given the name of a file as a string, we can open it to read:
f = open('BeeMovie.txt')
#This is the same as:
f = open('BeeMovie.txt','r')
#Variable f now “points” to the first line of file abc.txt.
#The "r" signifies read mode which tells Python we will be reading from this
# file — this is the default


#One way to access contents of a file is by doing so one input line at a time
#(To help illustrate reading files, lines marking the strings are printed)

# In particular:
line = f.readline()
print("\/ STRING HERE \/")
print(line)
print("/\ STRING HERE /\\")
#.readline() reads in the next line up to and including the end-of-line
# character, and “advances” f to point to the next line of file abc.txt
# Notice how the whitespace \n is also printed
print("")

#By contrast:
s = f.read()
print("\/ STRING HERE \/")
print(s)
print("/\ STRING HERE /\\")
#.read() will do the following:
#   read the entire REMAINDER of the input file as a single string
#   storing the one (big) string in s, and
#   advancing f to the end of the file
print("")

#When you are at the end of a file, f.read() and f.readline() will both return
# the empty string "":
s = f.read()
print("\/ STRING HERE \/")
print(s)
print("/\ STRING HERE /\\")
f.close()
print("")
print("")
print("")



"Reading the contents of a file"
#The most common way to read a file is illustrated in the following example
# that reads each line from a file and prints it on the screen:
f = open('BeeMovie.txt')

print("\/ LOOP HERE \/")
for line in f:
    print(line)
print("/\ LOOP HERE /\\")
#And gain, the whitespace characters are printed
#(Of course you can replace the call to print() with any other processing code
# since each line is just a string!)
print("")
print("")

#You can combine the above steps into a single for loop:
print("\/ LOOP HERE \/")
for line in open('BeeMovie.txt'):
    print(line)
print("/\ LOOP HERE /\\")
print("")
print("")
print("")



"Closing and Reopening Files"
#The code below opens, reads, closes and reopens a file

f = open('BeeMovie.txt')
# Insert whatever code is need to read from the file
# and use its contents ...
f.close()

f = open('BeeMovie.txt')

#f now points again to the beginning of the file
#This can be used to read the same file multiple times

#Think of f as a cursor moving through a file
# When a .read() function is called, the cursor moves through the string up to
# a certain point (depending on if .readline() or .read() is used) and stops
# at that point thi is why nothing is printed if a .read() is called again
# after a whole file has been printed through



"Example: Computing the Average Score"
#We are given a file that contains a sequence of integers representing test
# scores, one score per line. We need to write a program that computes the
# average of these scores.

#Here is one solution:
file_name = input("Enter the name of the scores file (HINT: it's scores.txt'): ")
file_name = file_name.strip()   #Delete extra whitespace the user might type
print(file_name)

num_scores = 0
sum_scores = 0
for s in open(file_name):
    sum_scores += int(s)
    num_scores += 1

print("Average score is {:.3f}".format( sum_scores / num_scores ))

#In class we will discuss:
#   Getting the file name from the user
#   The importance of using strip
#   The rest of the program
print("")
print("")
print("")



"Writing to a File"
#In order to write to a file we must first open it and associate it with a
# file variable:
f_out = open("outfile.txt","w")
#The "w" signifies write mode which causes Python to completely delete the
# previous contents of outfile.txt (if the file previously existed).

#It is also possible to use append ("a") mode:
f_out = open("outfile.txt","a")
# which means that the contents of outfile.txt are kept and new output is
# added to the end of the file
#Write mode is much more common than append mode

#To actually write to a file, we use the write method:
f_out.write("Hello world!\n")
#Each call to write passes only a single string

#Unlike what happens when using print, spacing and newline characters are
# required explicitly
#You can use the format method of each string before you print it


#You must close the files you write, otherwise the changes you made will not
# be recorded!
f_out.close()

#To show what we've done, here's what the file reads:
myFile = open("outfile.txt")
print(myFile.read())
myFile.close()
print("")
print("")
print("")



"Opening Static Web Pages"
#We can import the urllib module to access web pages
#We did this with our very first “real” example:
"""
import urllib.request

word_url = 'http://www.greenteapress.com/thinkpython/code/words.txt'
word_file = urllib.request.urlopen(word_url)
"""
#Once we have word_file, we can use the .read(), .readline(), and .close()
# methods just like we did with “ordinary” files


#Static web pages are unchanging, like a text file or blog post, so we can edit
# or read them freely since nothing will happen to them
#When the web page is dynamic, we usually need to work through a separate API
# (application program interface) to access the contents of the web site



"Parsing"
#Before writing code to read a data file or to read the contents of a web page,
# we must know the format of the data in the file.
#The work of reading a data file or a web page is referred to as parsing.

#Files can be of a fixed well-known format:
#   Python code
#   C++ code
#   HTML (HyperText Markup Language, used in all web pages)
#   JSON (Javascript Object Notation, a common data exchange format)
#   RDF (resource description framework)

#Often there is a parser module for these formats that you can use instead of implementing them from scratch
#For code, parsers check for syntax errors.



"Short tour of data formats"
#Python code:
#   -Each statement is on a separate line
#   -Changes in indentation are used to indicate entry/exit to blocks of code,
#     e.g. within def, for, if, while…


#HTML:
#Basic structure = mix of text with commands that are inside “tags” < ... >.
#Example:
"""
<html>
   <head>
      <title>HTML example for CSCI-100</title>
   </head>
   <body>
      This is a page about <a href="http://python.org">Python</a>.
      It contains links and other information.
   </body>
</html>
"""
#Despite the clean formatting of this example, html is in fact free-form, so
# that, for example, the following produces exactly the same web page:
"""
<html><head><title>HTML   example for CSCI-100</title>
</head> <body> This is a page about <a
href="http://python.org">Python</a>.  It contains   links
and other   information. </body> </html>
"""
#This is becuase spaces and indentation do not matter in HTML, so long as the
# grouping and tags are correctly used/placed


#JSON:
#Used often with Python in many Web based APIs:

{
   "class_name": "CSCI 1100"
   , "lab_sections" : [
          { "name": "Section 01"
             , "scheduled": "T 10AM-12PM"
             , "location": "Sage 2704"
          }
          , { "name": "Section 02"
             , "scheduled": "T 12PM-2PM"
             , "location": "Sage 2112"
          } ]
 }
#Similar to HTML, spaces do not matter.

#Json is a simple module for converting between a string in JSON format and a
# Python variable:

import json
x = ' [ "a", [ "b", 3 ] ] '
print(json.loads(x))
print("")
print("")
print("")



"Parsing ad-hoc data formats - Regular tabular data"
#We will examine some simple formats that you may have already seen in various
# contexts.

#Parsing files with fixed format in each line, delimited by a character
#Often used: comma (csv), tab or space
#One example is a file of comma separated values, Each line has a label of a
# soup type and a number of cans we have available:
"""
chicken noodle, 2
clam chowder, 3
"""
#Here is pseudo code for processing such files:
"""
for each line of the file:
    split into a list using the separator
    process the entries of the list into the desired form
"""

#Practice Problem: write a simple parser for the soup list that returns a list
# of the form:
["chicken noodle", "chicken noodle", "clam chowder", "clam chowder", "clam chowder"]

soupFile = input("Enter file name (soup.txt): ").strip()
soupList = []
for line in open(soupFile):
    lineNew = line.split(",")
    soupName = lineNew[0].strip()
    soupCount = int(lineNew[1])
    soupList = soupList + [soupName]*soupCount

print(soupList)



"Parsing ad-hoc data formats - Irregular tabular data"
#Parsing files with one line per row of information, different columns
# containing unknown amount of information separated with a secondary delimiter

#Example: Yelp data with the name of a restaurant, the lattitude, the
# longitude, the address, the URL, and a sequence of reviews
"""
Meka’s Lounge|42.74|-73.69|407 River Street+Troy, NY 12180|http://www.yelp.com/biz/mekas-lounge-troy|Bars|5|2|4|4|3|4|5
"""

#Information after column 5 are all reviews
#The address field is separated with a plus sign

#Pseudo code:
"""
for each line of the file
    split using the separator
    split the entry with secondary separator
    for each value in the column
        handle value
"""

#Practice Problem: Write a function that returns a list of lists for a file
# containing Yelp data. Each list should contain the name of the restaurant
# and the average review



"---SUMMARY---"
#You should now have enough information to easily write code to open, read,
# write and close files on local computers
#Once text (or HTML) files found on the web are opened, the same reading
# methods apply just as though the files were local. Binary files such as
# images require special modules
#Parsing a file requires understanding its format, which is, in a sense, the
# “language” in which it is written
#You will practice with file reading and writing in future labs and homework
#assignments