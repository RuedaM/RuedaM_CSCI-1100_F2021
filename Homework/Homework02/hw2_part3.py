#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:07:43 2021

@author: maxrueda

Rueda, Maximillian
9/23/21
CSCI 1100
Homework 2.3
"""



def number_happy(sentence):
    sentence = sentence.lower()
    HappyCount = sentence.count("laugh")
    HappyCount += sentence.count("happiness")
    HappyCount += sentence.count("love")
    HappyCount += sentence.count("excellent")
    HappyCount += sentence.count("good")
    HappyCount += sentence.count("smile")
    return HappyCount

def number_sad(sentence):
    sentence = sentence.lower()
    SadCount = sentence.count("bad")
    SadCount += sentence.count("sad")
    SadCount += sentence.count("terrible")
    SadCount += sentence.count("horrible")
    SadCount += sentence.count("problem")
    SadCount += sentence.count("hate")
    return SadCount


Sentence = input("Enter a sentence => ")
print(Sentence)


HappyNumber = number_happy(Sentence)
SadNumber = number_sad(Sentence)

"""
Find and print the tone of the sentence by first printing a sentiment line
 with a number of + equal to the number of happy words followed by the
 number of - equal to the number of sad words, followed by a simple
 statement of the analysis.
 """
print("Sentiment:", ("+" * HappyNumber) + ("-" * SadNumber))


if (HappyNumber > SadNumber):
    print("This is a happy sentence.")
elif (HappyNumber < SadNumber):
    print("This is a sad sentence.")
else:
    print("This is a neutral sentence.")