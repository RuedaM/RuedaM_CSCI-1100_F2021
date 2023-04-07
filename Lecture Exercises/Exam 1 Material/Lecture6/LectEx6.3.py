#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:22:37 2021

@author: maxrueda

Rueda, Maximillian
9/16/21
CSCI 1100
Lect. Exercises 6.3
"""

"""
So far we have assumed all input to our programs is correct. In practice,
 however, programs must do extensive error checking. Here is a
 slightly-contrived problem to illustrate this:
Write a short program that asks the user to input two numbers where one of
 them must be greater than 10 and the other must be less than or equal to 10.
 It does not matter which is which. If both inputs are greater than 10, the
 program should output the error message “Both are above 10.” If both are less
 than or equal 10, the program should output the message “Both are below 10.”
 If one of the numbers is above 10 and the other is less than or equal to 10,
 no message should be output.
Regardless of any messages, the program should then output the average of the
 two numbers, accurate to 2 decimals. This program must use one if, one elif
 and no else. Note: just like in HW 1, the program should output a value
 immediately after reading it. Also, if you are having problems matching our
 output format, explore the difference between the output of the following two
 lines:

print("{:.2f}".format(112.099))
print(round(112.099, 2))

Here are two examples of how your program might look when run from the
 interpreter:

Enter the first number: 17.1
17.1
Enter the second number: 13.45
13.45
Both are above 10.
Average is 15.28

and

Enter the first number: 4.7
4.7
Enter the second number: 15.5
15.5
Average is 10.10
"""

number1 = input("Enter the first number: ")
print(number1)
number2 = input("Enter the second number: ")
print(number2)
number1 = float(number1)
number2 = float(number2)

if number1 > 10 and number2 > 10:
    print("Both are above 10.")
elif number1 <= 10 and number2 <= 10:
    print("Both are below 10.")

average = (number1 + number2) / 2
print("Average is {0:.2f}".format(average))