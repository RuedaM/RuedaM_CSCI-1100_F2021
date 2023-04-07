#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 13:30:54 2021

@author: maxrueda
"""

import json
from BerryField import Berry_Field as bfClass

class Bear(object):
    def __init__(self, bearCoordAndDirec=[]):
        self.rowLoc = bearCoordAndDirec[0]
        self.colLoc = bearCoordAndDirec[1]
        self.direction = bearCoordAndDirec[2]
        
        self.outside = False
        self.rest = False
        self.restCount = 3
    
    
    
    def __str__(self):
        return "Bear at ({},{}) moving {}".format(self.rowLoc, self.colLoc, self.direction)
    
    
    #detects if the bear is resting, keeps a counter within itself so that it wakes up after 3 turns
    def resting(self):
        if (self.rest):
            self.restCount -= 1
            if (self.restCount == 0):
                self.rest = False
                self.restCount = 3
                return False
            return True
        else:
            return False
            
        
        



if (__name__ == "__main__"):
    bb1Dict = json.loads(open("bears_and_berries_1.json").read())
    
    bearObjList = []
    for bear in bb1Dict["active_bears"]:
        bearObjList.append(Bear(bear))
    
    for bearObj in bearObjList:
        print(bearObj)
    
    for bearObj in bearObjList:
        bearObj.move(bfClass(bb1Dict).grid)
        print(bfClass(bb1Dict))
    
    