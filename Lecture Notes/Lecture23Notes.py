#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:18:38 2021

@author: maxrueda
"""

"---Lecture 23 Notes - Recursion---"


"Overview"
#When a function calls itself, it is known as a recursive function
#Use of the function call stack allows Python to handle recursive functions
# correctly
#Examples include factorial, Fibonacci, greatest common divisor, flattening a
# list of lists, and mergesort
#We’ll think about how to hand-simulate a recursive function as well as rules
# for writing recursive functions

#Steps to  Recursive Function:
#   1. Function must be able to call itself
#   2. There must be a base case to reach
#   3. There must be a recursive case/step
#   4. Every recursive case must bring the function closer top the base case


"Our First Example"
#Consider the following Python function.
def blast(n):
    if n > 0:
        print(n)
        blast(n-1)
    else:
        print("Blast off!")
    return

#What is the the output from the  following call?
blast(5)
print("")
print("")


"Python’s Call Stack Mechanism"
#The following mechanism helps us understand what is happening:
#Each time the code makes a function call, Python puts information on the
# “call stack”, including:
#   All values of parameters and local variables
#   The location in the code where the function call is being made
#Python then makes the function call, switching execution to the start of the
# called function
#This function in turn can make additional (potentially recursive) function
# calls, adding information to the top of the stack each time
#When a function ends, Python looks at the top of the stack, and:
#   restores the values of the local variables and parameters of the most
#    recent calling function,
#   removes this information from the top of the stack,
#   inserts the returned value of the called function (if any) in the
#    appropriate location of the calling function’s code, and
#   continues execution from the location where the call was made


"Practice Problems to Illustrate This"
#What are the outputs of the following?
def rp1( L, i ):
    if i < len(L):
        print(L[i], end=' ')
        rp1( L, i+1 )
    else:
        print()

def rp2( L, i ):
    if i < len(L):
        rp2( L, i+1 )
        print(L[i], end=' ')
    else:
        print()

L = [ 2, 3, 5, 7, 11 ]
rp1(L, 0)
rp2(L, 0)
print("")
print("")
print("")

#Note that the entirety of list L is not copied to the top of the stack.
#Instead, a reference (an alias) to L is placed on the stack.


"Factorial"
#The factorial function is:
#   n != n(n−1)(n−2)⋯1 and 0 != 1

#This is an imprecise definition because the … is not formally defined
#Writing this recursively helps to clear it up:
#   n != n⋅(n−1)! and 0 !=1

#The factorial is now defined in terms of itself, but on a smaller number!
#Note how this definition now has a recursive part and a non-recursive part:
#The non-recursive part is called the base case. There must be at least one
# base case in every recursive function definition


"Exploring Factorial"
#We will:
#Write a recursive Python function to implement n!
#Hand-simulate the call stack for n=4
#We’ll add output code to the implementation to help visualize the recursive
# calls in a different way


"Guidelines for Writing Recursive Functions"
#1. Define the problem you are trying to solve in terms of smaller / simpler
#    instances of the problem. This includes:
#       What needs to happen before making a recursive call?
#       What recursive call(s) must be made?
#2. What needs to happen to combine or generate results after the recursive
#    call (or calls) ends?
#3. Define the base case or cases

#Make sure the code is proceeding toward the base case in every step.


"Fibonacci"
#The Fibonacci sequence starts with the values 0 and 1.
#Each new value in the sequence is obtained by adding the two previous values:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …

#Recursively, the nth value, f(n), of the sequence is defined as
#f(n) = f(n−1) + f(n−2)
#This leads naturally to a recursive function…
def fib(n):
    if (n < 0):
        return
    elif (n == 1):
        return 0
    elif (n == 2):
        return 1
    else:
        return (fib(n-1) + fib(n-2))

print(fib(9))
print("")
print("")


"Dangers of Recursion"
#Some recursive function implementations contain wasteful repeated computation
#Recursive function calls, like any function calls, typically involve hidden
# overhead costs
#Often, therefore, a recursive function can (and should) be replaced with a
# non-recursive, iterative function that is significantly more efficient
#This is easy to do for both Factorial and Fibonacci, as we will see in class


"Why, Then, Do We Study Recursion?"
#Many of our definitions and even, our logical structures (such as lists), are
# formalized using recursion
#Sometimes recursive functions are the first ones we come up with and the
# easiest to write (at least after you are comfortable with recursion)
#Only later do we write non-recursive versions
#Sometimes on harder problems it is difficult to even write non-recursive
# functions! The list flattening problem below is one such example


"Advanced Examples"
#We’ll spend the rest of class on three more advanced examples:
#Recursive geometric shapes: the Sierpinski triangle
#Flattening a nested list
#A recursive version of merge sort
#Recursive Geometric Shapes

#Fractals are often defined using recursion. How can we draw, for example, a
# Sierpinski triangle?

#We will look at this example in class and attempt to define the recursion.

#To aid us, we’ll look at a Tkinter Python program that implements the drawing
# of the Sierpinski triangle:
"""
Example program shows the use of recursion to create fractals, 
in this case, the Sierpinski Triangle. See function:

