#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:42:46 2021

@author: maxrueda

Rueda, Maximillian
10/14/21
CSCI 1100
Homework 4.2 - COVID-19 Quarantine States


This code utilizes per-state COVID-19 spread data over the first 29 weeks since
 March 15 to calculate certain values based on user input. The user would input
 the number week and would be given options to calculate 1 of the following:
 the average daily positive cases per 100,000 people of a given state, the
 average daily percentage of positive tests over the week of a given state, the
 list of state abbreviations, alphabetically by two-letter abbreviation, of
 travel quaratine states for the given week, or the state with the highest
 daily average number of positive cases per 100,000 people over the given week
 and the daily average itself
"""


#Imports:
#hw4_util file contains functions that allows us to properly complete the code
# For Part 2, the functions part2_get_week() and print_abbreviations() are
# used to return a list of lists of COVID test data for the given week and to,
# given a list of state abbreviations, output them 10 per line respectively
#To abbreviate the title, it will be imported as util
import hw4_util as util


#User-Defined Functions and Printed Outputs:
#Unique to this code, text will be printed from the functions themselves rather
# than storing returned values in integers in the main code and printing those

#Daily:
#daily() takes 3 paramenters, the user-inputted week and state, and if the
# result should be returned or not
# If the function is called from the main code, no value is returned and print
#  statements are outputted - the opposite will happen if called from a function
#All states' data in the given week are stored in a variable
#The quotients of positive tests each day in the week in a given state and the
# population of the state are stored in the list dailyPosPercList
# Afterwards, the average daily positive cases per 100,000 people for that
#  state for the given week is calculated
def daily(week, state, canReturn):
    weekData = util.part2_get_week(week)
    dailyPosPercList = []
    
    for stateData in weekData:
        if (stateData[0] == state):
            for positiveTest in stateData[2:9]:
                dailyPosPercList.append(positiveTest/stateData[1])
            
            positiveTestAvg = (sum(dailyPosPercList) / len(dailyPosPercList)) * 100000
            
            if canReturn:
                return positiveTestAvg
            else:
                print("Average daily positives per 100K population: {:.1f}".format(positiveTestAvg))
                return
    
    print("State", state ,"not found")


#Percent:
#perc() takes 3 paramenters, the user-inputted week and state, and if the
# result should be returned or not
# If the function is called from the main code, no value is returned and print
#  statements are outputted - the opposite will happen if called from a function
#All states' data in the given week are stored in a variable
# two totals are declared, one each for total positive and negative tests
#The sums of all positive and negative tests in the week in a given state are
# calculated and are alter used to calculate the average daily percentage of
# tests that are positive over the week
def pct(week, state, canReturn):
    weekData = util.part2_get_week(week)
    totPosTests = 0
    totNegTests = 0
    
    for stateData in weekData:
        if (stateData[0] == state):
            for positiveTest in stateData[2:9]:
                totPosTests += positiveTest
            for negativeTest in stateData[9:]:
                totNegTests += negativeTest
            
            percentPositive = ((totPosTests/(totPosTests + totNegTests)) * 100)
            
            if canReturn:
                return percentPositive
            else:
                print("Average daily positive percent: {:.1f}".format(percentPositive))
                return
        
    print("State", state ,"not found")


#Quarantine:
#quar() only takes one argument, the user-inputted week
#All states' data in the given week are stored in a variable
#Both daily() and pct() are called within this function, and both provide
# returned values rather than print statements
#For each state, if the average daily positive cases or average daily
# percentage of positive tests is greater than 10, that state is added to a
# list of quarantined states
# The states are then printed 10 in a row using part2_get_week() in hw4_util
def quar(week):
    weekData = util.part2_get_week(week)
    stateList = []
    
    for stateData in weekData:
        if (pct(week, stateData[0], True) > 10) or (daily(week, stateData[0], True) > 10):
            stateList.append(stateData[0])
    
    print("Quarantine states:")
    util.print_abbreviations(stateList)


#Highest:
#high() only takes one argument, the user-inputted week
#All states' data in the given week are stored in a variable
#daily() is called within this function, and it provides a returned value
# rather than print statements
# For each state, the average daily positive cases are stored in list -
#  simultaneously, the state abbreviation is stored in a separate list
# Both the max value of daily averages and the corresponding state (which is
#  found by finding the index at which the max daily average is and using that
#  index to find the state in the state list) are determined and printed
def high(week):
    weekData = util.part2_get_week(week)
    dailyAvgList = []
    dailyAvgStateList = []
    
    for stateData in weekData:
        dailyAvgList.append(daily(week, stateData[0], True))
        dailyAvgStateList.append(stateData[0])
    
    maxDailyAvg = max(dailyAvgList)
    
    maxDailyAvgStateIndex = dailyAvgList.index(max(dailyAvgList))
    maxDailyAvgState = dailyAvgStateList[maxDailyAvgStateIndex]
    
    print("State with highest infection rate is", maxDailyAvgState)
    print("Rate is {:.1f} per 100,000 people".format(maxDailyAvg))




#Main Code:
if __name__ == "__main__":

    #While Loop:
    #This booleanFlag variable will remain True so that the code will constantly
    # loop until a negative number, i.e. a negative week, is inputted, at which
    # point the while-loop will break at the code will end
    #If the user gives an unrecognizable command at any stage of the code, the
    # code will loop back to the beginning of the while-loop
    booleanFlag = True    

    while booleanFlag:
        
        #User Input:
        #Immediately after getting input, the string is placed in a new variable
        # week is converted to a usable whole number integer value
        week = input("...\nPlease enter the index for a week: ")
        print(week)
        week = week.strip("\r")
        week = int(week)
        
        if (week < 0):
            booleanFlag = False
        
        #There are only data for up to and including 29 weeks; any weeks past
        # 29 will have no data
        elif (week > 29):
            print("No data for that week")
        
        else:
            
            #Main If-Statements:
            #The code will ask the user what of four possibilities it should
            # calculate for the given week
            # Based on user input, the function will call a corresponding
            #  user-defined function with certain variables (or loop back to
            #  the start if the input is not recognizable)
            if (len(util.part2_get_week(week)) > 1):
                request = input("Request (daily, pct, quar, high): ")
                print(request)
                request = request.strip("\r")
                
                if (request.lower() == "daily"):
                    state = input("Enter the state: ")
                    print(state)
                    state = state.strip("\r")
                    daily(week, state.upper(), False)
                elif (request.lower() == "pct"):
                    state = input("Enter the state: ")
                    print(state)
                    state = state.strip("\r")
                    pct(week, state.upper(), False)
                elif (request.lower() == "quar"):
                    quar(week)
                elif (request.lower() == "high"):
                    high(week)
                else:
                    print("Unrecognized request")