#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 13:03:17 2021

@author: maxrueda
"""

"---Lecture 12 - Controlling Loops---"

"Restatement of the Basics"
#for-loops tend to have a fixed number of iterations computed at the start of
# the loop
#while-loops tend to have an indefinite termination, determined by the
# conditions of the data
#Most Python for loops are easily rewritten as while loops, but not vice-versa
#In other programming languages, for and while are almost interchangeable, at
# least in principle.


"Overview"
#Ranges and control of loop iterations
#Nested loops
#Lists of lists
#Contolling loops through break and continue
#Reading: Practical Programming, rest of Chapter 9.


"Part 1: Ranges and For-Loops — A Review"
#A range is a function to generate a sequence of integers:
for i in range(10):
    print(i)
print("")
#This would the digits 0 through 9 in succession, one per line.
#   (Remember that this is up to and not including the end value specified!)

#A range is not quite a list — it generates values for each successive
# iteration of a for-loop.
#For now, we will convert each range to a list as the basis for studying them

#If we want to start with something other than 0, we provide two integer
# values:
print(list(range(3,8)))

#With a third integer value, we can create increments:
print(list(range(4,20,3)))
#This list starts at 4, increments by 3, stops when 20 is reached/surpassed

#We can ALSO create backwards increments
print(list(range(-1, -10, -1)))


#Remembering the parameters for range(): Start, Stop, Step
#   Start - what number do we start with and include
#   Stop - what is the number we stop before: if we stop at 5, it ends at 4
#   Step - How much we should step/increment/decrement by
print("")
print("")


"Using Ranges in For Loops"
#We can use the range to generate the sequence of loop variable values in a
# for-loop. Our first example is printing the contents of the planets list:
planets = [ 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter',
    'Saturn', 'Uranus', 'Neptune', 'Pluto' ]
for i in range(len(planets)):
    print(planets[i])
print("")
#   (In this case we don’t need a index variable - we can just iterate over
#    the values in the list.)

#The variable i is variously known as the index or the loop index variable or
# the subscript.

#Modify the loop to do the following:

#Print the indices of the planets starting at 1:
for i in range(len(planets)):
    print(i+1)
#The range stays the same, the output will be changed - i starts at 0, so add 1
print("")

#Print the planets backward:
for i in range(-1,-(len(planets)+1), -1):
    print(planets[i])
#Start at index -1, go until the first index (in the opposite direction), and
# decrement by 1
print("")

#Print every other planet:
for i in range(0,len(planets),2):
    print(planets[i])
#Start at 0th index, go until the end of the list (len(list)), increment by 2
print("")
print("")


"Loops That Do Not Iterate Over All Indices"
#Sometimes the loop index should not go over the entire range of indices, and
# we need to think about where to stop it early, as the next example shows.

#Example: Returning to our example from Lecture 1, we will briefly re-examine
# our solution to the following problem: Given a string, how can we write a
# function that decides if it has three consecutive double letters?
def has_three_doubles(s):
    for i in range(0, len(s)-5):
        if s[i] == s[i+1] and s[i+2] == s[i+3] and s[i+4] == s[i+5]:
            return True
    return False
print(has_three_doubles("aabbcc"))
print(has_three_doubles("abbcc"))
print(has_three_doubles("xaaybbzcc"))
print(has_three_doubles("xyzaabbcc"))

#We have to think carefully about where to start our looping and where to stop
#Notice how the range only goes up to len(s)-5; this is because the for-loop
# will technically only need to read the 0th index, otherwise the loop wil go
# through the other indices (that don't exist) and go out of the range; we
# restrict the index to NOT read the last 5 characters of a string


#Refer back to Lecture 10 for further examples
print("")
print("")
print("")

"Part 2: Nested Loops"
#Some problems require iterating over either:
#   - two dimensions of data, or
#   - all pairs of values from a list

#As an example, here is code to print all of the products of digits:
digits = range(10)

for i in digits:
    for j in digits:
        print("{} x {} = {}".format(i,j,i*j))
#How does this work?
#   For each value of i the variable in the first, or “outer”, loop, Python
#    executes the entire second, or inner, loop
#   More importantly, i stays fixed during the entire inner loop.

#We will look at finding the two closest points in a list.
print("")
print("")


"Example: Finding the Two Closest Points"
#Suppose we are given a list of point locations in two dimensions, where each
# point is a tuple. For example:
points = [ (1,5), (13.5, 9), (10, 5), (8, 2), (16,3) ]

#Our problem is to find the two points that are closest to each other.
#   (We started working on a slightly simpler version of this problem at the
#    end of Lecture 10.)

#The natural idea is to compute the distance between any two points and find
# the minimum - We can do this with and without using a list of distances
import math

def distance(tuple1, tuple2):
    return math.sqrt(((tuple2[0]-tuple1[0])**2) + ((tuple2[1]-tuple1[1])**2))

def approach_1(pointsList):
    distanceList = []
    for i in range(len(pointsList)):
        for j in range(i+1, len(pointsList)):
            distanceList.append([distance(pointsList[i], pointsList[j]), i, j])
    return min(distanceList)


def approach_2(pointsList):
    smallest = distance(pointsList[0], pointsList[1])
    i1 = 0
    i2 = 1
    for i in range(len(pointsList)):
        for j in range(i+1, len(pointsList)):
            dist = distance(pointsList[i], pointsList[j])
            if dist < smallest:
                smallest = dist
                i1 = i
                i2 = j
    return smallest, i1, i2

cp = approach_1(points)
print("Closest dist. of {:.2f} is between points {} and {}".format(cp[0], points[cp[1]], points[cp[2]]))
cp = approach_2(points)
print("Closest dist. of {:.2f} is between points {} and {}".format(cp[0], points[cp[1]], points[cp[2]]))
print("")
print("")
print("")



"Part 3: Lists of Lists"
#In programming you often must deal with data much more complicated than a
# single list. For example, we might have a list of lists, where each list
# might be temperature (or pH) measurements at one location of a study site:
temps_at_sites = [ [ 12.12, 13.25, 11.17, 10.4],
                   [ 22.1, 29.3, 25.3, 20.2, 26.4, 24.3 ],
                   [ 18.3, 17.9, 24.3, 27.2, 21.7, 22.2 ],
                   [ 12.4, 12.5, 12.14, 14.4, 15.2 ] ]

#Here is code to find the site with the maximum average temperature; note that
# no indices are used:
averages = []
for site in temps_at_sites:
    avg = sum(site) / len(site)
    averages.append(avg)

max_avg = max(averages)
max_index = averages.index(max_avg)
print("Maximum average of {:.2f} occurs at site {}".format(max_avg, max_index))

#Notes:
#for-loop variable site is an alias for each successive list in temps_at_sites
#A separate list is created to store the computed averages

#We will see in class how this would be written without the separate averages
# list.
print("")
print("")
print("")



"Part 4: Controlling Execution of Loops"
#We can control loops through use of break and continue
#We need to be careful to avoid infinite loops


"Using a Break"
#We can terminate a loop immediately upon seeing the 0 using Python’s break:
sum = 0
while True:
    x = int(input("Enter an integer to add (0 to end) ==> "))
    if x == 0:
        break
    sum += x

print(sum)
#break sends the flow of control immediately to the first line of code outside
# the current loop, and the while condition of True essentially means that the
# only way to stop the loop is when the condition that triggers the break is
# met.

#This is similar to the booleanFlag method of stopping a while-loop, but this
# can be used in local areas, not just entire while-loops
print("")
print("")


"Continue: Skipping the Rest of a Loop Iteration"
#Suppose we want to skip over negative entries in a list. We can do this by
# telling Python to continue when the loop variable, taken from the list, is
# negative:

myList = [0, 2, -3, -5, 9, 25, -36, 1]
for item in myList:
    if item < 0:
        continue
    print(item)

#When it sees continue, Python immediate goes back to the “top” of the loop,
# skipping the rest of the code, and initiates the next iteration of the loop
# with a new value for item.

#Any loop that uses break or continue can be rewritten without either (i.e.
# the boolanFlag); therefore, we choose to use them only if they make our code
# clearer - A loop with more than one continue or break is rarely
# well-structured, so if you find that you have written such a loop you should
# stop and rewrite your code.

#The example above, while illustrative, is probably better w/out continue - 
# Usually when we use continue the rest of the loop is relatively long. The
# condition that triggers the continue is tested at/near the top of the loop
print("")
print("")


"Termination of a While-Loop"
#When working with a while loop one always needs to ensure that the loop will
# terminate, otherwise we have an infinite loop

#Sometimes it is easy to decide if a loop will terminate - sometimes it isn't
#Below, both loops repeatedly take the square root of a user-inputted number
# until the value reaches 1

#Do either of the following examples cause an infinite loop?

x = float(input("Enter a positive number -> "))
while x > 1:
    x = math.sqrt(x)
    print(x, flush=True)
"""
x = float(input("Enter a positive number -> "))
while x >= 1:
    x = math.sqrt(x)
    print(x, flush=True)
