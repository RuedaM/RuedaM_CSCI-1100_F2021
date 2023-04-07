#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 15:30:07 2021

@author: maxrueda
"""

import hw4_util as util

weekData = util.part2_get_week(1)
totalPositiveTests = 0

for stateData in weekData:
    if (stateData[0] == "AZ"):
        for positiveTest in stateData[2:9]:
            totalPositiveTests += int(positiveTest)
            print(totalPositiveTests)
        
        positiveTestAvg = (totalPositiveTests / 100000)
        
        print("Average daily positives per 100K population: {:.1f}".format(positiveTestAvg))
    """
    else:
        print("State", state ,"not found")
"""