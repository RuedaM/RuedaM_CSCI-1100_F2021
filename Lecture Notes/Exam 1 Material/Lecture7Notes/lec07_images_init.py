#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:30:26 2021

@author: maxrueda
"""

from PIL import Image

filename = "KonoDioDa.jpg"
im = Image.open(filename)
print('\n' '********************')
print("Here's the information about", filename)
print(im.format, im.size, im.mode)

gray_im = im.convert('L')
scaled = gray_im.resize( (128,128) )
print("After converting to gray scale and resizing,")
print("the image information has changed to")
print(scaled.format, scaled.size, scaled.mode)

scaled.show()
scaled.save(filename + "_scaled.jpg")