draw_triangles

for the recursion. The rest is TkInter program allowing the
user to change properties of the Sierpinski triangle drawn.

"""


from tkinter import *
import math

class MyApp(object):
    def __init__(self, parent):
        ##Function local to init to simplify repetitive button creation process
        def put_button(parent, name, functionname, placement):
            newbutton = Button(parent, text=name, command=functionname)
            newbutton.pack(side=placement)
            newbutton.configure(width=button_width,\
                                padx=button_padx, pady=button_pady )
            return newbutton
        
        ## constants used  in the initialization
        button_width = 10
        button_padx = "3m"
        button_pady = "3m"

        ## variables used in the program
        self.maxlevel = 6
        self.size = 600  #3**self.maxlevel
        self.maxy = int(self.size*math.sqrt(3)/2)
        self.stopped = False
        self.depth = 2
        self.wait_time = 1
        self.parent = parent
        
        ## interface elements
        ## all frames
        self.main_frame = Frame(parent)
        self.main_frame.pack()
        self.top_frame = Frame(self.main_frame)
        self.top_frame.pack(side=TOP)
        self.bottom_frame = Frame(self.main_frame)
        self.bottom_frame.pack(side=BOTTOM)

        ## canvases: top for info, buttom for drawing Triangles
        self.infocanvas = Canvas(self.top_frame, \
                                 width=self.size, height=30)
        self.infocanvas.pack(side=TOP)
        self.text_area = self.infocanvas.create_text(30,10,anchor='nw')
        self.canvas = Canvas(self.top_frame, \
                             width=self.size, height=self.maxy)
        self.canvas.pack(side=BOTTOM)

        ## buttons: for controlling the program
        self.drawbutton = put_button(self.bottom_frame, 'Draw', self.draw, LEFT)
        self.clearbutton = put_button(self.bottom_frame, 'Clear', self.clear, LEFT)
        self.fasterbutton = put_button(self.bottom_frame, \
                                         "Faster", self.faster, LEFT)
        self.slowerbutton = put_button(self.bottom_frame, \
                                         "Slower", self.slower, LEFT)
        self.increasebutton = put_button(self.bottom_frame, \
                                         "Depth+1", self.increase, LEFT)
        self.decreasebutton = put_button(self.bottom_frame, \
                                         "Depth-1", self.decrease, LEFT)
        self.quitbutton = put_button(self.bottom_frame, \
                                     "Quit", self.quit, RIGHT)
        ## display settings for the program on the info canvas
        self.put_info()

    def put_info(self):
        """ Function for displaying the settings for the program, 
            depth and wait time for the animation effect.

        """
        
        info = "Wait time: %d ms" %(self.wait_time)
        if self.depth == self.maxlevel+3:
            info += " "*10+ "Depth: %d (max level reached)" %self.depth 
        elif self.depth == 0:
            info += " "*10+ "Depth: 0 (min level reached)"
        else:
            info += " "*10+ "Depth: %d" %self.depth
        self.infocanvas.itemconfigure(self.text_area, text=info)

    def clear(self):
        """ Clear the drawing (used in self.clearbutton). """
        self.canvas.delete("all")
        
    def faster(self):
        """ Make the animation faster (used in self.fasterbutton). """
        self.wait_time //= 2
        if self.wait_time <= 0:
            self.wait_time = 1
        self.put_info()

    def slower(self):
        """ Make the animation slower (used in self.slowerbutton). """
        self.wait_time *= 2
        self.put_info()
        
    def increase(self):
        """ Increases the depth for recursion (used in self.fasterbutton). """
        if self.depth < self.maxlevel+3: 
            self.depth += 1
            self.put_info()
        
    def decrease(self):
        """ Decreases the depth for recursion (used in self.slowerbutton). """
        if self.depth > 0:
            self.depth -= 1
            self.put_info()
            
    def draw(self):
        """ Clear the canvas and draws the Sierpinksi triangles (used in self.drawbutton). """
        padding = 20 ##just leave some space off the corners
        if not self.stopped:
            self.clear()
            self.draw_triangles(0+padding,self.maxy-padding,self.size-2*padding, 1)
            
    def draw_triangles(self, x, y, length, depth):
        """ Draws two triangles: one with x,y as the bottom left corner,
            in red and a second inverted one inside between the midpoints
            of the outside triangle, in white.

        """
        ## Triangle 1: Outside Triangle
        mid = length/2
        self.canvas.create_polygon(x, y, \
                                   x+length, y, \
                                   x+mid, y-math.sqrt(3)*mid,\
                                   fill = "red")
            
        if depth <= self.depth:
            ## Triangle 2: Inside Triangle
            leftmid = ( x+(mid)/2, y-(math.sqrt(3)*mid)/2 )
            rightmid = (  x+(length+mid)/2, y-(math.sqrt(3)*mid)/2 )
            bottommid = ( x+mid, y )
            
            self.canvas.create_polygon( leftmid[0], leftmid[1], \
                                        rightmid[0], rightmid[1], \
                                        bottommid[0], bottommid[1], \
                                        fill = "white" )
            self.draw_triangles(x, y, length/2, depth+1)
            self.draw_triangles(leftmid[0], leftmid[1], length/2, depth+1)
            self.draw_triangles(x+length/2, y, length/2, depth+1)
            ## Add animation effect
            self.canvas.update()
            self.canvas.after(self.wait_time)
            
    def quit(self):
        self.stopped = True
        self.parent.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("Recursion Example with Sierpinski Triangles")
    myApp = MyApp(root)
    root.mainloop()


"Flattening a Nested List"
#Suppose we want to take a list such as:
v = [[1,5], 6, [[2]], [3, [7, 8, [9,10], [11,12] ]]]

#...and “flatten” it, converting it to just a list of values with no sublists.
v = [ 1, 5, 6, 2, 3, 7, 8, 9, 10, 11, 12 ]

#This is challenging because we don’t know when we write a function to solve
# this problem how “deep” the nesting of sublists goes. The solution should
# handle arbitrary depths:
#   Many, many data structures (containers) in computer science have this type
#    of nested / recursive structure: an entry in a list may be another list…
#To solve this problem we will also need to know how to recognize when an
# entry in a list is another list. For this we need to use the type function
# in Python. The following example should make this clear:
v = [ 'a', 'b', 'c']
x = 12
print(type(v) == list)
print(type(v[0]) == list)
print(type(x) == int)
print("")
print("")

#Now we are ready to solve the “flattening” problem. We’ll look at two
# different approaches. In both, the key will be to distinguish between
# handling elements that are lists (and therefore must be flattened
# recursively) and elements that are not lists:
def flatten(L):
    result = []
    for x in L:
        if type(x) == list:
            result.extend( flatten(x) )
        else:
            result.append(x)
    return result

def flatten2(L):
    if type(L) != list:
        return [L]
    else:
        result = []
        for x in L:
            result.extend( flatten2(x) )
        return result


v = [[1,5], 6, [[2]], [3, [7, 8, [9,10], [11,12] ]]]
print(v)
print(flatten(v))
print(flatten2(v))
print("")
print("")


"Final Example: Merge Sort"
#The fundamental idea of merge sort is recursive:
#   Any list of length 1 is sorted
#   Otherwise:
#       Split the list in half
#       Recursively sort each half
#       Merge the resulting sorted halves

#We repeat our use of the merge function from Lecture 20:
import time
import random

def time_function(L, func):
    """ Illustrates how you can send a function as an argument
    to another function as well. Runs the function called func,
    and returns the time.

    """

    L1 = list(L)
    start = time.time()
    func(L1)
    end = time.time()
    print("Method: {:s} took {:f} seconds".format((func.__name__).ljust(20), end-start))

def merge(L1, L2):
    """ Assume L1 and L2 are sorted.
    Create a new list L that is the merged
    version of L1&L2.
    
    This is the efficient version of merge
    that does not modify the input lists, as pop 
    is costly, even though it is a constant time operation.

    """
    
    L = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            val = L1[i]
            L.append( val )
            i += 1
        else:
            val = L2[j]
            L.append( val )
            j += 1
    ## at this point, either L1 or L2 has run out of values
    ## add all the remaining values to the end of L.
    L.extend(L1[i:]) 
    L.extend(L2[j:])
    return L


    
def merge_sort_iterative(L):
    """ Complexity: O(n* log n)
        See earlier version of this code for explanation.

    """

    L1 = []
    for val in L:
        L1.append( [val] )
    
    while len(L1) > 1:
        L2 = []
        for i in range(0, len(L1)-1, 2):
            Lmerged = merge( L1[i], L1[i+1] )
            L2.append( Lmerged )
            
        if len(L1)%2 == 1:
            L2.append( L1[-1] )
        L1 = L2
    return L1[0]


def merge_sort_recursive(L):
    """ Complexity: O(n logn)
        The function calls itself recursively logn times,
        and each time about n elements are merged.

    """
    if len(L) == 1:
        return L
    
    length = len(L)
    mid = length // 2
    left = merge_sort_recursive(L[:mid])
    right = merge_sort_recursive(L[mid:])
    return merge(left,  right)


##Testing code
k = 100000
L = list(range(k))
random.shuffle(L)

time_function( L, merge_sort_iterative )
time_function( L, merge_sort_recursive )
time_function( L, list.sort )


#Comparing what we write to our earlier non-recursive version of merge sort
# shows that the primary job of the recursion is to organize the merging
# process!


"---SUMMARY---"
#Functions that call themselves are known as “recursive functions”
#Use of a function call stack allows Python to handle recursive functions
# correctly
#Many structures and functions important to computer science are defined
# recursively
#Fundamentally, recursion is about defining a problem solution as a function
# of the solution to a simpler/shorter/smaller version of the problem
#A basis case (or cases) is (are) always needed to make a recursion function
# succeed
#Infinite recursion is avoided by ensuring that progress is made toward the
# basis case or cases in every recursive call
#While many recursive functions are easily rewritten to remove the recursion,
# some advanced problems are difficult to solve without recursion