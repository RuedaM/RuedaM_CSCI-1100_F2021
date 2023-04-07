#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:07:38 2021

@author: maxrueda

Rueda, Maximillian
9/23/21
CSCI 1100
Homework 2.1
"""



import math


def find_volume_sphere(radius):
    sphere_volume = ((4/3) * math.pi * math.pow(radius, 3))
    return sphere_volume

def find_volume_cube(side):
    cube_volume = (math.pow(side, 3))
    return cube_volume


GumballRadius = input("Enter the gum ball radius (in.) => ")
print(GumballRadius)
GumballRadius = float(GumballRadius)

Sales = input("Enter the weekly sales => ")
print(Sales)
Sales = int(Sales)
print()


TargetSales = math.ceil((Sales * 1.25))


GumballsPerSide = math.ceil((TargetSales ** (1/3)))
print("The machine needs to hold",GumballsPerSide,"gum balls along each edge.")


SideMeasure = ((GumballRadius*2) * GumballsPerSide)
print("Total edge length is {0:.2f} inches.".format(SideMeasure))


TotalGumballs = (GumballsPerSide ** 3)
RemainingGumballs = (int(TotalGumballs) - TargetSales)
print("Target sales were {}, but the machine will hold {} extra gum balls.".format(TargetSales, RemainingGumballs))


GumballVolume = find_volume_sphere(GumballRadius)
CubeVolume = find_volume_cube(SideMeasure)

WastedSpaceWithTarget = (CubeVolume - (GumballVolume * TargetSales))
WastedSpaceWhenFull = (CubeVolume - (GumballVolume * TotalGumballs))

print("Wasted space is {0:.2f} cubic inches with the target number of gum balls,\nor {1:.2f} cubic inches if you fill up the machine.".format(WastedSpaceWithTarget, WastedSpaceWhenFull))