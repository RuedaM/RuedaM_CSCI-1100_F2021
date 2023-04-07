#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:58:29 2021

@author: maxrueda
11/09/21
CSCI 1100
Lect. Exercises 18.1 - Point2d Class
"""

"""
1. Starting from the Point2d.py file you download from the Course Resources
    page of the Submitty site, please do the following:
        1) Write a new Point2d method called scale that takes as an input
            argument a Point2d object (self) and a numerical value (int or
            float) and multiples both the x and y attributes by this value.
        2) Write a new Point2d method called dominates that takes two Point2d
            objects and returns True if and only if the x coordinate of the
            first object is greater than that of the second object and the y
            coordinate of the first object is greater than that of the second
            object.
        3) The code to test these functions is commented out in the main code
            area. Please remove this commenting, test your code, and submit
            your resulting Point2d.py file. Call it Point2d_q1.py
"""

import math

class Point2d(object):
    def __init__( self, x0=0, y0=0 ):
        self.x = x0
        self.y = y0

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def dist(self, o):
        return math.sqrt( (self.x-o.x)**2 + (self.y-o.y)**2 )
    
    def scale(self, value):
        self.x *= value
        self.y *= value
    
    def dominates(self, point):
        if (self.x > point.x) and (self.y > point.y):
            return True
        else:
            return False



if __name__ == "__main__":
    p = Point2d(0,4)
    q = Point2d(5,10)
    leng = q.magnitude()
    leng = Point2d.magnitude(q)
    print("Magnitude {:.2f}".format( leng ))
    print("Distance is {:.2f}".format( p.dist(q) ))

    # Exercise 1 tests:
    p.scale(3)
    print('After scaling p = ({},{})'.format(p.x, p.y) )
    r = Point2d(3,5.5)
    r.scale(2)
    print('After scaling r = ({},{})'.format(r.x, r.y) )
    print('p dominates r:', p.dominates(r))
    print('r dominates p:', r.dominates(p))
    print('r dominates q:', r.dominates(q))