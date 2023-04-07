#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 16:05:32 2021

@author: maxrueda
"""

"---Lecture 7 Notes, Tuples, Modules, & Images---"

"Overview"
#While most of these notes are not covered in our text book, these serve as an
# introduction to using more complex data types like lists.
#We will first learn a simple data type called tuples which allow us to work
# with multiple values together - including returning two or more values from
# a function.
#We will then revisit modules, how functions you write can be used in other
# programs.
#Most of the class we will be learning how to use a new module for
# manipulating images.
#We will introduce a new data type - an image - which is much more complex
# than the other data types we have learned so far.
#We will study a module called pillow which is specifically designed for this
# data type.

#At the end of this lecture material are some topics for review for our
# upcoming exam. We will try to cover this over the next few classes, but
# please read it over on your own as well…


"Tuple Data Type"
#A tuple is a simple data type that puts together multiple values as a single
# unit.
#A Tuple allows you to access individual elements: first value starts at zero
# (this “indexing” will turn into a big Computer Science thing!)

x = (4, 5, 10)   # note the parentheses
print(x[0])
print(x[2])
len(x)
print("")

#As we will explore in class tuples and strings are similar in many ways.
s = 'abc'
print(s[0])
print(s[1])
print("")

#Just like strings, you cannot change a part of the tuple; you can only change
# the entire tuple!   (Uncomment the following to reveal the type of errors)
'''
x[1] = 2

s[1] = 'A'
'''
print("")


"What are tuples good for?"
#Tuples are Python’s way of making multiple assignments:
x = 2, 3
print(x)
print("")

a, b = x
print(a)
print(b)
print("")

#Tuples allow for multiple-assignment on a single line:
c, d = 3, 4
print(c)
print(d)
print("")

part1 = 1, 2, 3, 4 
print(part1)            #You can put parenthesis around tuples,
part2 = (5, 6, 7)       # it's just a way of organizing - 
print(part2)            # it will always be returned as a
print(part1 + part2)    # comma-separated list
print("")
print("")

#You can write functions that return multiple values:
def split(n):
    ''' Split a two-digit number into its tens and ones digit '''
    tens = n // 10
    ones = n % 10
    return (tens, ones)

x = 83
ten,one = split(x)
print( x, "has tens digit", ten, "and ones digit", one )

#In the above example, the function is returning two values and the variables
# ten and one are being assigned a variable each to be used later on
print("")

#We can do the reverse, passing a tuple to a function:
def combine(digits):
    return digits[0]*100 + digits[1]*10 + digits[2]

d = (5, 2, 7)
print(combine(d))
print("")
print("")


"Basics of modules"
#Recall that a module is a collection of Python variables, functions and
# objects, all stored in a file, a file just like the ones we've made.
#Modules allow code to be shared across many different programs.

#Before we can use a module, we need to import it. The import of a module and
# use of functions within the module have the follow general form:
'''
import module_name
module_name.function(arguments)
'''


"Area and Volume Module"
#A file entitled lec07_area.py has been created on this device; in it are a
# number of functions from the area calculations we’ve been developing so far

#Now we can write another program that imports this code and uses it:
import lec07_area

r = 6
h = 10
a1 = lec07_area.circle(r)       #  Call a module function
a2 = lec07_area.cylinder(r,h)   #  Call a module function
a3 = lec07_area.sphere(r)       #  Call a module function
print("Area circle {:.1f}".format(a1))
print("Surface area cylinder {:.1f}".format(a2))
print("Surface area sphere {:.1f}".format(a3))
print("")
print("")


"PIL/PILLOW — Python Image Library"
#PILLOW is a series of modules built around the Image type, our first object
# type that is not part of the main Python language (so we need to import it)

#We will use images as a continuing example of what can be done in programming
# beyond numbers and beyond text.

#See http://pillow.readthedocs.org/en/latest/handbook/tutorial.html for more


"Images"
#An image is a two-dimensional matrix of pixel values
#The origin is in the upper left corner, see below:
"""
   (0,0)                                                (w-1,0)
       **************************************************
       **************************************************
       **************************************************
       **************************************************
       **************************************************
       **************************************************
       **************************************************
       **************************************************
       **************************************************
       **************************************************
       **************************************************
       **************************************************
       **************************************************
       **************************************************
 (0,h-1)                                                (w-1, h-1)
