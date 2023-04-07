#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:17:31 2021

@author: maxrueda
"""

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

class Date(object):
    def __init__(self, yr=1900, mo=1, dy=1):
        self.yr = yr
        self.mo = mo
        self.dy = dy
    
    def __str__(self):
        return "{}/{}/{}".format(self.yr, str(self.mo).rjust(2, "0"), str(self.dy).rjust(2, "0"))
    
    def same_day_in_year(self, date):
        if (self.mo == date.mo) and (self.dy == date.dy):
            return True
        else:
            return False
    
    def is_leap_year(self):
        if (self.yr % 4 == 0) and not ((self.yr % 100 == 0) and not (self.yr % 400 == 0)):
            return True
        else:
            return False
    
    def __lt__(self, date):
        print("Comparing", str(self.yr), "and", str(date.yr))
        if (self.yr < date.yr) or ((self.yr == date.yr) and (self.mo < date.mo)) or (((self.yr == date.yr) and (self.mo == date.mo)) and (self.dy < date.dy)):
            return True
        else:
            return False



if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1996, 4, 13)
    d4 = Date(2002, 4, 11)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print("d1.is_leap_year()", d1.is_leap_year())
    print("d2.is_leap_year()", d2.is_leap_year())
    print("d4.is_leap_year()", d4.is_leap_year())
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1998, 5, 13)
    d4 = Date(1998, 4, 11)
    print("d1 < d2", (d1 < d2))
    print("d2 < d3", (d2 < d3))
    print("d3 < d4", (d3 < d4))
