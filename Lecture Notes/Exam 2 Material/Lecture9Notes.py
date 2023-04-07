#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:00:02 2021

@author: maxrueda
"""

"---Lecture 9 Notes - While Loops---"


"Overview"
#Loops are used to access and modify information stored in lists and are used
# to repeat computations many times.
#We construct loops using logical conditions: while-loops - we will
# investigate single and multiple loops

#Reading: Our coverage of loops is in a different order than that of Practical
# Programming. A direct reference for reading material is Section 9.6.


"Part 1: The Basics"
#Loops allow us to repeat a block of code multiple times. This is the basis
# for many sophisticated programming tasks.

#We will see two ways to write loops: using while-loops and for-loops
#In Python, while-loops are more general because you can always write a for-
# loop using a while-loop.
#We will start with while-loops first then see how we can simplify common
# tasks with for loops later.


"Basics of While"
#Our first while loop just counts numbers from 1 to 9, and prints them:
Number=1
while Number<10:
    print(Number)
    Number += 1   ## if you forget this, your program will never end

#General form of a while loop:
"""
block a
while condition:
    block b
block c
"""

#Steps:
#1. Evaluate any code before while (block a)
#2. Evaluate the while loop condition:
#       If it is True, evaluate block b, and then repeat the evaluation of the
#        condition.
#       If it is False, end the loop, and continue with the code after the
#        loop (block c).

#In other words, the cycle of evaluating the condition followed by evaluating
# the block of code continues until the condition evaluates to False.

#An important issue that is sometimes easy to answer and sometimes very hard
# to answer is to know that your loop will always terminate.
print("")
print("")


"Using Loops with Lists"
#Often, we use loops to repeat a specific operation on every element of a list

#We must be careful to create a number that will serve as the index of
# elements of a list. Valid values are: 0 up to (not including) the length of
# list:
co2_levels = [ (2001, 320.03), (2003, 322.16), (2004, 328.07),\
               (2006, 323.91), (2008, 341.47), (2009, 348.92),\
               (2010, 357.29), (2011, 363.77), (2012, 361.51),\
               (2013, 382.47) ]

count=0
while count < len(co2_levels):
    print( "Year:", co2_levels[count][0], \
           "-- CO2 levels:", co2_levels[count][1])
    count += 1
print("")
print("")


"Accumulation of Values"
#Often, we use loops to accumulate some type of information such as adding all
# the values in a list.

#Let’s change the loop to add numbers from 1 to 9:
count=1
total = 0   #Accumulation variable
while count<10:
    total +=count
    count += 1
print(total)
#(Of course you can and should do this with the sum() function, but guess what
# that actually does!)

#Let’s use a loop to add the numbers in a list.
#Now, we will use the numbers the loop generates to index a list.
#So, the loop must generate numbers from 0 to length of the list.
co2_levels = [ (2001, 320.03), (2003, 322.16), (2004, 328.07),\
               (2006, 323.91), (2008, 341.47), (2009, 348.92),\
               (2010, 357.29), (2011, 363.77), (2012, 361.51),\
               (2013, 382.47) ]
count=0
total=0
while count< len(co2_levels):
    total += co2_levels[count][1]
    count += 1

print("Total co2_levels is", total)
print("")
print("")

#Let’s have more interesting examples. Be very careful not to use an
# incorrect index for the list.

#Count the number of CO2 values in the list that are greater than 350.
counter = 0
GreaterThan350Count = 0
while counter < len(co2_levels):
    if co2_levels[counter][1] > 350:
        GreaterThan350Count += 1
    counter += 1
print("The number of values greater than 350 is", GreaterThan350Count)
print("")
print("")

#Calculate and print the percentage change in each measurement year from the
# previous measurement year.
"""ditto"""

#Determine the years in which the CO2 levels dropped compared to the previous
# measurement. Output just these years.
"""ditto"""


"Loops that end on other conditions"
#Here is a while loop to add the non-zero numbers that the user types in.
total = 0
end_found = False

while not end_found:
    x = int( input("Enter an integer to add (0 to end) ==> "))
    if x == 0:
        end_found = True
    else:
        total += x
print(total)
#We will work through this loop by hand in class.
print("")
print("")


"Multiple nested loops"
#Loops and if statements can both be nested which we've seen for if statements
#Here’s an example where we print every pair of values in a list.
#First solution:
L = [2, 21, 12, 8, 5, 31]
i = 0
while i < len(L):
    j = 0
    while j < len(L):
        print(L[i], L[j])
        j += 1
    i += 1
#This solution prints the values from the same pair of indices twice - e.g.
# the pair 21, 12 is printed once when i=1, j=2 and once when i=2, j=1.

#How can we modify it so that we only print each pair once?
#What has to change if we don’t want to print when i==j?

#Finally, we will modify the resulting loop to find the two closest values in
# the list.
print("")
print("")


"---SUMMARY---"
#Loops are especially useful for iterating over a list, accessing its
# contents, and adding or counting the values from a list. This is done in the
# sum() and len() functions of Python.
#Each loop has a stopping condition — the boolean expression in the while
# statement. The loop will end when the condition evaluates to True.
#If the stopping condition is never reached, the loop will become “infinite”.
#Often a counter variable is used. It (a) is given an initial value before the
# loop starts, (b) is incremented (or decremented) once in each loop
# iteration, and (c) is used to stop the loop when it reaches the index of the
# end (or beginning) of the list.
#We will demonstrate a simple way to write these common loops with a for loop
# in the next lecture.





"---Lecture 9 Practice Problems 1---"

'''
1. Write a while loop to count down from 10 to 1, printing the values of the
    loop counting variable i (it could be some other variable name as well).
'''
backcount = 10
while backcount > 0:
    print(backcount)
    backcount -= 1
print("")


'''
2. Modify your loop to print the values in the list co2_levels in reverse
    order.
'''
#Refer to variable co2_levels above:
count=(len(co2_levels) - 1)
while count > 0:
    print( "Year:", co2_levels[count][0], \
           "-- CO2 levels:", co2_levels[count][1])
    count -= 1
print("")
print("")


"---Lecture 9 Practice Problems 2---"

'''
1. Suppose we wanted to print the first, third, fifth, etc. elements in a
    list. Write code to accomplish this.
months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
'''
months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
counter = 0
while counter < len(months):
    print(months[counter])
    counter += 2
print("")

'''
2. Now, use a similar loop code to print a little evergreen tree.
    *
   ***
  *****
 *******
*********
   ***
   ***
'''
counter = 1
spacecounter = 4
while counter < 10:
    print((" " * (spacecounter)) + ("*" * counter) + (" " * (spacecounter)))
    counter += 2
    spacecounter -= 1
print((" " * 3) + ("*" * 3) + (" " * 3))
print((" " * 3) + ("*" * 3) + (" " * 3))


'''
3. Try this later: change your loop to work for any size evergreen.
'''
"""ditto"""