"""
#Pixel values stored in an image can be:
#   RGB — a “three-tuple” consisting of the red, green and blue values, all
#         non-negative integers
#   L — a single “gray-scale” integer value representing the brightness of
#       each pixel

#Some basic colors:
#Color       (Red,Green,Blue) value
#----------------------------------
#Black       (0,0,0)
#Red         (255,0,0)
#Green       (0,255,0)
#Blue        (0,0,255)
#White       (255,255,255)
#Light Gray  (122,122,122)


"Some important image modules"
#Image - contains main functions to manipulate images: open, save, resize,
#        crop, paste, create new images, change pixels, etc.
#ImageDraw - contains functions to touch up images by adding text, drawing
#            ellipses, drawing rectangles, etc.
#ImageFont - contains functions to create images of text for a specific font.

#We will only use the Image module in this lecture.


"Our First Image Program"
#Look to the file entitled lec07_images_init.py to find the separate program


"Image Type and Methods"
#Let us now see some very useful image methods. You need to be very careful
# with the image functions.

from PIL import Image

#Some functions do change the image and return nothing.
#Some functions do not change the image and return a value, which is sometimes
# a new image.

#It is crucial that you use each function correctly:
'''im = Image.open(filename)'''
#This reads an image with the given filename and returns an image object
# (which we are associating with the variable im).
#       Because we only give the file name, and not a more complete path, the Python
#        script and the image must be stored in the same folder.

#Images are complex objects. They have associated properties that you can
# print or use. For example:
im = Image.open('KonoDioDa.jpg')
print(im.size)
print(im.format)
print(im.mode)
#You can see that im.format and im.mode are strings, while im.size is a tuple.
# All of these are values associated with an image object.

#im.show() is a function that displays the image.

#im.save(filename) saves the image in the given file name

#You can create an empty new image with given dimensions using:
# Image.new("RGB",(width,height)).
im5 = Image.new('RGB', (200,200))
im5.show()

#You can also create a new image by cropping a part of a given image:
''''im.crop((w1,h1,w2,h2))'''
#which will crop a box from upper left corner (w1, h1) to lower right corner
# (w2,h2).

#You can see that the box is entered as a tuple.
#The image object im is not changed by this function, but a new image is
# returned. So, we must assign it to a new variable.

#Try this:
im2 = im.crop((100,100,300,400))
im2.show()
im.show()

#You can get a new image that is a resized version of an existing image. The
# new size must be given as a tuple: im.resize((width,height))
im3 = im.resize((300,200))
im3.save('resized.jpg')

#im.convert(mode) creates a copy of in image with a new mode - gray scale
# ('L') in the following example:
im4 = im.convert('L')
im4.show()


"Something new, functions that change an image"
#The functions we have seen so far return a new result, but never change the
# object that they apply to.

#More complex types such as images, often provide methods that allow us to
# change the object (image) for efficiency reason.

#You just have to remember how each function works.

#Here is our first function with this property: im1.paste(im2, (x,y)) pastes
# one image (im2) into the first image (im1) starting at the top left
# coordinates (x,y). The first image is changed as a result, but not the
# second one.

#Note that the second image must fit in the first image starting with these
# coordinates; otherwise, the pasted image will be cropped.

#How we call such a function is different:
im1 = Image.open('KonoDioDa.jpg')
print(im1.size)
im = Image.new('RGB', (600, 396*2))
im.paste( im1, (0,0))   ##not assigning the result of paste to a new variable
im.show()
im.paste( im1, (0, 396))
im.show()

#The fact that the function paste changes an image is an implementation
# decision made by the designers of PIL, mostly because images are so large
# and copying is therefore time consuming.

#Later in the semester, we will learn how to write such functions.


"Example 2: Cut and pasting parts of an image"
#This example crops three boxes from an image, creates a new image and pastes
# the boxes at different locations of this new image.

from PIL import Image

im = Image.open("KonoDioDa.jpg")
w,h = im.size

## Crop out three columns from the image
## Note: the crop function returns a new image
part1 = im.crop((0,0,w//3,h))
part2 = im.crop((w//3,0,2*w//3,h))
part3 = im.crop((2*w//3,0,w,h))

## Create a new image
newim = Image.new("RGB",(w,h))

## Paste the image in different order
## Note: the paste function changes the image it is applied to
newim.paste(part3, (0,0))
newim.paste(part1, (w//3,0))
newim.paste(part2, (2*w//3,0))
newim.show()


"SUMMARY"
#Tuples are similar to strings and numbers in many ways. You cannot change a
# part of a tuple. However, unlike other simple data types, tuples allow
# access to the individual components using the indexing notation [ ].
#Modules contain a combination of functions, variables, object definitions,
# and other code, all designed for use in other Python programs and modules
#PILLOW provides a set of modules that define the Image object type and
# associated methods.