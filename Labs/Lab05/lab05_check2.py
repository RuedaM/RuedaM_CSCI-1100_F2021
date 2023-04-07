#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:07:26 2021

@author: maxrueda
"""

import lab05_util as util

def print_info(index):
    print(restaurants[index][0], "({})".format(restaurants[index][5]))
    print("\t" + restaurants[index][3].replace("+", "\n\t"))
    
    if (len(restaurants[index][6]) > 3):
        minScore = min(restaurants[index][6])
        maxScore = max(restaurants[index][6])
        avgScore = (sum(restaurants[index][6]) - minScore - maxScore) / (len(restaurants[index][6]) - 2)
    else:
        avgScore = sum(restaurants[index][6]) / len(restaurants[index][6])
    
    if (avgScore >= 0) and (avgScore < 2):
        print("This restaurant is rated bad, based on {} reviews.".format(len(restaurants[index][6])))
    elif (avgScore >= 2) and (avgScore < 3):
        print("This restaurant is rated average, based on {} reviews.".format(len(restaurants[index][6])))
    elif (avgScore >= 3) and (avgScore < 4):
        print("This restaurant is rated above average, based on {} reviews.".format(len(restaurants[index][6])))
    elif (avgScore >= 4) and (avgScore < 5):
        print("This restaurant is rated very good, based on {} reviews.".format(len(restaurants[index][6])))
    elif (avgScore >= 5):
        print("This restaurant is rated excellent, based on {} reviews.".format(len(restaurants[index][6])))


restaurants = util.read_yelp('yelp.txt')
booleanFlag = True


while booleanFlag:
    index = int(input("Enter ID: "))
    print(index)
    if (index-1 >= 0) and (index-1 <= 153):
        print_info(index-1)
    else:
        print("Warning: Invalid ID")
        booleanFlag = False