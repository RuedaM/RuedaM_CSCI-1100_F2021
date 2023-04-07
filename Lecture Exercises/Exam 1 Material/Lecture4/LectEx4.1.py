#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:07:04 2021

@author: maxrueda

Rueda, Maximillian
9/12/21
CSCI 1100
Lect. Exercises 4.1
"""

"""
Write a program that assigns a string to the variable called phrase and then
 transforms phrase into a hashtag. In other words, all words in phrase are
 capitalized, all spaces are removed, and a # appears in front. Store the
 result in a variable called hashtag. Then print the value of both phrase and
 hashtag. Your program should start with:
  
phrase = 'Things you wish you knew as a freshman'
  
 and the output from the program (using print() function calls) should be:

The phrase "Things you wish you knew as a freshman"
becomes the hashtag "#ThingsYouWishYouKnewAsAFreshman"

 Note that the output includes the quotation marks.
"""


phrase = 'Things you wish you knew as a freshman'
hashtag = ('"#' + phrase.strip('"').title().replace(" ","") + '"')
print('The phrase "'+phrase+'"\nbecomes the hashtag '+hashtag)