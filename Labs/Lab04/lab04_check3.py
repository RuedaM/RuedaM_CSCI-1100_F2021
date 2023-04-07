#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:54:53 2021

@author: maxrueda
"""

from PIL import Image


def resize_image(im):
    w,h = im.size
    imresized = im.resize((((w*256)//h),256))
    return imresized


im1 = Image.open("1.jpg")
im2 = Image.open("3.jpg")
im3 = Image.open("5.jpg")
im4 = Image.open("2.jpg")
im5 = Image.open("4.jpg")
im6 = Image.open("6.jpg")



imBlank = Image.new("RGB", (1000,360))
w,h = imBlank.size


im1re = resize_image(im1)
im2re = resize_image(im2)
im3re = resize_image(im3)
im4re = resize_image(im4)
im5re = resize_image(im5)
im6re = resize_image(im6)

w1,h1 = im1re.size
w2,h2 = im2re.size
w3,h3 = im3re.size
w4,h4 = im4re.size
w5,h5 = im5re.size
w6,h6 = im6re.size


imBlank.paste(im1re, (31,20))
imBlank.paste(im2re, (31+w1+10,60))
imBlank.paste(im3re, (31+w1+w2+20,20))
imBlank.paste(im4re, (31+w1+w2+w3+30,60))
imBlank.paste(im5re, (31+w1+w2+w3+w4+40,20))
imBlank.paste(im6re, (31+w1+w2+w3+w4+w5+50,60))


imBlank.save("Lab4.3Result.jpg")
imBlank.show()