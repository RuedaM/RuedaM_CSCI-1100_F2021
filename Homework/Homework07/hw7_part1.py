#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 08:56:15 2021

@author: maxrueda

Rueda, Maximillian
11/11/21
CSCI 1100
Homework 7.1 - Autocorrect

This code takes in user inputs and performs a small version of autocorrect
 that looks for a few common typographical errors. These errors are counted,
 and possible replacements are given. To accomplish this, the code takes files
 that give necessary information and words to test on.

words_10percent.txt
input_words.txt
keyboard.txt
"""



#User-Defined Functions:

#Main Dictionary Creation:
#A dictionary of correctly-spelled English words (like a real English
# dictionary) is created with the word's lexicon frequency as a value of each
# word
def true_dict_creation(dictFileName):
    dictFile = open(dictFileName)
    trueDict = dict()
    
    for line in dictFile:
        lineList = line.strip().split(",")
        trueDict[lineList[0].strip()] = lineList[1]
    
    dictFile.close()
    return trueDict


#Keyboard Dictionary Creation:
#A dictionary of all letters of the alphabet is created with lists of all
# neighboring letters (according to a qwerty keyboard) as each letter's value
def keyboard_dict_creation(kbFileName):
    kbFile = open(kbFileName)
    kbDict = dict()
    
    for line in kbFile:
        charList = line.strip().split(" ")
        kbKey = charList[0]
        charList.pop(0)
        kbDict[kbKey] = charList
        
    kbFile.close()
    return kbDict


#Input Words List Creation:
#All words in the input text file are put into a usable list
def input_list_creation(inFileName):
    inFile = open(inFileName)
    inFileList = []
    for word in inFile:
        inFileList.append(word.strip())
    
    return inFileList


#Found Substitution:
#For every word in the input file list, if the word itself is found in the dict
# of English words, then it will return True and nothing else will happen
# Otherwise, if it is not found in the dict of English words, then the rest of
#  the main code will run
def found(inFileList):
    if (word in trueDict):
        return True
    else:
        return False


#Drop Substitution:
#All possible ways to drop a single letter are found.
# If any of the results produce an English word, it is added as a possible
#  replacement
def drop(word, trueDict):
    possDropCorrect = []
    for index in range(len(word)):
        wordList = list(word)
        wordList.pop(index)
        if ("".join(wordList) in trueDict.keys()):
            possDropCorrect.append((trueDict["".join(wordList)], "".join(wordList)))
            possDropCorrect = set(possDropCorrect)
            possDropCorrect = list(possDropCorrect)
    
    return possDropCorrect


#Insert Substitution:
#All possible ways to insert a single letter are found
# If any of the results produce an English word, it is added as a possible
#  replacement
#This is done by looping through all keys int he keyboard dict
def insert(word, trueDict, kbDict):
    possInsertCorrect = []
    for index in range(len(word)):
        for letter in kbDict.keys():
            wordList = list(word)
            wordList.insert(index, letter)
            if ("".join(wordList) in trueDict):
                possInsertCorrect.append((trueDict["".join(wordList)], "".join(wordList)))
    
    for letter in kbDict.keys():
        if ((word+letter) in trueDict):
            possInsertCorrect.append((trueDict[(word+letter)], (word+letter)))    
    
    return possInsertCorrect


#Swap Substitution:
#All possible ways to switch the order of two consecutive letters are found
# If any of the results produce an English word, it is added as a possible
#  replacement
def swap(word, trueDict):
    possSwapCorrect = []
    for index in range(len(word)-1):
        wordList = list(word)
        letter1 = wordList[index]
        letter2 = wordList[index+1]
        wordList[index+1] = letter1
        wordList[index] = letter2
        if ("".join(wordList) in trueDict):
            possSwapCorrect.append((trueDict["".join(wordList)], "".join(wordList)))
    
    return possSwapCorrect


#Replace Substitution:
#All possible ways to replace a single letter with another letter are found
# If any of the results produce an English word, it is added as a possible
#  replacement
#This is done by looping through all keys int he keyboard dict
def replace(word, trueDict, kbDict):
    possReplaceCorrect = []
    for index in range(len(word)):
        for repList in kbDict[word[index]]:
            for rep in repList:
                wordList = list(word)
                wordList[index] = rep
                if ("".join(wordList).strip() in trueDict):
                    possReplaceCorrect.append((trueDict["".join(wordList)], "".join(wordList)))
    return list(possReplaceCorrect)


"""
#Sorting Words By Frequency:
#After all possible replacements are put into a list/set, the frequencies of
# each word are associated with each word
# Words are sorted from highest frequency to lowest
def frequency_sort(allPossCorrect, trueDict):
    frequList = set()
    for word in allPossCorrect:
        frequList.add(trueDict[word])
    
    frequDict = dict()
    counter = 0
    for frequ in frequList:
        frequDict[frequ] = allPossCorrect[counter]
        counter += 1
    
    allPossCorrectSorted = list(frequDict.keys())
    allPossCorrectSorted.sort(reverse=True)
    for index in range(len(allPossCorrectSorted)):
        allPossCorrectSorted[index] = frequDict[allPossCorrectSorted[index]]
    
    return allPossCorrectSorted
"""


#Main Code:
if __name__=="__main__":
    
    #User-Defined Input:
    #
    dictFileName = input("Dictionary file => ").strip()
    print(dictFileName)
    inFileName = input("Input file => ").strip()
    print(inFileName)
    kbFileName = input("Keyboard file => ").strip()
    print(kbFileName)
    
    
    
    trueDict = true_dict_creation(dictFileName)
    kbDict = keyboard_dict_creation(kbFileName)
    
    inFileList = input_list_creation(inFileName)
    
    for word in inFileList:
        if (found(word)):
            print(" "*(15-len(word)) + "{} -> FOUND".format(word))
            continue
        else:
            possDropCorrect = drop(word, trueDict)
            possInsertCorrect = insert(word, trueDict, kbDict)
            possSwapCorrect = swap(word, trueDict)
            possReplaceCorrect = replace(word, trueDict, kbDict)
            
            allPossCorrect = []
            allPossCorrect.extend(possDropCorrect)
            allPossCorrect.extend(possInsertCorrect)
            allPossCorrect.extend(possSwapCorrect)
            allPossCorrect.extend(possReplaceCorrect)
            
           # allPossCorrect = sorted(list(possDropCorrect+possInsertCorrect+possSwapCorrect+possReplaceCorrect))
            allPossCorrect = sorted(allPossCorrect, reverse = True)
            
            
            if (len(allPossCorrect) == 0):
                print(" "*(15-len(word)) + "{} -> NOT FOUND".format(word))
            elif (len(allPossCorrect) == 1):
                print(" "*(15-len(word)) + "{} -> FOUND  1:  {}".format(word, allPossCorrect[0][1]))
            else:

                if len(allPossCorrect) == 2:
                    print(" "*(15-len(word)) + "{} -> FOUND  2:  {} {}".format(word, allPossCorrect[0][1], allPossCorrect[1][1]))
                elif len(allPossCorrect) > 2:
                    
                    print(" "*(15-len(word)) + "{} -> FOUND{:3d}:  {} {} {}".format(word, len(allPossCorrect), allPossCorrect[0][1], allPossCorrect[1][1], allPossCorrect[2][1]))