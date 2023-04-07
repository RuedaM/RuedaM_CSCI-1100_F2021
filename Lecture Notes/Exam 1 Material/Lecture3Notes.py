#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:57:15 2021

@author: maxrueda
"""

"---Lecture 3 Notes - Python Strings---"


"Strings, Definition and Syntax"
#A string is a sequence of 0 or more characters delimited by single quotes or
# double quotes, whichever you prefer.

print("hello, world.")
print("")

#Strings may be assigned to variables:

VariableString1 = 'Hello'
VariableString2 = "Good-bye"
print(VariableString1, ",", VariableString2)
print("")

#A string that starts with double quotes must end with double quotes, and
# therefore we can have single quotes inside.
#The same goes for the vice versa (starting+ending with singles, doubles
# allowed inside).

StringQuotes1 = 'He said, "Hello, World!"'
StringQuotes2 = "Many single quotes here '''''''  and here ''' but correct."
print(StringQuotes1)
print(StringQuotes2)
print("")

#Ordinarily, strings do not extend across multiple lines, causing an error if
# you try. But, starting and ending a string with triple single-/double-quotes
# tells Python to allow the string to cross multiple lines. Any character
# other than these is allowed inside the string. These are known as Multi-Line
# Strings

MultiLine = """This
is a multi-line
string."""
print(MultiLine)
print("")
print("")


"Escape Characters"
#Inserting a backwards slash (\) in the middle of a string tells Python that
# the next character will have special meaning - this will only work for
# certain characters, most notably:
#\n — end the current line of text and start a new one
#\t — skip to the next “tab stop” in the text. This allows output in columns
#\' — do not interpret the ' as a string delimiter
#\" — do not interpret the " as a string delimiter
#\\ — put a true back-slash character into the string (don't interpret \ as an
#     ecape character')

Escapes1 = "*\t*\n**\t**\n***\t***\n"
Escapes2 = "I said, \"This is a valid string.\""
print(Escapes1)
print(Escapes2)
print("")

#Escape characters can also be used to create multi-line strings:

MultiLineEscape = 'This\nis a multi-line\nstring.'
print(MultiLineEscape)
print("")
print("")
print("")



"String Operations - Concatenation"
#Concatenation: Two (or more) strings may be concatenated to form a new string,
#               either with(out) the + operator.

Concat1 = "Hello"
Concat2 = "World"
print(Concat1 + Concat2)
print(Concat1 + ' ' + Concat2)
print("")


Concat3 = 'Good'
Concat4 = 'Morning'
Concat5 = 'America!'
print(Concat3 + Concat4 + Concat5)

Concat3a = 'Good '
Concat4a = 'Morning '
Concat5a = 'America!'
print(Concat3a + Concat4a + Concat5a)
print("")
print("")


"String Oerations - Replication"
#You can replicate strings by multiplying them by an integer:

Replic = 'Ha'
print(Replic * 10)
print("")
print("")


"String Operations - Functions"
#Python provides many operations for us to use in the form of functions. We
# have already seen print(), but now we are going to look at other functions
# that operate on strings.
#You can compute the length of a string with len().

StringLen = "Hello!"
print(len(StringLen))

#Recall that a string is a collection of characters
#1. Function len() is provided with the value of the string associated with
#   variable s
#2. len calculates the number of characters in the provided string using its
#   own code, code that is built-in to Python.
#3. len returns the calculated integer value (in this case, 6) and this value
#   is sent to the print function, which actually generates the output.

#Example String Functions
#We will look at examples of all of the following later on:
#str() - convert integer/float to a string
#int() - convert a string that is in the form of an integer to an integer
#float() - convert a string that is in the form of a float to a float
print("")
print("")


"The print() Fuction in More Detail"
#Using help(), we can learn more about print():

help(print)
print("")

#We can see that print can take several inputs in addition to varibles+strings

    #print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
#The section sep=' ', for example, can be used as another way to separate 
# different values in a string - by default, this is set to a space:

PrintSep1 = "How"
PrintSep2 = "Are"
PrintSep3 = "You?"
print(PrintSep1, PrintSep2, PrintSep3, sep="--")
print("")

#And the end=' ' segment will change how a string will end - by default, this
# is set to \n:

PrintEnd = "Hello"
print(PrintEnd, end='!!!')

#Towards the end we see a command called flush, which is useful when trying to
# debug. If you are trying to trace your program execution using print, adding
# flush=True as your final argument will give you more accurate results. We
# will talk about this more later.
print("")
print("")
print("")




"User Input"
#Python programs can ask the user for input using the function called input.
#This waits for the user to type a line of input, which Python reads as a
# string. The string below can be converted to an integer or a float (as long
# as it is properly an int/float).

print("Enter a number: ")
Input = float(input())
print('The square of', Input, 'is', Input*Input)

#We can also insert the string right into the input function call:

Input2 = input("Enter a new number: ")
Input2 = float(Input2)
print('The square of', Input2, 'is', Input2*Input2)

#A similar function exists to convert a string to an integer:

Input3 = input("Enter an integer ")
Input3 = int(Input3)

#We will use this idea to modify our area+volume calculator so that the user
# of the program types in the numbers.
#The result is more useful and feels more like a real program (run from the
# command line).



"---SUMMARY---"
#Strings represent character sequences — our third Python type.
#String operations include addition (concatenation) and replication.
#Functions on strings may be used to determine length and to convert back and
# forth to integers and floats.
#Escape sequences change the meaning of special Python characters or make
# certain characters have special meaning.
#Some special characters of note: \n for new line, \t for tab. They are each
# preceded by a backslash (\).
#The print() function offers significant flexibility.
#We can read input using input().




"---Lecture 3 Practice Problems 1---"

'''
1. Which of the following are valid Python strings?:
s1 = '"Hi mom", I said.  "How are you?"'
s2 = '"Hi mom", I said.  '"How are you?"
s3 = '"Hi mom", I said.  '"How are you?"'
s4 = """'Hi mom", I said.  '"How are you?"'"""
s5 = ""I want to be a lion tamer!"'
s6 = "\"Is this a cheese shop?\"\n\t'Yes'\n\t\"We have all kinds!\""
For those that are not valid, what needs to be fixed?
For those that are, what is the output when they are passed to the print
function?


