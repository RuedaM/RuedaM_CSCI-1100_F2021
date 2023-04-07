#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:48:26 2021

@author: maxrueda
"""

from PIL import Image
import check2_helper


im1 = Image.open("ca.jpg")
im2 = Image.open("im.jpg")
im3 = Image.open("hk.jpg")
im4 = Image.open("bw.jpg")

im1square = check2_helper.make_square(im1)
im2square = check2_helper.make_square(im2)
im3square = check2_helper.make_square(im3)
im4square = check2_helper.make_square(im4)


imBlank = Image.new("RGB", (512,512), "white")
w,h = imBlank.size


im1re = im1square.resize((256,256))
im2re = im2square.resize((256,256))
im3re = im3square.resize((256,256))
im4re = im4square.resize((256,256))


imBlank.paste(im1re, (0,0))
imBlank.paste(im2re, (w//2,0))
imBlank.paste(im3re, (0,h//2))
imBlank.paste(im4re, (w//2,h//2))


imBlank.save("Lab4.2Result.jpg")
imBlank.show()