#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:18:53 2021

@author: maxrueda
"""

"---Lecture 5 Notes - Python Functions---"


"Why Functions?"
#The purpose of today’s class is to introduce the basics of writing and
# running Python functions.
#Repeating code is painful.
#It is also hard to distinguish between the same code repeated three times and
# three different computations.
#It is easy to find a mistake in one copy of a section of code and forget to
# fix it in the other copies.
#Learn a programmer’s motto: DRY – don’t repeat yourself.
#Define it once and use it multiple times.
#Functions are extremely useful for writing complex programs:
#They divide complex operations into a combination of simpler steps.
#They make programs easier to read and debug by abstracting out frequently
# repeated code.


"Functions"
#As we have learned, a function:
# Takes as input one or more arguments.
# Computes a new value, a string or a number.
# Returns the value, so that it can be assigned to a variable/output.

#Let’s recall this with a built-in function:

#       print(len('RPI Puckman'))
#       11
#Can you identify the input argument, computation and returned value?
#   'RPI Puckman' is the input argument, len() and print() is the computation,
#    and 11 is the returned value


"A Function to Compute the Area of a Circle"
#In mathematics, many functions are given as formulas. You might write a
# function to calculate the area of a circle as 𝑎(𝑟)=𝜋𝑟^2

#In Python, typing into a file (in the upper pane of the Spyder IDE), we write:

def area_circle(radius):
    pi = 3.14159
    area = pi * radius**2
    return area

#Note that the def is not indented and the other lines are indented
# four spaces - this indicates that the following statements are under the
# user-defined function area_circle

#We add unindented code the file below the definition of area_circle() to
# execute the function and calculate the area:
a = area_circle(1)
print(a)
print('A circle with radius 2 has area {:.2f}'.format(area_circle(2)))

r = 75.1
a = area_circle(r)
print("A circle with radius {:.2f} has area {:.2f}".format(r,a))
#(Note: by using examples with small values for the radius we can easily check
# that our function is correct.)

#Important syntax includes
#Use of the keyword def and the : to indicate the start of the function
#Indentation for the lines after the def line
#Unindented lines for code outside the function to indicate the end of the
# function.
print("")
print("")


"What does Python do when we run this code?"
#We can visualize this using the website http://www.pythontutor.com

#1. Reads the keyword def and notes that a function is being defined - the
#    line that starts with def is called the function header.
#2. Reads the rest of the function definition, checking its syntax.
#3. Notes the end of the definition when the unindented code is reached.
#4. Sees the function call inside the assignment statement 'a = area_circle(1)'
#    at what’s known as the “top level” or “main level” of execution and:
#       -Jumps back up to the function
#       -Assigns 1 to the parameter radius.
#       -Runs the code inside the function using radius as a variable inside
#         the function.
#       -Returns the result of the calculation back to the top level and
#         assigns the value 3.14159 to the variable a.
#5. Repeats the process of running the function at the second print(), this
#    time with the parameter value 2 and therefore a new value for radius
#    inside the function.
#6. Repeats the process of running the function right after we reassign a,
#    this time with parameter value 75.1 taken from the variable r.


"Flow of Control"
#To re-iterate, the “flow of control” of Python here involves
#Reading the function definition without executing the function.
#Seeing a “call” to the function, jumping up to the start of the function and
# executing its code.
#Returning the result of the function back to the place in the program that
# called the function and continuing the execution.
#Functions can compute many different things and return any data type Python
# supports.


"Arguments, Parameters, and Local Variables"
#Arguments are the values 1, 2 and 75.1 in our above examples.
#These are each passed to the parameter called radius named in the function
# header. This parameter is used just like a variable in the function.
#The variable pi and area are local variables to the function (though we
# should probably use the math module for pi in the future).
#Neither pi nor radius nor area exists at the top / main level. At this level,
# they are ‘’undefined variables’’. Try it out.


"Exercise / Example"
#As some basic practice, we’ll write a function to convert miles per hour to
# kilometers per day, and then we’ll write several calls to demonstrate its
# use. Then we will give you time to work on the first lecture exercise.

def mph_to_kpd(mph):
    mpd = mph * 24.0
    kpd = mpd  * 1.60932
    return kpd

mph = float(input("Enter miles per hour: "))
kpd = mph_to_kpd(mph)
print("A vehicle traveling {0:.2f} mph is traveling about {1:.2f} kpd".format(mph, kpd))
print("")
print("")


"Computing the Surface Area of A Cylinder Using Two Functions"
"A More Complicated Example"
#We’ll use the example below to illustrate two important concepts:
#1. Functions can call other functions, ones that we write ourselves or that
#    Python provides.
#2. Functions may have multiple parameters. One argument in the function call
#    is required for each parameter. Arguments and parameters are matched up
#    in order.

#We will switch to the use of math.pi and use this from now on

import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_cylinder(radius,height):
    circle_area = area_circle(radius)
    height_area = 2 * radius * math.pi * height
    return 2*circle_area + height_area

print('The area of a circle of radius 1 is', round(area_circle(1),2))
r = 2
height = 10
print('The surface area of a cylinder with radius', r)
print('and height', height, 'is', round(area_cylinder(r,height),2))

#Now we’ve defined two functions, one of which calls the other.

#Flow of control proceeds in two different ways here:
#1. Starting at the first print() function call at the top level, into
#    area_circle() and back.
#2. At the third print():
#       1. into area_cylinder()
#       2. into area_circle()
#       3. back to area_cylinder(), and
#       4. back to the top level (and then into round() and finally into
#           print()).

#The Python interpreter keeps track of where it is working and where to return
# to when it is done with a function, even if it is back into another function.

#What are the arguments, the parameters, the local variables and the global
# variables?
#       Arguments are the 1 and 2 in round(area_circle(1),2), r = 2,
#        height = 10, and 2 in round(area_cylinder(r,height),2)
#       Paramenters are radius in area_circle(radius) and radius and height in
#        area_cylinder(radius,height)
#       Local variables are circle_area and height_area in the function
#        area_cylinder
#       Global variablles are r and height
print("")
print("")

"More on program structure"
#Let's revisit the program structure that will allow us to write readable
# programs.
#First a general comment describing the program.
#Second, all import statements.
#Third, all function definitions.
#Fourth, the main body of your program.
#Well structured programs are easy to read and debug. We will work hard to
# help you develop good habits early on.


"Thinking About What You See"
#Why is it NOT a mistake to use the same name, for example radius, in
# different functions (and sometimes at the top level)?
#       Both paramenters named 'variable' are only local to the function, so
#        they would not be confused betwen each other


"A Final Example, Including Documentation"
#We will write a function that linearly scales a test score, so that if raw is
# the “raw score” then the scaled score will be 'scaled = a*raw + b'

#The values of raw, a and b will be parameters of the function. We will also
# want to cap the scaled score at 100.

#In writing our function we will be careful to document the meaning of the
# parameters and the assumptions. You should get into the habit of doing this.

def scale(raw, a, b):
    scaled = a*raw + b
    return min(100, scaled)

score = float(input("Enter score: "))
factor = 1.1
constant = 5
print(scale(score, factor, constant))
print("")
print("")


"Why Functions?"
#Our goal in using functions is to write code that is
#Easier to think about and write
#Easier to test: we can check the correctness of area_circle before we test
# area_cylinder.
#Clearer for someone else to read
#Reusable in other programs
#Together these define the notion of encapsulation, another important idea in
# computer science!

"---SUMMARY---"
#Functions for encapsulation and reuse
#Function syntax
#Arguments, parameters and local variables
#Flow of control, including functions that call other functions



"---Lecture 5 Practice Problems---"

'''
1. Write a function that computes the area of a rectangle. Then, write a
   second function that calls this function three times to compute the surface
   area of a rectangular solid.
Note: You will notice that the solution to the first problem in particular is
 longer than the solution without using functions. While we don’t often write
 such short functions in practice, here it is a good illustration.
'''
def rectangle_area(x, y):
    area = x * y
    return area

def rectangle_surface_area(height, width, depth):
    face1 = rectangle_area(height, width)
    face2 = rectangle_area(width, depth)
    face3 = rectangle_area(depth, height)
    surface_area = (face1 + face2 + face3) * 2
    return surface_area

height = int(input("Give dimension 1: "))
width = int(input("Give dimension 2: "))
depth = int(input("Give dimension 3: "))
surface_area = rectangle_surface_area(height, width, depth)
print("")
print("Surface area = " + str(surface_area))


'''
2. Write a function that returns the middle value among three integers.
 (Hint: make use of min() and max()). Write code to test this function with
 different inputs.
'''

def middle(int1, int2, int3):
    least = min(int1, int2, int3)
    greatest = max(int1, int2, int3)
    middle = ((int1 + int2 + int3) - least) - greatest
    return middle

int1 = int(input("Enter Integer 1: "))
int2 = int(input("Enter Integer 2: "))
int3 = int(input("Enter Integer 3: "))
print(middle(int1, int2, int3))