#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:41:56 2021

@author: maxrueda
"""

import lab05_util as util

def print_info(index):
    print(restaurants[index][0], "({})".format(restaurants[index][5]))
    print("\t" + restaurants[index][3].replace("+", "\n\t"))
    
    avgScore = sum(restaurants[index][6]) / len(restaurants[index][6])
    print("Average score: {:.2f}".format(avgScore))

restaurants = util.read_yelp('yelp.txt')

index = int(input("Enter index: "))
print(index)
print_info(index)