#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:32:07 2021

@author: maxrueda
"""

from PIL import Image

im = Image.open('KonoDioDa.jpg')
im.show()

im2 = im.crop((100,100,300,400))
im2.show()