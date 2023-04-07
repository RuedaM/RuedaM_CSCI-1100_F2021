#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:20:09 2021

@author: maxrueda
"""

from PIL import Image


def make_square(im):
    w,h = im.size
    if w > h:
        squareVer = im.crop((0,0,h,h))
        return squareVer
    else:
        squareVer = im.crop((0,0,w,w))
        return squareVer

"""
im1 = Image.open("inc1.jpg")
im3 = Image.open("inc3.jpg")

newim1 = make_square(im1)
newim3 = make_square(im3)

newim1.show()
newim3.show()
"""