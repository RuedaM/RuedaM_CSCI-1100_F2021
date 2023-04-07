#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:57:04 2021

@author: maxrueda
11/12/21
CSCI 1100
Lect. Exercises 19.2 - lec19_american_in_troy.py Example
"""

"""
2. Copy the code in lec19_restaurant_exercise.py into a file called
    lec19_american_in_troy.py. Rewrite the main code in this new file to list
    the names of all Restaurants in Troy that have American in their category
    and that have an average rating of more than 3.0. The only output should
    be the alphabetical list of restaurant names, one per line of output. The
    trick is that you are not allowed to change the Restaurant class at all.
    This will require that you access and use both one or two methods from
    Restaurant and some of its attributes directly. Upload your
    lec19_american_in_troy.py to Submitty when you are done. Submitty will use
    our Restaurant.py file to test.
"""

from Point2d import Point2d

class Restaurant(object):
    def __init__(self, name, lat, lon, address, url, category, scores):
        '''
        Initialize an object, including a name string, two floats to
        store the latitude and longitude, a list of strings to
        represent each line of an address, a string representing the
        url, a string representing the category of restaurant, and a
        list of scores.
        '''
        self.name = name
        self.loc = Point2d(float(lon), float(lat))
        self.address = address
        self.url = url
        self.category = category
        self.reviews = scores

    def __str__(self):
        '''
        Format the information about the restaurant as a multi-line string.
        Rather than outputing the whole list of reviews, the average review
        is output.
        '''
        s =  '      Name: ' + self.name + '\n'
        s += '  Lat/Long: ' + str(self.loc) + '\n'
        s += '   Address: ' + self.address[0] + '\n'
        for i in range(1,len(self.address)):
            s += '            ' + self.address[i]  + '\n'
        s += '  Category: ' + self.category + '\n'
        # s += 'Avg Review: {:.2f}'.format( self.average_review() )  + '\n'
        return s

    def is_in_city(self, city_name):
        '''
        Return True iff the restaurant is in the given city.  This is
        realized by testing the beginning of the last-line of the
        address (a list), up until the ,
        '''
        my_city = self.address[-1].split(',')[0].strip()
        return city_name == my_city

    def average_review(self):
        '''
        Calculate and return the average rating.  Return a -1 if there
        are none.
        '''
        if len(self.reviews) == 0:
            return -1
        else:
            return sum(self.reviews) / len(self.reviews)

    def min_review(self):
        '''
        Return the minimum review, and -1 if there are no reviews
        '''
        if (len(self.reviews) == 0):
            return -1
        else:
            return min(self.reviews)

    def max_review(self):
        '''
        Return the maximum review, and -1 if there are no reviews
        '''
        if (len(self.reviews) == 0):
            return -1
        else:
            return max(self.reviews)

    def latitude(self):
        '''
        Return the latitude stored in the Point2d object
        '''
        return self.loc.y

    def longitude(self):
        '''
        Return the longitude stored in the Point2d object
        '''
        return self.loc.x

def convert_to_restaurant(line):
    m = line.strip().split("|")
    name = m[0]
    latitude = float(m[1])
    longitude = float(m[2])
    address = m[3].split("+")
    url = m[4]
    restaurant_type = m[5]
    reviews = []
    for r in m[6:]:
        reviews.append(int(r))
    return Restaurant(name, latitude, longitude, address, url, restaurant_type, reviews)

def restaurant_list(file_name):
    restaurants = []
    for line in open(file_name):
        restaurants.append(convert_to_restaurant(line))
    
    return restaurants

if __name__ == "__main__":
    """
    This is relatively minimal testing code for the Restaurant class.
    Observe that when you import the Restaurant into the lecture 19
    example programs, this code is not run.
    """

    file_name = "yelp.txt"
    restaurants = restaurant_list(file_name)
    
    
    """for i in range(len(restaurants)):
        print(restaurants[i].average_review())"""
    
    
    
    finalNameList = []
    for x in range(len(restaurants)):
        if ("American" in restaurants[x].category) and (restaurants[x].average_review() > 3.0) and ("Troy" in restaurants[x].address[1]):
            finalNameList.append(restaurants[x].name)
        
    finalNameList.sort()
    
    for x in finalNameList:
        print(x)