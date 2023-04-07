#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:17:31 2021

@author: maxrueda
"""

from Date import Date

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]


def read_birthdays(bdayFileName):
    bdayFile = open(bdayFileName)
    bdayList = []
    for line in bdayFile:
        lineList = line.strip().split(" ")
        bdayList.append(Date(lineList[0], lineList[1], lineList[2]))
    
    return bdayList


if __name__ == "__main__":
    bdayList = read_birthdays("birthdays.txt")
    
    earliest = bdayList[0]
    for index in range(len(bdayList)):
        if (bdayList[index] < earliest):
            earliest = bdayList[index]
    print("THE EARLIEST:", str(earliest))
    
    latest = bdayList[0]
    for index in range(len(bdayList)):
        if not (bdayList[index] < latest):
            latest = bdayList[index]
    print("THE LATEST:", str(latest))
    
    monthDict = dict()
    for bday in bdayList:
        bdayListTemp = str(bday).split("/")
        if (month_names[int(bdayListTemp[1])] in monthDict):
            monthDict[month_names[int(bdayListTemp[1])]] += 1
        else:
            monthDict[month_names[int(bdayListTemp[1])]] = 1
    
    highest = max(monthDict.values())
    print("MONTH WITH MOST BIRTHDAYS:", month_names[highest+1])
        