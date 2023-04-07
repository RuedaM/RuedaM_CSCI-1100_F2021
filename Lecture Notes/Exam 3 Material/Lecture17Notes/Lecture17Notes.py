#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:52:20 2021

@author: maxrueda
"""

"---Lecture 17 Notes — Dictionaries, Part 2---"

"Overview"
#Recap
#More IMDB examples:
#   Dictionaries of string/set pairs
#   Converting dictionaries with one key to another
#   Combining information from multiple dictionaries
#A different view of dictionaries: storing attribute/value pairs.
#Accessing APIs and getting data back as a dictionary.


"Recap of dictionaries"
#On the surface, dictionaries look like lists, except, you can have anything
# for indices (keys), not just numbers starting with 0

#The following two store the same information:
listoption = ['a','b','c']
dictoption = {0:'a', 1: 'b', 2:'c'}
#Note that this is a new way for us to initialize a dictionary

#You would access them in the same way:
print(listoption[1])
print(dictoption[1])
print("")

#And you would update them in the same way:
listoption[1] = 'd'
dictoption[1] = 'd'
print(listoption[1])
print(dictoption[1])
print("")

#But you CANNOT extend them in the same way. For example:
"""listoption[10] = 'e'"""
# is illegal, but:

dictoption[10] = 'e'
# is perfectly fine. Be sure you can explain why.
#   You can only change list values that are within the range of indices of
#    the list - 10 isn't an index of the list (which only goes up to 2 indices)
#    so 'e' cannot be appended


#Of course the power of a dictionary is that keys can be anything, or at least
# anything hashable:
d = {'Gru':3, 'Margo':4}
print(d['Gru'])
print()

#This dictionary has strings as keys and integers as values. The values can
# really be anything:
d2 = {'Gru': set( [123,456] ), 'Margo': set( [456] ) }
print(d2['Gru'])
print("")

#Note that since keys can be anything, we need to know how to print or iterate
# through the values in a dictionary. This is actually quite trivial using a
# dictionary:

print(d2.keys())
d2KeyList = list(d2.keys())
print(d2KeyList)
for key in d2:   #  or, for key in d2.keys():
    print(key, d2[key])
print("")
print("")


"Copying and Aliasing Dictionaries"
#We’ll take a few minutes in class for you to try to predict the output of the
# following:
d = dict()          #Create a new dict
d[15] = 'hi'        #Adding a key+value to the dict
L = []              #Creating an empty list
L.append(d)         #Appending the dict into our new list
d[20] = 'bye'       #Adding another key+value to the dict inside the list
L.append(d.copy())  #Appending a copy of d to the list
d[15] = 'hello'     #Adding another key+value to the dict - but which one?
del d[20]           #Deleting they key+value at key 20 - but which dict?
print(L)            # [{15: 'hello'}, {15: 'hi', 20: 'bye'}] ???
print("")

#The result may surprise you, but it reflects the difference between making an
# alias to an object and making a full copy of an object - the line d.copy()
# is an entirely new object separate from the actual dict
#  We did not assign the copy to a variable, so it just exists in space - any
#   call of d2 will only refer to the original, not the copy.alias

#Let's see what happens for each step:
d = dict()
d[15] = 'hi'
L = []
L.append(d)
print(L)
d[20] = 'bye'
print(L)
L.append(d.copy())
print(L)
d[15] = 'hello'
print(L)
del d[20]
print(L)
print("")
print("")

#An alias is also sometimes known as a shallow copy
#A full copy is also sometimes known as a deep copy
#Assignment between lists, between sets, and between dictionaries all involve
# aliasing / shallow copying!

#At this point we will take a few minutes for you to work on the first lecture
# exercise.


"Back to IMDB: Dictionaries Whose Values Are Sets"
#In our IMDB data, an individual may be listed more than once for each movie.
# For example, Tom Hanks is listed six times for Polar Express
#In order to determine who was involved in the most different movies, we need
# to keep a set of movies for each individual instead of a count
#We will modify our solution to the IMDB example to find out who was involved
# in the most different movies:
imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

'''
Generate first dictionary by parsing lines of in-file.
Take actor's name as key, add movie name into set of movies associated w/ them
'''
movies = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    
    if name in movies:
        movies[name].add(movie)
    else:
        movies[name] = set()
        movies[name].add(movie)
'''
Look through dict, see how many actors appeared in only one unique movie and
 which actor was busiest based on associations w/ unique movies
'''
singlets = 0
most = 0
for name in movies:
    movie_ct = len(movies[name])
    if movie_ct == 1:
        singlets += 1
    if movie_ct > most:
        most = movie_ct
        person = name
        
print("{} appears most often: {} times".format(person, most))
print("{} people appear once".format(singlets))
print("")
print("")

"Converting to Other Dictionaries: The N Busiest Individuals"
#Suppose we want to find the top 10 or 25 busiest individuals in the IMDB,
# based on the number of different movies they are involved in
#Now we need a different dictionary:
#   Keys are integers representing the number of movies
#   Values are lists of actors.
#       Why don’t we need sets here?

#We will show how to extend our code to build this dictionary from our
# original dictionary

#Next, we will need to access the keys from this dictionary in reverse
# lexicographical order (last to first) and print out names of the individuals,
# stopping when we’ve printed the top N busiest (allowing more in the case of
# ties)
imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

'''
Generate first dictionary by parsing lines of in-file.
Take actor's name as key, add movie name into set of movies associated w/ actor
'''
movies = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    
    if name in movies:
        movies[name].add(movie)
    else:
        movies[name] = set()
        movies[name].add(movie)

'''
Cycle through movies dictionary to get data for new dictionary.
This time, for every actor, calculate how many movies they were associated with
 by taking length of set indicated by movies[name], which becomes a key in
 actors dictionary where everyone who is associated with length number of
 movies is stored in a list.
'''
actors = dict()
for name in movies:
    movie_ct = len(movies[name])
    if movie_ct not in actors:
        actors[movie_ct] = []
        actors[movie_ct].append(name)
    else:
        actors[movie_ct].append(name)

'''
Sort actors dictionary from highest (most # of movies) to lowest (least #).
Print top 25 actors by number of movies they are associated with.
'''
keys = sorted(actors, reverse=True)
i = 0
count = 0
while count < 25 and i < len(keys): 
    print(keys[i], actors[keys[i]])
    count += len(actors[keys[i]])
    i += 1
print("")
print("")

"More That We Can Do With the IMDB"
#We now have an actors dictionary whose keys are actor names and whose values
# are sets of movies

#We can also construct a different dictionary whose keys are movies and whose
# values are sets of actors

#Using this we can find all sorts of information:
#   What movie involved the most people?
#   How many different people have been in movies that included Meryl Streep?
#   Solve the “degrees of Kevin Bacon” problem:
#       Who has been in a movie with Kevin Bacon? These people are degree 1.
#       Who is not a deg. 1 individual and has been in a movie with a person
#        who was in a movie with Kevin Bacon? These people are degree 2 indivs.
#       etc.

"""DO THESE EXAMPLES --- FOUND IN PART 3 VIDEO"""


"Attribute / Value Pairs"
#We can use dictionaries to construct even more complicated data structures:
# dictionaries as values, lists of dictionaries, etc.

#Consider the problem of representing all the houses a real estate company is
# trying to sell
#We could keep a list with information about each property, but a list of what?

#We will look at describing each house as a dictionary, with the keys being
# the “attributes”, and the values being, well, the values of the attributes

#Examples include the listing reference number, the address, the number of
# bedrooms, the price, whether or not it has a pool, the style of the house,
# the age, etc.
#   Some properties will not be known and therefore they will not be
#    represented in the dictionary

#We will work through a made-up example in class, producing a list of
# dictionaries. This list will be called houses

#As an exercise you can think about write coding that finds all houses in our
# house list that have at least 4 bedrooms (attribute is bedrooms, value is an
# integer), a pool (attribute is pool, value a string describing if the pool
# is above ground or below), for a price below $300,000 (atttribute is price,
# value is an int)

#Overall, this a simple Python implementation of the storage and access of
# information in a database.

"Accessing APIs"
#Many APIs (Application Programming Interfaces) accessible on the Internet
# return values that are JSON (Java Script Object Notation) strings. These are
# easily loaded into Python objects, often involving dictionaries

#The best way to understand the dictionary structure returned by an API is to
# seek documentation. If that fails, you can print the top level keys and
# values to explore

#Public APIs, which do not not require authentication, are accessed as follows:
"""
import urllib.request
import json

