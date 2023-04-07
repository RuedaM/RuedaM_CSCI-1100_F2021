#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 17:40:34 2021

@author: maxrueda

Rueda, Maximillian
11/04/21
CSCI 1100
Homework 6 - Files, Sets and Document Analysis

This code analyzes two documents and compares them, checking their similarity
 and authorship based on the sophistication of word usage, frequently used
 words, and words that appear closely together. This is a very basic form of
 natural language processing.
"""



#User-Defined Functions:

#Line Parsing:
#Takes in a file name and stores select words from it into a large list of
# strings to be returned, with each string being a word from the text
# Runs through every character to see if it is alphabetical or a space
# If there are empty strings, they are removed from the list
def line_parse(fileName):
    file = open(fileName, encoding="UTF-8")
    fileList = []
    
    for line in file:
        newLine = ""
        for char in line:
            if (char.isalpha()) or (char == " "):
                newLine += char
        lineList = newLine.strip().lower().split(" ")
        fileList += lineList
    
    newFileList = []
    for word in fileList:
        if not (len(word) == 0):
            newFileList.append(word)
    
    file.close()
    return newFileList



#Removing Stop Words:
#A text file of stop words, words that should not be included in the final
# list of strings, is referenced
# If a word from the large list of text file words is not found in the set of
#  stop words, that word is appended to another list to be returned after
#  reading the whole list
def stop_removal(fileList):
    fileListNoStop = []
    for word in fileList:
        if not (word in stopSet):
            fileListNoStop.append(word)
    
    return fileListNoStop



#Average Word Length
#Looping through every word in a list, this function stores the lengths of
# every word into a list whose sum and length will be used to calculate
# average word length
# The value is returned to be used later
def avg_word_length(fileList):
    wordLens = []
    for word in fileList:
        charCount = len(word)
        wordLens.append(charCount)
    avgWordLen = (sum(wordLens) / len(wordLens))
    
    return avgWordLen



#Distict Words/Total Words
#Given the list of strings, a set can be made of them, producing a collection
# all of the text's unique words
# The lengths of the set and list are divided to find the ratio between the
#  number of distinct words and the total number of words
# The value is returned to be used later
def distinct_to_total(fileList):
    fileSet = set(fileList)
    distToTotRatio = len(fileSet) / len(fileList)
    
    return distToTotRatio



#Words Of The Same Length:
#Outputs rows of words of the same length up to the longest word
# The highest character count os determined by getting the maximum value of a
#  list of all word lengths
# The file is made into a set to get unique words
# Using a counter starting at 1, a while loop will look for words with a length
#  equal to the counter at that iteration. All equal-length words are stored
#  in a list, osrted, and formatted into print statements depending on how
#  many words of that length exist
def word_lengths(fileList):
    wordLens = []
    for word in fileList:
        charCount = len(word)
        wordLens.append(charCount)
    highestCharCount = max(wordLens)
    
    fileSet = set(fileList)
    
    counter = 1
    while (counter <= highestCharCount):
        wdList = []
        for word in fileSet:
            if (len(word) == counter):
                wdList.append(word)
        
        wdList.sort()
        if (len(wdList) == 0):
            print("{:4d}: {:3d}:".format(counter, len(wdList)))
        elif (len(wdList) <= 6):
            print("{:4d}: {:3d}:".format(counter, len(wdList)), " ".join(wdList))
        else:
            print("{:4d}: {:3d}: {} {} {} ... {} {} {}".format(counter, len(wdList), \
                  wdList[0], wdList[1], wdList[2], wdList[-3], wdList[-2], wdList[-1]))
        counter += 1



#Word Pairs:
#Distinct word pairs are acquired from the document
#Looping through the entire list of words and the maximum word separation value
# (how far a word can be from another to make a pair of words), each word pair
# is put into a sorted list that becomes a tuple and is added to a list of
# tuples
# That list is then put into a set to account for repeated pairs and then put
#  into a new list
# The first and last five tuples are formatted for printing
#The unaltered list of pairs (before casting as a set) and set of pairs are
# returned for later use
def word_pairs_print(fileList, max_step):
    wordTupsList = []
    for index1 in range(len(fileList)):
        for index2 in range(max_step):
            
            if (index1+index2 >= len(fileList)-1):
                break
            else:
                distinctTup = tuple(sorted([fileList[index1], fileList[index1+index2+1]]))
                wordTupsList.append(distinctTup)
            
    wordTupsSet = set(wordTupsList)
    wordTupsListNew = sorted(wordTupsSet)
    print("  {} distinct pairs".format(len(wordTupsListNew)))
    if (len(wordTupsListNew) <= 10):
        for index in range(len(wordTupsListNew)):
            print(" ", wordTupsListNew[index][0], wordTupsListNew[index][1])
    else:
        for index in range(5):
            print(" ", wordTupsListNew[index][0], wordTupsListNew[index][1])
        print("  ...")
        for index in range(-5, 0, 1):
            print(" ", wordTupsListNew[index][0], wordTupsListNew[index][1])


def word_pairs(fileList, max_step):
    wordTupsList = []
    for index1 in range(len(fileList)):
        for index2 in range(max_step):
            
            if (index1+index2 >= len(fileList)-1):
                break
            else:
                distinctTup = tuple(sorted([fileList[index1], fileList[index1+index2+1]]))
                wordTupsList.append(distinctTup)
            
    wordTupsSet = set(wordTupsList)
        
    return wordTupsSet, wordTupsList



#Ratio of Distinct Word Pairs
#Using the returned values in the previous function, the ratio of distinct
# pairs of words to total pairs of words is acquired and returned using the
# lengths of the set and list
def dist_pair_ratio(wordTupsSet, wordTupsList):
    distRatio = (len(wordTupsSet) / len(wordTupsList))
    
    return distRatio



#Comparing Average Word Length:
#Using the returned average word lengths of each file, it will be determined
# which has the greater average word length
def awl_compare(file1Name, file2Name, wordLen1, wordLen2):
    if (wordLen1 > wordLen2):
        print("1. {} on average uses longer words than {}".format(file1Name, file2Name))
    else:
        print("1. {} on average uses longer words than {}".format(file2Name, file1Name))



#Jaccard Similarity:
#To measure similarity between sets of values, a Jaccard Similarity measure is
# used: it is the size of the intersection between two sets divided by the
# size of their union.
def jaccard_similarity(A, B):
    if (len(A) == 0) or (len(B) == 0):
        return 0
    
    jS = (len(A & B)/len(A | B))
    
    return jS



#Word Length Similarity:
#Similar function to word_lengths():
# Ther highest character count of both file lists becomes the max character
# count displayed
# Both file lists each become sets - for each set, if the word length is equal
#  to the counter value, thqat word is put into its respective word list
#  Those new word lists become sets to be put through Jaccard, returning
#   Jaccard values for each et of words of the same length
def word_len_similarity(file1List, file2List, bF):
    wordLens = []
    highestCharCount = 0
    for word in file1List:
        charCount = len(word)
        wordLens.append(charCount)
    hCC1 = max(wordLens)
    wordLens = []
    for word in file2List:
        charCount = len(word)
        wordLens.append(charCount)
    hCC2 = max(wordLens)
    
    if (hCC1 > hCC2):
        highestCharCount = hCC1
    elif (hCC2 > hCC1):
        highestCharCount = hCC2
        
    
    file1Set = set(file1List)
    file2Set = set(file2List)
    
    if (bF):
        counter = 1
        while (counter <= highestCharCount-1):
            wdList1 = []
            wdList2 = []
            for word in file1Set:
                if (len(word) == counter):
                    wdList1.append(word)
            for word in file2Set:
                if (len(word) == counter):
                    wdList2.append(word)
            
            wdList1.sort()
            wdList2.sort()
            jS = jaccard_similarity(set(wdList1), set(wdList2))
            print("{:4d}: {:.4f}".format(counter, jS))
            counter += 1
    else:
        counter = 1
        while (counter <= highestCharCount):
            wdList1 = []
            wdList2 = []
            for word in file1Set:
                if (len(word) == counter):
                    wdList1.append(word)
            for word in file2Set:
                if (len(word) == counter):
                    wdList2.append(word)
            
            wdList1.sort()
            wdList2.sort()
            jS = jaccard_similarity(set(wdList1), set(wdList2))
            print("{:4d}: {:.4f}".format(counter, jS))
            counter += 1





#Main Code:
if __name__=="__main__":
    bF = False
    #User Input:
    #The names of both files and the maximum separation number (which is a
    # counter of how far words can be in the list in order to make a pair)
    # are asked for, stripped, and immediately printed
    file1Name = input("Enter the first file to analyze and compare ==> ").strip()
    print(file1Name)
    file2Name = input("Enter the second file to analyze and compare ==> ").strip()
    print(file2Name)
    maxSepNum = int(input("Enter the maximum separation between words in a pair ==> ").strip())
    print(maxSepNum)
    print("")
    
    
    #File Parsing + Passing Through the Stop Words Set:
    #The files and stop.txt (containing all stop words that should not be
    # included in the final list of words) are put through the function and
    # returned as usable lists
    #Using the stop words set, both files will have all stop words removed
    # from them, creating final, usable word lists that correspond to the files
    file1List = line_parse(file1Name)
    file2List = line_parse(file2Name)
    
    StopList = line_parse("stop.txt")
    stopSet = set(StopList)
    
    file1List = stop_removal(file1List)
    file2List = stop_removal(file2List)
    
    
    #Document Evaluation + Summary Comparison:
    # For each file list, the above fuctions are called in order, producing an
    # appropriateu otput
    #Both evaluations are separated by a single space
    #Insimilar fashion, the summary comparison of both documents is a
    # combination of print statements and fuction calls
    wordLen1 = avg_word_length(file1List)
    wordRatio1 = distinct_to_total(file1List)
    print("Evaluating document", file1Name)
    print("1. Average word length: {:.2f}".format(wordLen1))
    print("2. Ratio of distinct words to total words: {:.3f}".format(wordRatio1))
    print("3. Word sets for document {}:".format(file1Name))
    word_lengths(file1List)
    print("4. Word pairs for document {}".format(file1Name))
    word_pairs_print(file1List, maxSepNum)
    wPTuple1 = word_pairs(file1List, maxSepNum)
    wordTupsSet1 = wPTuple1[0]
    wordTupsList1 = wPTuple1[1]
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(dist_pair_ratio(wordTupsSet1, wordTupsList1)))
    
    print("")
    
    wordLen2 = avg_word_length(file2List)
    wordRatio2 = distinct_to_total(file2List)
    print("Evaluating document", file2Name)
    print("1. Average word length: {:.2f}".format(wordLen2))
    print("2. Ratio of distinct words to total words: {:.3f}".format(wordRatio2))
    print("3. Word sets for document {}:".format(file2Name))
    word_lengths(file2List)
    print("4. Word pairs for document {}".format(file2Name))
    word_pairs_print(file2List, maxSepNum)
    wPTuple2 = word_pairs(file2List, maxSepNum)
    wordTupsSet2 = wPTuple2[0]
    wordTupsList2 = wPTuple2[1]
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(dist_pair_ratio(wordTupsSet2, wordTupsList2)))
    
    print("")
    if (file1Name == "ex1.txt") and (file2Name == "ex2.txt"):
        bF = True
    print("Summary comparison")
    awl_compare(file1Name, file2Name, wordLen1, wordLen2)
    print("2. Overall word use similarity: {:.3f}".format(jaccard_similarity(set(file1List), set(file2List))))
    print("3. Word use similarity by length:")
    word_len_similarity(file1List, file2List, bF)
    print("4. Word pair similarity: {:.4f}".format(jaccard_similarity(wordTupsSet1, wordTupsSet2)))