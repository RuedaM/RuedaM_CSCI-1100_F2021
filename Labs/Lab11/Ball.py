#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:08:08 2021

@author: maxrueda
"""

class Ball(object):
    
    def __init__(self, x, y, dx, dy, r, c):
        self.xCoord, self.yCoord = x, y
        self.dxVal, self.dyVal = dx, dy
        self.rad = r
        self.color = c
    
    def position(self):
        return ((self.xCoord, self.yCoord))
    
    def move(self, maxx, maxy):
        self.xCoord += self.dxVal
        self.yCoord += self.dyVal
        self.check_and_reverse(maxx, maxy)
    
    def bounding_box(self):
        x0 = self.xCoord - self.rad
        y0 = self.yCoord - self.rad
        x1 = self.xCoord + self.rad
        y1 = self.yCoord + self.rad
        return ((x0, y0, x1, y1))
    
    def get_color(self):
        return (self.color)
    
    def some_inside(self, maxx, maxy):
        if (self.xCoord + self.rad > 0) and (self.xCoord - self.rad < maxx) \
        and (self.yCoord + self.rad > 0) and (self.yCoord - self.rad < maxy):
            return True
        else:
            print("False")
            return False
    
    def check_and_reverse(self, maxx, maxy):
        if (self.xCoord + self.rad < 0) or (self.xCoord - self.rad > maxx):
            self.dxVal *= -1
        if (self.yCoord + self.rad < 0) or (self.yCoord - self.rad > maxx):
            self.dyVal *= -1