s1, s4, and s6 are valid strings, while the rest are not.

s2 has phrases in doubles quotes with single quotes behind both of them - this
does not enclose the hole phrase, instead precluding "How are you?"
s3 is similar to s2, but the second double-quote phrase has single quotes
around both sides - again, this does nothing to encapsulate that last phrase
s5 is trying to encapsulate the whole phrase with two double-quotes to start
and a double- then single-quote to end which will not do anytihng to close the
string

s1 will print: "Hi mom", I said. "How are you?"
s4 will print: 'Hi mom", I said.  '"How are you?"'
(Even though the quotes are misplaced, as long as it is between the triple
 quotes it will be fine)
s6 will print "Is this a cheese shop?"
                  'Yes'
                  "We have all kinds!"
'''


'''
2. What is the output?
s = "Cats\tare\n\tgood\tsources\n\t\tof\tinternet\tmemes"
s
print(s)


Cats	are
	good	sources
		of	internet	memes
'''


'''
3. What is the output?
print('\\'*4)
print('\\\n'*3)
print('Good-bye')


\\\\
\
\
\
Good-bye
'''


'''
4. Which of the following are legal? For those that are, show what Python
outputs when these are typed directly into the interpreter.
a. 'abc' 'def'
b. 'abc' + 'def'
c. 'abc ' + 'def'
d. x = 'abc'
e. y = 'def'
f. x+y
g. x y
h. s1 = 'abc'*4
i. s1
j. s2 = 'abc '*4
k. print(s2)


g. cannot be printed because there is nothing connecting the two variables such
as a comma or plus sign to note that they should be printed together
a. abcdef
b. abcdef
c. abc def
f. abcdef
i. abcabcabc
k. abc abc abc abc
'''


"---Lecture 3 Practice Problems 2---"

'''
1. What is the output for this Python program?
print(len('George'))
print(len(' Tom  '))
s = """Hi
sis!
"""
print(len(s))


6
6
8
'''


'''
2. Which of the following are legal? For those that are, show what Python
outputs when these are typed directly into the interpreter.
a. 'abc' + str(5)
b. 'abc' * str(5)
c. 'abc' + 5
d. 'abc' * 5
e. 'abc' + 5.0
f. 'abc' + float(5.0)
g. str(3.0) * 3


a., d., and g. are all legal, the rest are not

For b., you cannot multiply two strings
For c., you cannot add an integer value to a string
For e., you cannot add a float value to a string
For f., You cannot add a float value to a string

a. abc5
d. abcabcabcabcabc
g. 3.03.03.0
'''


'''
3. What is the output of the following when the user types 4 when running the
following Python program?
x = input('Enter an integer ==> ')
x = x*2
x = int(x)
x *= 2
print("x is:", x)


The string character 4 will be placed in the variable x, which will then turn
into 44 because of the line x = x*2; the string 44 will then be converted to
an integer which will then be multiplied by 2. The resulting product, 88, will
be printed
'''


'''
4. What is the output when the user types the value 64 when running the
following Python program?
x = int(input('Enter an integer ==> '))
y = x // 10
z = y % 10
print(x, ',', y, z, sep='')


The string 64 will immediately be converted into an integer value, which will
go through whole-number division by 10, resulting in 6. THis quotient is stored
in the new variable y which will be divided by 10 in the next line. The
remainder between these numbers, , will be stored in z. Finally, 64,66 will be
printed.
'''


'''
5. What happens when you do not have the call to the int function?
Write a program that requests an integer from the user as an input and stores
in the variable n. The program should then print n 1’s with 0’s inbetween.
For example if the user input the value 4 then the output should be:
1010101
'''

n = int(input("Give input: "))
print("1" * n, sep='0')