#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:42:44 2021

@author: maxrueda

Rueda, Maximillian
10/14/21
CSCI 1100
Homework 4.1 - Password Strength

This code implements a few simple strength judgment rules and then evaluates
 a score to determine if a user-inputted password is to be rejected or rated
 poor, fair, good or excellent.
"""

#Imports:
#hw4_util file contains functions that allows us to properly complete the code
# For Part 1, the function part1_get_top() is used to return a list of the top
#  100 most common passwords
# To abbreviate the title, it will be imported as util
import hw4_util as util



#User-Defined Functions:

#Password Length:
#This function simply returns a score based on the length of the password
# If the password is shorter than six characters, the function returns a score 0
def length(password):
    lengthScore = 0
    
    if (len(password) == 6) or (len(password) == 7):
        lengthScore += 1
    elif (len(password) >= 8) and (len(password) <= 10):
        lengthScore += 2
    elif (len(password) > 10):
        lengthScore += 3
    
    return lengthScore


#Password Cases:
#This function returns a score based on the amount of uppercase and lowercase
# letters in the password
# If there is at least 1 uppercase and 1 lowercase letter, a score 1 is returned
# If there is at least 2 uppercase and 2 lowercase letters, a score 2 is returned
# If not, 0 score is returned
def case(password):
    caseScore = 0
    lowercaseCounter = 0
    uppercaseCounter = 0

    for letter in password:
        if (letter.islower() == True):
            lowercaseCounter += 1
        elif (letter.isupper() == True):
            uppercaseCounter += 1

    if (uppercaseCounter >= 1) and (lowercaseCounter >= 1):
        if (uppercaseCounter >= 2) and (lowercaseCounter >= 2):
            caseScore += 2
        elif (uppercaseCounter >= 2) or (lowercaseCounter >= 2):
            caseScore += 1
    
    return caseScore
    

#Password Digits:
#This function returns a score based on the amount of digits in the password
# If there is at least 1 digit, a score 1 is returned
# If there is at least 2 digits, a score 2 is returned
# If not, 0 score is returned
def digits(password):
    digitScore = 0
    digitCounter = 0
    
    for character in password:
        if (character.isdigit() == True):
            digitCounter += 1
        
    if (digitCounter >= 1):
        digitScore += 1
        if (digitCounter >= 2):
            digitScore += 1
    
    return digitScore
    

#Password Punctuation:
#This function returns a score based on the amount and type of punctuation in
# the password
# Punctuation is split in to two categories, one of !@#$ or %^&*
# If there is at least one of !@#$ or %^&*, a score 1 will be returned
# If there are at least one of both !@#$ and %^&*, a score of 2 will be returned
# If not, 0 score is returned
#This function also returns the category of punctuation, either !@#$ or %^&*
# depending on what is found in the password
def punctuation(password):
    punctScore = 0
    punctCounter1 = 0
    punctCounter2 = 0
    
    for char in password:
        if (char == "!") or (char == "@") or (char == "#") or (char == "$"):
            punctCounter1 += 1
        elif (char == "%") or (char == "^") or (char == "&") or (char == "*"):
            punctCounter2 += 1
        
    if (punctCounter1 >= 1) and (punctCounter2 >= 1):
        punctScore1 = 1
        punctScore2 = 1
        return "!@#$", "%^&*", punctScore1, punctScore2
    elif (punctCounter1 >= 1) and (punctCounter2 == 0):
        punctScore += 1
        return "!@#$", punctScore
    elif (punctCounter1 == 0) and (punctCounter2 >= 1):
        punctScore += 1
        return "%^&*", punctScore
    else:
        return punctScore
    

#Password Liceneses:
#This function returns a score based on if the password matches a potential
# license plate
# If the password at any point contains 3 consecutive letters followed by 4
#  consecutive numbers, there is a possibility that the password matches a
#  license plate, and a score of -2 will be returned
# If not, 0 score is returned
def licenses(pswrd):
    licenseScore = 0
    
    pswrd = pswrd.lower()
    if (len(pswrd) >= 7):
        for char in range(len(pswrd)-6):
            if (pswrd[char].isalpha() == True) and (pswrd[char+1].isalpha() == True) \
            and (pswrd[char+2].isalpha() == True):
                if (pswrd[char+3].isdigit() == True) and (pswrd[char+4].isdigit() == True) \
               and (pswrd[char+5].isdigit() == True) and (pswrd[char+6].isdigit() == True):
                    licenseScore = -2
                    return licenseScore
    
    return licenseScore
    

#Password Matching to Common Passowrd:
#This function returns a score based on if the password matches any of the top
# 100 most common passwords
# If the lowercase version of the password matches any of the top 100 most common,
# a score of -3 will be returned
# If not, 0 score is returned
def common(password):
    commonScore = 0
    
    for commPass in util.part1_get_top():
        if commPass == password.lower():
            commonScore = -3
    
    return commonScore



#Main Code:

#Main Code Checkpoint:
#This if-statement ensures that the code being run currently is the main code
# If this file is the main code, the following code will be run normally
# If this file is not the main code and is instead being used for the functions
#  contained within it, this part of the code downwards will not run
#This comment will only appear for this specific code - going forward, this
# will be standard
if __name__ == "__main__":
    
    
    #User Input:
    #Immediately after getting user input, the string is placed in a new variable
    # password will remain a string
    password = input("Enter a password => ")
    print(password)
    password = password.strip("\r")
    
    #Variables:
    #6 variables representing scores are declared
    # Stored in these variables are the scores based on the above functions'
    # calculations
    lengthScore = length(password)
    caseScore = case(password)
    digitScore = digits(password)
    punctuationTuple = punctuation(password)
    licenseScore = licenses(password)
    commonScore = common(password)
    
    #Because the varaible punctuationTuple can return a tuple or an int, this
    # part of the code was made to store all possible tuple values into separate
    # variables
    #If punctuationTuple is not a tuple and is instead the int 0, this will
    # not be read
    if (type(punctuationTuple) == tuple):
        if (len(punctuationTuple) == 4):
            punctLabel1 = punctuationTuple[0]
            punctLabel2 = punctuationTuple[1]
            punctScore1 = punctuationTuple[2]
            punctScore2 = punctuationTuple[3]
        elif (len(punctuationTuple) == 2):
            punctLabel = punctuationTuple[0]
            punctScore = punctuationTuple[1]
    
    
    #Printed Output:
    
    #Printed Scores:
    #All of the above variables are formatted into strings that are to be printed
    # If the variable is zero, i.e. the password did not receive a score based
    #  on a paramenter, the string is not printed
    #Again, if the variable punctuationTuple is in fact a tuple, specific print
    # statements are made
    # If the password has punctuation from both !@#$ and %^&*, both scores and
    #  labels are printed - if it has only one from one category, only that
    #  label and score are printed
    if (lengthScore > 0):
        print("Length: +{}".format(lengthScore))
    if (caseScore > 0):
        print("Cases: +{}".format(caseScore))
    if (digitScore > 0):
        print("Digits: +{}".format(digitScore))
    if (type(punctuationTuple) == tuple):
        if (len(punctuationTuple) == 4):
            print("{}: +{}".format(punctLabel1, punctScore1))
            print("{}: +{}".format(punctLabel2, punctScore2))
        elif (len(punctuationTuple) == 2):
            print("{}: +{}".format(punctLabel, punctScore))
    if (abs(licenseScore) > 0):
        print("License: {}".format(licenseScore))
    if (abs(commonScore) > 0):
        print("Common: {}".format(commonScore))
    
    
    #Combined Score:
    #The combined score is calculated and printed
    #Both punctuation scores are added if the password has punctuation from
    # both !@#$ and %^&*
    #A single punctuation score is added if the password has punctuation from
    # either !@#$ or %^&*
    #No punctuation score is added if punctuatino score is the int 0
    if (type(punctuationTuple) == tuple):
        if (len(punctuationTuple) == 4):
            combinedScore = lengthScore + caseScore + digitScore + punctScore1 \
                          + punctScore2 + licenseScore + commonScore
            print("Combined score: {}".format(combinedScore))
        elif (len(punctuationTuple) == 2):
            combinedScore = lengthScore + caseScore + digitScore \
                          + punctScore + licenseScore + commonScore
            print("Combined score: {}".format(combinedScore))
    else:
        combinedScore = lengthScore + caseScore + digitScore \
                      + licenseScore + commonScore
        print("Combined score: {}".format(combinedScore))
    
    
    #Password Evaluation:
    #Based on the combined score value, certain outputs are printed
    if (combinedScore <= 0):
        print("Password is rejected")
    elif (combinedScore == 1) or (combinedScore == 2):
        print("Password is poor")
    elif (combinedScore == 3) or (combinedScore == 4):
        print("Password is fair")
    elif (combinedScore == 5) or (combinedScore == 6):
        print("Password is good")
    elif (combinedScore >= 7):
        print("Password is excellent")