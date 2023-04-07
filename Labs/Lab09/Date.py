'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

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
        if (self.yr < date.yr) or ((self.yr == date.yr) and (self.mo < date.mo)) or (((self.yr == date.yr) and (self.mo == date.mo)) and (self.dy < date.dy)):
            return True
        else:
            return False