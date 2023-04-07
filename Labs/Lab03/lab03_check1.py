"""
This program experiments with the use of functions
and also learning error checking.
"""

## Math is imported in order to use the function math.sqrt()
import math


### This function returns the length of a line starting at (x1,y1) and ending at (x2,y2)
## The differences between the two x values and y values are each squared and added to each other
## That sum is then put under a square root, returning the length between the two points
def line_length(x1,y1,x2,y2):
    length = (x1-x2)**2 + (y1-y2)**2
    length = math.sqrt(length)
    return length
## The function returns the length and will be stored into an integer later on


initial_x = 10
initial_y = 10
next_x = input("The next x value ==> ")
print(next_x)
next_y = input("The next y value ==> ")
print(next_y)

next_x = int(next_x)
next_y = int(next_y)
## The program has the first point set as (10,10)
### The program asks for two new values which will be the coordinates of the next point
## The inputs, which were strings, are converted into integers to be used in calculations
# As per the class' rules, the inputs are immediately printed after being asked for


print("The line has moved from ({:d},{:d})".format(initial_x, initial_y),\
       "to ({:d},{:d})".format(next_x, next_y))
## All four values are then printed in a formatted statement

    
length = line_length(initial_x, initial_y, next_x, next_y)
print("Total length traveled is:", round(length, 2))
### The value returned by line_length() is stored in the variable called length
## Length is printed with the sring and is rounded to two decimal places with Python's built-in round() function