"""
#2nd loop would cause infinite printing
#The first will continue to take the square root until eventually equals 1
# (which all looping sqrt functions do) when it does, it will end since 1 does
# not meet the condition x > 1
#However, in the 2nd loop, the parameter is x >= 1, and 1 IS >= 1: the loop 
# will, after the true calculations, will continually take the sqrt of 1 w/out
# stopping, whhich is an infinite loop
print("")
print("")
print("")



"---SUMMARY---"
#range is used to generate a sequence of indices in a for loop.
#Nested for loops may be needed to iterate over two dimensions of data.
#Lists of lists may be used to specify more complex data. We process these
# using a combination of for loops, which may need to be nested, and Python’s
# built-in functions. Use of Python’s built-in functions, as illustrated in
# the example here in these notes, is often preferred.
#Loops (either for or while) may be controlled using continue to skip the rest
# of a loop iteration and using break to terminate the loop altogether. These
# should be used sparingly!






"Part 1 Practice"

"""
1. Generate a range for the positive integers less than 100. Use this to
    calculate the sum of these values, with and without (i.e. use sum) a
    for-loop.
"""
range100 = range(1,100) #Staring number can either be 1 or 0 for this



#OPTION A - with for-loop
forSum100 = 0
for number in range100:
    forSum100 += number
print(forSum100)

#OPTION B - without for-loop
#THIS SHOULD WORK - I DON'T KNOW WHY IT DOESN'T
#sum100 = sum(range100)
#print(sum100)
print("")

"""
2. Use a range and a for-loop to print the positive, even numbers less than
    the integer value associated with n.
"""
n = int(input("Give integer: "))
for x in range(2, n, 2):
    print(x)
print("")

"""
3. Suppose we want a list of the squares of the digits 0 to 9. The following
    does NOT work:
squares = list(range(10))
for s in squares:
    s = s*s
    
    Why not? Write a different for loop that uses indexing into the squares
    list to accomplish our goal.
"""
#There is no list that is being appended to in the first place
numbers = list(range(10))
squares = []
for i in numbers:
    squares.append(i*i)
print(squares)
print("")

"""
4. The following code for finding out if a word has two consecutive double
    letters is wrong. Why? When, specifically, does it fail?
def has_two_doubles(s):
    for i in range(0, len(s)-5):
        if s[i] == s[i+1] and s[i+2] == s[i+3]:
            return True
    return False
"""
#The range is wrong - the smallest string possible for this function has a
# length of 4, so we should restrict the range accordingly, only scanning from
# the fisrt letter up to the 4th to last letter of the string
def has_two_doubles(s):
    for i in range(0, len(s)-3):
        print(s[i])
        if s[i] == s[i+1] and s[i+2] == s[i+3]:
            return True
    return False
print(has_two_doubles("xyaabb"))