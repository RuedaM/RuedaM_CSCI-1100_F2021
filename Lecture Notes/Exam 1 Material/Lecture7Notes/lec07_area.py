#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 16:56:23 2021

@author: maxrueda
"""

import math

def circle(radius):
    ''' Compute and return the area of a circle '''
    return math.pi * radius**2


def cylinder(radius,height):
    ''' Compute and return the surface area of a cylinder '''
    circle_area = circle(radius)
    height_area = 2 * radius * math.pi * height
    return 2*circle_area + height_area


def sphere(radius):
    '''  Compute and return the surface area of a sphere '''
    return 4 * math.pi * radius**2