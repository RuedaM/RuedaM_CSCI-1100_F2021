#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:53:04 2021

@author: maxrueda

Rueda, Maximillian
10/7/21
CSCI 1100
Homework 3.1 - How complex is the language used in the text?

This code reads a user-inputted paragraph containing multiple English sentences
 as text. The paragraph is read as a single (long) line of text. Based on the
 given paragraph, certain measures corresponding to the overall readability of
 this text will be given.
"""

#Imports:
#The syllables file is imported to allows us to count the syllables in a string/word
#To abbreviate syllables, it will be imported as syl
import syllables as syl


#User Inputs:
#Immediately after getting user input, the string is placed in a new variable
# This new variable is a list that contains all of the words in the input
# Every string added to the list will be added with punctuation included (Ex.: ! ? , -)
Paragraph = input("Enter a paragraph => ")
print(Paragraph)
ParagraphList = Paragraph.split()


#Variables:
#Three totals, the word count, sentence count, and the syllable count, are declared
# Theses are to be added to via the loops below
#Additionally, there is an empty list to which difficult words will be added
WordCount = 0
SenCount = 0
SyllCount = 0
HardWordsList = []


#Main Code:

#Sentence and Word Count:
#This for-loop iterates through a range equivalent to the number of strings in ParagraphList
# Every string in ParagraphList will be added
# If the string contains a . in the [-1] index (the last character in the string), sentence count will increase
for word in range(len(ParagraphList)):
    WordCount += 1
    if (ParagraphList[word][-1] == "."):
        SenCount += 1

#Getting Syllable Count and Adding Hard Words:
#This for-loop iterates through each string (word of the paragraph) in ParagraphList
# Each string will be put through the find_num_syllables() function in the syllables import
# The function returns an integer that will be added to SyllCount
#Afterward, the for-loop looks for the number of words of 3+ syllables
# These 3-syllable words must also not contain a hyphen (-) or end with 'es' or 'ed'.
# If all three conditions are met, the word is added to HardWordsList
for word in ParagraphList:
    SyllCount += syl.find_num_syllables(word)
    
    if (syl.find_num_syllables(word) >= 3):
        if not (word.find("-") > -1):
            if not (word[-2:] == "es") or (word[-2:] == "ed"):
                HardWordsList.append(word)


#Variables To Be Printed:
#Average sentence length (ASL) is found by dividing total word count by total sentence count
#Percent hard words (PHW) is found by dividing the amount of hard words by total amount of words, multiplied by 100
#Average number of syllables (ASYL) is found by dividing total number of syllables by total number of words
##Gunning-Fog and Flesch Kincaid Reading Indexes (GFRI and FKRI respectively) are calculated with the formulas given below
ASL = (WordCount / SenCount)
PHW = ((len(HardWordsList) / WordCount) * 100)
ASYL = (SyllCount / WordCount)
GFRI = (0.4*(ASL + PHW))
FKRI = (206.835-1.015*ASL-86.4*ASYL)
            

#Printed Output:
#The results stored in the above variables are then formatted into the below print statements
# All number values are formatted as floats rounded to 2 decimal places
print("Here are the hard words in this paragraph:\n", HardWordsList)
print("Statistics: ASL:{0:.2f} PHW:{1:.2f}% ASYL:{2:.2f}".format(ASL, PHW, ASYL))
print("Readability index (GFRI): {0:.2f}".format(GFRI))
print("Readability index (FKRI): {0:.2f}".format(FKRI))