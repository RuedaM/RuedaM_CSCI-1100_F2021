#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 13:30:54 2021

@author: maxrueda
"""

class Tourist(object):
    def __init__(self, tourCoord=[], l = []):
        self.rowLoc = tourCoord[0]
        self.colLoc = tourCoord[1]
        self.bearObjList = l
        
        self.bearSeenCount = 0
        self.turnCount = 0
        self.gone = False
        
        
    
    
    
    def __str__(self):
        return "Tourist at ({},{}), {} turns without seeing a bear.".format(self.rowLoc, self.colLoc, self.turnCount)
    
    
    #Used in leave(), explained there
    def see_bear(self, bearObjList):
        for bearObj in bearObjList:
            btDist = ((((bearObj.rowLoc)-(self.rowLoc))**2) + (((bearObj.colLoc)-(self.colLoc))**2))**.5
            if btDist <= 4:
                self.bearSeenCount += 1
    
    
    #uses see_bear() to count the amount of bears in the tourist's vicinity
    #based on certain conditions,t he bear will be signaled to leave
    def leave(self, bearObjList):
        self.see_bear(bearObjList)
        
        if (self.bearSeenCount == 0):
            self.turnCount += 1
        
        if (self.turnCount == 3) \
        or (self.bearSeenCount >= 3):
            self.gone = True
        
        self.bearSeenCount = 0



if (__name__ == "__main__"):
    print("OK")