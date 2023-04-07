#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:55:38 2021

@author: maxrueda
"""

from PIL import Image


im1 = Image.open("ca.jpg")
im2 = Image.open("im.jpg")
im3 = Image.open("hk.jpg")
im4 = Image.open("bw.jpg")


imBlank = Image.new("RGB", (512,512), "white")
w,h = imBlank.size


im1re = im1.resize((256,256))
im2re = im2.resize((256,256))
im3re = im3.resize((256,256))
im4re = im4.resize((256,256))


imBlank.paste(im1re, (0,0))
imBlank.paste(im2re, (w//2,0))
imBlank.paste(im3re, (0,h//2))
imBlank.paste(im4re, (w//2,h//2))


imBlank.save("Lab4.1Result.jpg")
imBlank.show()