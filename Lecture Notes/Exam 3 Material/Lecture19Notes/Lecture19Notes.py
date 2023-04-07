#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:36:21 2021

@author: maxrueda
"""

"---Lecture 19 — Classes, Part 2---"

"Overview"
#Review of classes
#Revisiting our Yelp data: a Restaurant class.
#Techniques that we will see:
#   Calling class methods from within the class
#   Class objects storing other objects, such as lists
#   Lists of class objects


"Review of Classes"
#We will use our Point2d class solution from Lect.18 to review the following:

#Attributes:
#   These store the data associated with each class instance
#   They are usually defined inside the class to create a common set of
#    attributes across all class instances
#Initialization:
#   Function __init__ called when the object is created
#   Should assign initial values to all attributes
#Methods:
#   Each includes the object, often referred to as self, as the first argument
#   Some change the object, some create new objects

#Special methods start and end with two underscores
#Python interprets their use in a variety of distinct ways:
#   __str__ is the string conversion function
#   __add__, __sub__, etc. become operators

#Each of these special methods builds on the “more primitive” methods


"Larger Example — Restaurant Class"
#Recall Lab 5 on the Yelp data:
#   Read and parse input lines that look like:
"""
The Greek House|42.73|-73.69|27 3rd St+Troy, NY 12180|\
   http://www.yelp.com/biz/the-greek-house-troy|Greek|1|5|4|5|4|4|5|5|5|5|5|4
"""
#   Find restaurants and print out information based on a user selection
#   Original implementation based on a list was awkward:
#       We had to remember the role of each index of the list — 0 was the name,
#        1 was the latitude, etc.
#New implementation here is based on a class


"Start to a Solution, the Main Code"
#Let’s look at lec19_restaurants_exercise.py, downloadable as part of the
# Lecture_19 zip file in the Course Materials section of Submitty:

#This is the code that uses the Restaurant class.
#   We start by considering how the class will be used rather than how we
#    write it
#Main function to initialize a restaurant is called convert_input_to_restaurant
#   Parses a restaurant line
#   Creates and returns a Restaurant object
#Function build_restaurant_list
#   Opens the input file
#   Reads each line
#   Calls convert_input_to_restaurant, and appends the resulting restaurant to
#    the back of a list
#Main code:
#   Builds the restaurant list
#   Prints the first three restaurants in the list
#   Includes commented-out code that:
#       Gets the name of a city
#       Finds the restaurant with the highest average rating

#We will complete this code soon.


"Functionality Needed in the Restaurant Class"
#Some functionality is determined by reading the code we have already written
#   Includes both methods and attributes

#Add other functionality by considering the methods that must be in the
# Restaurant class, including the parameters that must be passed to each
# method.

#Add attributes last…


"Turning to the Actual Restaurant Class"
#Look at Restaurant.py which was distributed with the Lecture_19 files.

#The __init__ function specifies the attributes.
#   Other attributes could be added, such as the average rating, but instead
#    these are computed as needed by methods.
#   Importantly, each class object stores a list of ratings, illustrating the
#    fact that classes can store data structures such as lists, sets, and
#    dictionaries.

#The Restaurant class has more complicated attributes than our previous objects
#   Point2d object,
#   A list for the address entries
#   A list of scores

#There is nothing special about working with these attributes other than they
# “feel” more complicated.
#   Just apply what you know in using them
#   Our lecture exercises will help

from LectEx18_2 import Point2d

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
        pass

    def max_review(self):
        '''
        Return the maximum review, and -1 if there are no reviews
        '''
        pass

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

if __name__ == "__main__":
    """
    This is relatively minimal testing code for the Restaurant class.
    Observe that when you import the Restaurant into the lecture 19
    example programs, this code is not run.
    """

    n = "Uncle Ricky's Bagel Heaven"
    lat = 42.73
    lon = -73.69
    address = [ '1809 5th Ave', 'Troy, NY 12180']
    url = "http://www.yelp.com/biz/uncle-rickys-bagel-heaven-troy"
    rest_type = 'Bagels'
    reviews = [ 5, 3, 5, 4, 3, 5, 4 ]
    rest1 = Restaurant( n, lat, lon, address, url, rest_type, reviews )

    n = "No Longer In Business"
    lat = 42.74
    lon = -73.7
    address = [ '123 Nowhere Street', 'Troy, NY 12180']
    url = "http://www.not_a_valid_url.biz/snafu"
    rest_type = 'Concrete'
    reviews = [ ]
    rest2 = Restaurant( n, lat, lon, address, url, rest_type, reviews )

    print("First restaurant:")
    print("Name:", rest1.name)
    print("Latitude:", rest1.latitude() )
    print("Longitude:", rest1.longitude() )
    print("Min review:", rest1.min_review() )
    print("Max review:", rest1.max_review() )

    print("\nSecond restaurant:")
    print("Name:", rest2.name)
    print("Latitude:", rest2.latitude() )
    print("Longitude:", rest2.longitude() )
    print("Min review:", rest2.min_review() )
    print("Max review:", rest2.max_review() )

"In-Class Example"
#Together we will add the following two methods to Restaurant to get our
# demonstration example to work:
#   1. The is_in_city method
#   2. The average_review method


"Discussion"
#What is not in the Restaurant class?
#   No input or line parsing. Usually, we don’t want the class tied to the
#    particular form of the input.
#   As an alternative, we could add a method for each of several different
#    forms of input.

#Often it is hard to make the decision about what should be inside and what
# should be outside the class.
#   One example the method we wrote to test if restaurant is in a particular
#    city. As an alternative we could have written a different method that
#    returns that name of the city and make the comparison outside the class.

#We could add an Address class:
#   Reuse for objects other than restaurants
#   Not needed in this (relatively) short example.
#   More flexible than our use of a list of strings from an address line.


"Summary"
#Review of the main components of a Python class:
#   Attributes
#   Methods
#   Special methods with names starting/ending with "__"
#       Initializer method is most important
#Important uses of Python classes that we have seen today:
#   Classes containing other objects as attributes
#   Lists of class objects.
#Design of Python classes
#   Start by outlining how they are to be used
#   Leads to design of methods
#   Specification of attributes and implementation of methods comes last