#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:02:11 2021

@author: maxrueda
"""

import math

def bunnies_next_year(bpop, fpop):
    bpop_next = ((10*bpop)/(1+0.1*bpop)) - (0.05*bpop*fpop)
    return math.floor(bpop_next)
    

def foxes_next_year(bpop, fpop):
    fpop_next = (0.4 * fpop) + (0.02 * fpop * bpop)
    return math.floor(fpop_next)


bpop = input("Number of bunnies ==> ")
print(bpop)
fpop = input("Number of foxes ==> ")
print(fpop)

bpop = int(bpop)
fpop = int(fpop)


print("Year 1:", bpop, fpop)


bpop_next = bunnies_next_year(bpop, fpop)
fpop_next = foxes_next_year(bpop, fpop)
print("Year 2:", bpop_next, fpop_next)
bpop = bpop_next
fpop = fpop_next


bpop_next = bunnies_next_year(bpop, fpop)
fpop_next = foxes_next_year(bpop, fpop)
print("Year 3:", bpop_next, fpop_next)
bpop = bpop_next
fpop = fpop_next


bpop_next = bunnies_next_year(bpop, fpop)
fpop_next = foxes_next_year(bpop, fpop)
print("Year 4:", bpop_next, fpop_next)
bpop = bpop_next
fpop = fpop_next


bpop_next = bunnies_next_year(bpop, fpop)
fpop_next = foxes_next_year(bpop, fpop)
print("Year 5:", bpop_next, fpop_next)
bpop = bpop_next
fpop = fpop_next