url = "enter your public url here"
f = urllib.request.urlopen(url)
rawcontent = f.read()
content = json.loads(rawcontent.decode("utf-8"))
"""

#An example of a public API:
#nominatim gives you a bounding box of geolocation for a given location. Let’s
# see this for ‘Troy, NY’:
"""
import urllib.request
import json

url = "http://nominatim.openstreetmap.org/"\
      "search?q={}&format=json&polygon_geojson=1&addressdetails=0"\
      .format('Troy,NY')
f = urllib.request.urlopen(url)
rawcontent = f.read()
content = json.loads(rawcontent.decode("utf-8"))
"""
#Many sources require authentication with an API key through the oauth2
# authentication module. But, the overall method of access remains the same
# after authentication

#Once we understand the structure, we can write code to extract the
# information we want.


"Final Example"
#Given the following dictionary for hobbies for people:
hobby = {'Gru':set(['Hiking','Cooking']), 'Edith':set(['Hiking','Board Games'])}

#create a new dictionary that lists people for each hobby:
#{'Hiking': {'Gru','Edith'}, 'Cooking':{'Gru'}, 'Board Games':{'Edith'}}

hobby = {'Gru':set(['Hiking','Cooking']), 'Edith':set(['Hiking','Board Games'])}

new = dict()
temp = set()
for i in hobby:
    temp = temp|hobby[i]
print(temp)
for i in hobby:
    for j in list(temp):
        if (j in new):
            new[j].add(i)
        else:
            new[j] = set()
            new[j].add(i)
print(new)


"---SUMMARY---"
#Dictionaries of sets.
#Dictionaries where the keys are numbers.
#A variety of examples to extract information from the IMDB data set.
#Dictionaries as database — storing attribute / value pairs.
#Accessing information from public APIs