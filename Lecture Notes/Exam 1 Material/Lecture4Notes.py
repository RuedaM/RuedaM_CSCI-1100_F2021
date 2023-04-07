#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:53:09 2021

@author: maxrueda
"""

"---Lecture 4 Notes - Using Functions + Modules---"

#So far, we have learned about three basic data types: integer, float and
# strings.
#We also learned some valuable functions that operate on strings (len) and
# that convert between data types (int, str, float)

Name = "Pickle Rick"
print(len(Name))

#The functions that Python provides are called built-in functions.
#We will see examples of these functions and experiment with their use in this
# class.
print("")
print("")


"How about numerical functions?"
#Many numerical functions also exist. Let us experiment with some of these
#first. You should make a note of what they do.

#abs() - returns the absolutle value of the number provided
#pow() - puts a number to the power of some other number; takes 2 inputs, the
#         first being the coefficient and the other, separated by a comma,
#         being the exponent
#int() - returns a number as an integer; this function will always round down
#float() - returns a number as a floating point decimal with deecimal places
#round() - rounds numbers to the nearest integer; this rounds up from 5; a
#           second comma-separated number can be added to indicate the number
#           of displayed decimal places
#max() - returns the largest value in a given comma-separated list of values
#min() - returns the smallest value in a given comma-separated list of values


"Objects and Methods"
#All variables in Python are objects.
#Objects are abstractions:
#   Each object defines an organization and structure to the data they store.
#   They have operations/functions — we call them methods — that we can apply
#    to access and manipulate this data.
#   We don’t think about how they are implemented; instead we just think about
#    how to use them. This is why they are called abstractions.

#Methods associate with objects often use a function call syntax of the form:
# variable.method(arguments). For example:
b = 'good morning'
print(b.find('o', 3))

#This also works on particular values instead of variables:
#value.method(arguments)

print('good morning'.find('o', 3))
#Note: here, find() starts looking for 'o' at the 3rd index (letter 'd'),
# which is why the function does not return 1 - if the function were to change
# to 'good morning'.find('o', 7), it would return a -1 because it did not find
# a corresponding letter

#You can see all the methods that apply to an object type with help() as well:
print("")
print("")


"String Methods"
#Here are a few more (of many) string methods:
name = "Neil Degrasse Tyson"
print(name.lower())
#Sets all of a string's characters to lowercase

lowername = name.lower()

print(lowername.upper())
#Sets all of a string's characters to uppercase

print(lowername.capitalize())
#Capitalizes the first letter of the first word in an entire string

print(lowername.title())
#Capitalizes the first letter of every space-separated word in a string

print(name.find(" "))
#Finds the location of the first iteration of the defined character and
# returns the index value

print(name.find("a"))

print(name.find("x"))
print("")
#If the function cannot find an indicated


magic = "abracadabra"
print(magic.replace("br", "dr"))
#Replaces the first set of characters defined before the comma with a new set
# of characters defined after the comma

print(magic.replace("a", ""))
#You can effectively "delete" with this by replacing things with ""
print("")


print("Monty Python".count("o"))
#Counts the number of iterations of the character/phrase and returns the count
# as an integer

print("aaabbbfsassassaaaa".strip("a"))
#Strips the front and end of a string, which is usually a space (shown as
# 'a's' to visualize this), and only leaves the center of the string

#As described above, all of these are called in the form of
# object.method(arguments), where object is either a string variable or a
# string value.
print("")
print("")


#Not all functions on objects are called this way; Some are called using more
# of a function form, while others are called as operators:

episode = "Cheese Shop"
print(episode.lower())
print(len(episode))
print(episode + "!")

#We will see the reason for the differences later in the semester.
#Note of caution: none of these functions change the variable that they are
# applied to.
print("")
print("")
print("")



"---String Format Method---"
#The format() method provides a nice way to produce clean looking output:

#Take, for example, this code:
pi = 3.14159
r = 2.5
h = 10**0.5
volume = pi * r**2 * h
print('A cylinder of radius', r, 'and height', h, 'has volume', volume)

#Now look at what we can do with the format() method:
out_string = 'A cylinder of radius {0:.2f} and height {1:.2f} has volume {2:.2f}'.format(r, h, volume)
print(out_string)

#Method format() replaces the substrings between { } with values from the
# argument list.

#{0:.2f} means argument 0, will be formatted as a float (f) with 2 digits
# shown to the right of the decimal place.

#Notice it applies rounding.
#We can leave off the 0, the 1, and the 2 from before the : unless we want to
# change the order of the output.
#We can leave off the :.2f if we want to accept print’s normal formatting on
# float outputs.
print("")
print("")


"---Built-In Functions---"
#All the functions we have seen so far are built-in to the core Python. It
# means that these functions are available when you start Python.
#Type help(__builtins__) to see the full list.


"---Modules---"
#Now we will begin to look at using functions that are not built into the core
# of Python but rather imported as modules.

#Modules are collections of functions and constants that provide additional
# power to Python programs.

#Some modules come with Python, but are not loaded automatically. For example,
# the math module.

#Other modules need to be installed first. When we installed software in Lab 0,
# we installed a library called pillow that has a number of image manipulation
# modules.

#To use a function in a module, first you must load it into your program using
#import:

import math

print(math.sqrt(5))
#Returns the square root of the input

print(math.trunc(4.5))
#Cuts out the decimals place of a float and leaves only the integer; this does
# NOT round up/down, only cuts the decimals off

print(math.ceil(4.5))
#Rounds up a floating point decimal to the nearest whole integer

print(math.floor(4.5))
#Rounds down a floating point decimal to the nearest whole integer

print(math.log(1024,2))
#Takes the logarithm of the first input; if provided, the second input is the
# base ofhte logarithm

print(math.pi)
#Provides a more accurate value of pi than a stopped decimal

#We can get an explanation of what functions and variables are provided in a
# module using help(math)
print("")
print("")


"---Different Ways of Importing---"
#The way you import a module determines what syntax you need to use the
# contents of the module in your program.

#We can import only a selection of functions and variables:
"""
from math import sqrt,pi
>>> pi
3.141592653589793
>>> sqrt(4)
2.0
"""

#Or we can give a new name to the module within our program:
"""
>>> import math as m
>>> m.pi
3.141592653589793
>>> m.sqrt(4)
2.0
"""

#Both of these methods help us distinguish between the function sqrt and the
# data pi defined in the math module from a function with the same name (if we
# had one) in our program.

#We can also do this (which is NOT recommended!):
"""
>>> from math import *
"""
#Now, there is no name difference between the math module functions and ours.
#Since this leads to confusion when the same name appears in two different
# modules it is almost always avoided.


"---Program Structure---"
#We have now seen several components of a program: import, comments, and our
# own code, including input, computation and output statements. We will add
# more components, such as our own functions, as we proceed through the
# semester.

#You should organize these components in your program files to make it easy to
# see the flow of the program

# We will use the following convention to order the program components:
'''
an initial comment explaining the purpose of the program,
all import statements,
then all variables and input commands,
then all computation,
finally all output.
'''


"---Putting It All Together---"
#In the rest of this class we will write a program that first asks the user
# for a name, then asks for the radius and height of a cylinder, and finally
# prints the surface area and volume of the cylinder, nicely formatted.


"---SUMMARY---"
#Python provides many functions that perform useful operations on strings,
# integers and floats.
#Some of these functions are built in while others are organized into modules.
#Be aware of the differences between how functions are called. You must
# remember them to call them correctly.
#Functions that require dot notation, applying the function to an object (or a
# variable containing an object):
'''
>>> "abc".upper()
'ABC'
'''
#Functions that are called with arguments (no dot notation):
'''
>>> x = -4.6
>>> abs(x)
4.6
>>> round(x)
-5
'''
#Note that these functions are actually aliases. The same function also exists
# in dot notation.
'''
>>> x = -4.6
>>> x.__abs__()
4.6
>>> x.__round__()
-5
>>> 4.6.__round__()
5
>>> (-1).__abs__()
1
'''
#After a module is imported, the functions in the module can be used by a call
# of the form: module_name.function_name(arguments)
#You can see the details of a function by: help(module_name.function_name)
#Python has many modules that make it easy to do complicated tasks. If you do
# not believe it, try typing: import antigravity



"---Lecture 4 Practice Problems 1---"

'''
1. Write code that takes a string in a variable called phrase and prints the
   string with all vowels removed.
'''
phrase = "supercalifragilisticexpialidocious"
phrase = phrase.replace("a", "").replace("e", "").replace("i", "")
phrase = phrase.replace("o", "").replace("u", "")
print(phrase)


'''
2. Create a string and assign it to a variable called name. Write code to
   create a new string that repeats each letter a in name as many times as "a"
   appears in name (assume the word is all lower case).
For example,
>>> name = "amos eaton"
## your code goes here
>>> name
'aamos eaaton'
'''
name = "amos eaton"
name = name.replace("a", "aa")
print(name)


'''
3. Given a string in a variable called name, switch all letters a and e (only
   lowercase versions). Assume the variable contains only letters and spaces.
Hint: first replace each ‘a’ with ‘1’.
>>> name = "Rensselaer Polytechnic Institute"
## your code goes here
>>> name
'Ranssalear Polytachnic Instituta'
'''
name = "Rensselaer Polytechnic Institute"
name = name.replace("a", "1").replace("e", "2")
name = name.replace("1", "e").replace("2", "a")
print(name)



"---Lecture 4 Practice Problems 2---"

'''
1. The math module contains the constant e as well as pi. Write code that
   prints these values accurate to 3 decimal places and then write code that
   computes and outputs [pi]^e and e^[pi] both accurate to 2 decimal places.
'''
import math
print("""The value of pi: {0:.3f}
The value of e: {1:.3f}""".format(math.pi, math.e))
print("""[pi]^e = {0:.2f}
e^[pi] = {1:.2f}""".format((math.pi ** math.e),(math.e ** math.pi)))


'''
2. Write a short program to ask the user to input height values (in
   centimeters) three times. After reading these values (as integers), the
   program should output the largest, the smallest and the average of the
   height values.
'''
Value1 = int(input("Please give one height measurement: "))
Value2 = int(input("Please give another height measurement: "))
Value3 = int(input("Please give one more height measurement: "))
print("Largest of the values: ", max(Value1, Value2, Value3))
print("Smallest of the values: ", min(Value1, Value2, Value3))
print("Average of all values: ", ((Value1 + Value2 + Value3) / 3))


'''
3. What happens when we type
import math
math.pi = 3
   and then use math.pi?


Rather than acting as an integer, math.pi becomes something similar to a
variable with an assigned value 3 rather than 3.1411592... - math.pi will then
always be 3 until it is assigned a new integer or is reset
'''