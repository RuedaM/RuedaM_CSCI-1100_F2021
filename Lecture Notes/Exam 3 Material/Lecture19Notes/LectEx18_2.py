#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:58:30 2021

@author: maxrueda
11/09/21
CSCI 1100
Lect. Exercises 18.2 - Point2d Class, continued
"""

"""
2. Copy your resulting file from the first question to a new file, perhaps
    called Point2d_q2.py.
        1) Write and test the implementation of the method __str__ which
            returns a string created from the values of a Point2d object. For
            our purposes this is mostly used to create a string that can be
            printed. Make sure you have this working before you proceed to the
            other parts of this exercise because they depend on it. If you are
            wondering about the format of a point, take a look at how we print
            out a point in Part 1.
        2) Write the implementation of the subtraction method __sub__ for the
            Point2d object. Uncomment the code in the main area and test this
            in Spyder.
        3) Write the implementation of the method __mul__ which is like the
            scale function you wrote for part 1, but it creates a new Point2d
            object.
        4) Write the implementation of the method __eq__ which returns True if
            and only if the two Point2d objects have exactly the same x and y
            values.
    For each of these you should look at the commented out main code in the
    Point2d.py file you were provided to see how these methods should be used.
    Uncomment this code, test your methods, and upload to Submitty when you are
    done.
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
    
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    
    def __sub__(self, value):
        xDiff = self.x - value.x
        yDiff = self.y - value.y
        
        return Point2d(xDiff, yDiff)
    
    def __mul__(self, value):
        xProd = self.x * value
        yProd = self.y * value
        return Point2d(xProd, yProd)
    
    def __eq__(self, value):
        if (self.x == value.x) and (self.y == value.y):
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
    
    
    # Exercise 2:  __str__ tests
    print("As a string p is " + str(p))
    print("As a string r is " + str(r))
    
    # Exercise 2:  other tests
    print('p - q =', str(p-q) )
    print('q - r =', str(q-r) )
    new_q = q*4
    print('new_q is', new_q )
    t = Point2d(0,12)
    u = Point2d(0,5)
    v = Point2d(5,12)
    print('p == t', p==t )
    print('t == u', t==u )
    print('t == v', t==v )