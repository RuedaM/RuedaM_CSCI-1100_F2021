#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:05:27 2021

@author: maxrueda
"""

"---Lecture 16 Notes - Dictionaries, Part 1---"

"Overview"
#More on IMDB
#Dictionaries and dictionary operations
#Solutions to the problem of counting how many movies are associated with each
# individual
#Other applications


"How Many Movies is Each Person Involved In?"
#Goals:
#   Count movies for each person.
#   Who is the busiest?
#   What movies do two people have in common?

#Best solved with the notion of a dictionary, but we’ll at least consider how
# to use a list.


"List-Based Solution — Straightforward Version"
#Core data structure is a list of two-item lists, each giving a person’s name
# and the count of movies.

#For example, after reading the first seven lines of our shortened hanks.txt
# file, we would have the list:
exampleList = [["Hanks, Jim", 3], ["Hanks, Colin", 1], \
               ["Hanks, Bethan", 1], ["Hanks, Tom", 2]]

#Just like our solution from the sets lectures, we can start from the
# following code:
"""
imdb_file = input("Enter the name of the IMDB file ==> ").strip()
count_list = []
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    found = False
    for pair in count_list:
        if pair[0] == name:
            pair[1] += 1
            found = True
            break
        if not found:
            new_pair = [name, 1]
            count_list.append(new_pair)
            
for pair in count_list:
    print(pair[0], pair[1])
"""
    
#Like our list solution for finding all IMDB people, this solution is VERY
#slow — once again O(N^2) (“order of N squared”)
print("")
print("")
print("")


"List-Based Solution — Faster Version Based on Sorting"
#There is an alternate solution that would work for the number of unique names
# solution from lecture 15 as well. It is based on sorting

#Append each name to the end of the list without checking if it is already
# there
#After reading all of the movies, sort the entire resulting list
#   (As a result, all instances of each name will now be next to each other)
#Go back through the list, counting the occurrence of each name

#This solution will be much faster than the first, but it is also more
# involved to write than the one we are about to write using dictionaries


"Introduction to Dictionaries"
#Association between “keys” (like words in an English dictionary) and “values”
# (like definitions in an English dictionary). The values can be ANYTHING

#Dictionaries (dict) are object types such that there is a key and a
# corresponding value that gets created - a collection of key-value pairs

#Examples:
heights = dict()    #Either of these two works
heights = {}        #Notice the curly braces = similar to a set

#When adding items to a dictionary, the following is uesd:
"""dictVariable[key] = value"""

#Below, animal heights are stored in a dict where the name is the key and the
# height is the value:
heights['belgian horse'] = 162.6
heights['indian elephant'] = 280.0
heights['tiger'] = 91.0
heights['lion'] = 97.0
print(heights)
print("")
#This dict will be printed as {[key]: [value], [key]: [value], etc.}

#To check if a key exists within a dict, simplay ask:
print('tiger' in heights)
print('giraffe' in heights)
print(91.0 in heights)
print("")
print("")
#Notice how the 91.0 returned False - the "in" boolean condition will only
# read through keys, not values


#Why do we Need Dictionaries?
#All keys in a dict are unique and unordered (much like a set)
#Key words help make access to the values associated with them faster
#   Unlike a list, where you have to scan every element, you can quickly jump
#    to the value if you know the key word


#dicts can be typecasted - both the keys AND the values can be stored in lists
# to be used elsewhere:
print(heights.keys())
print(heights.values())
print("")

heightsKeyList = list(heights.keys())
print(heightsKeyList)
heightsKeyListSort = sorted(heights.keys())
print(heightsKeyListSort)
print("")

heightsValList = list(heights.values())
print(heightsValList)
print("")
print("")
print("")


#Details:
#Two initializations; dict() or like the creation of a set: var = {}
#Syntax is very much like the subscripting syntax for lists, except dictionary
# subscripting/indexing uses keys instead of integers!
#The keys, in this example, are animal species (or subspecies) names; the
# values are floats
#The in method/boolean tests only for the presence of the key, like looking up
# a word in the dictionary without checking its definition
#The keys ARE NOT ordered
#Just as in sets, the implementation uses HASHING of keys
#   Conceptually, sets are dictionaries without values


"Back to Our IMDB Problem"
#Even though our coverage of dictionaries has been brief, we already have
# enough tools to solve our problem of counting movies.
#Once again we’ll use the following as a starting point:
imdb_file = input("Enter the name of the IMDB file ==> ").strip()
counts = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if (name in counts):
        counts[name] += 1
    else:
        counts[name] = 1

names = sorted(counts)
limit = min(100, len(names))
for index in range(limit):
    name = names[index]
    print(name, counts[name])
    
#The solution we give in class will output the counts for the first 100
# individuals in alphabetical order - It will be up to you as an exercise to
# find the most frequently occuring individual

#We will impose an ordering on the output by sorting the keys
#We’ll test first on our smaller data set and then again later on larger ones


"Key Types"
#Thus far, the keys in our dictionary have been strings.
#Keys can be any “hashable” type — string, int, float, booleans, tuples
#Lists, sets and other dictionaries can not be keys

#Strings are by far the most common key type
#We will see an example of integers as the key type by the end of the Lecture
# 17 (next lecture)
#Float and boolean are generally poor choices. Can you think why?
#   There are only two options for boolean (T/F) and floats can go on and on


"Value Types"
#So far, the values in our dictionaries have been integers and floats, but ANY
# type can be values:
#booleans, ints, floats, strings, lists, tuples, sets, even other dictionaries

#Here is an example using our IMDB code and a set:
people = dict()
people['Hanks, Tom'] = set()
#A set is added to the dict - you can even add to the set from th dict
people['Hanks, Tom'].add('Big')
people['Hanks, Tom'].add('Splash')
people['Hanks, Tom'].add('Forest Gump')

print(people['Hanks, Tom'])
print("")
print("")

#Here is another example where we store the continent and the population for a
# country instead of just the population:
countries = dict()
countries.clear()
countries['Algeria'] =  (37100000, 'Africa')
countries['Canada'] = (34945200, 'North America' )
countries['Uganda'] = (32939800, 'Africa')
countries['Morocco'] = (32696600, 'Africa')
countries['Sudan'] = (30894000, 'Africa')
print(countries["Canada"][0])   #prints a population
print(countries["Canada"][1])   #prints a continent
#       /\dict   /\key   /\value
print("")
print("")

#We access the values in the entries using two consecutive subscripts
#For example:
name = "Canada"
print("The population of {} is {}".format(name, countries[name][0]))
print("It is in the continent of", countries[name][1])
print("")
print("")
print("")


"Removing Values: Sets and Dictionaries"
#For a set:
#   .discard() - removes specified element, does nothing if it isn't there
#   .remove() - removes specified element, but fails (ERROR) if it isn't there
s = {2, 3, 4, 5, 6}
s.discard(2)
print(s)
s.discard(10)
print(s)
s.remove(5)
print(s)
"""s.remove(5)"""   #would result in error
print("")
print("")
print("")

#For a dictionary, it is the del() function;
#For both sets and dictionaries, the .clear() method empties the container.

#We will look at toy examples in class


"Other Dictionary Methods"
#The following dictionary methods are useful, but not so much as the ones
# we’ve discussed"
#   .get()
#   .pop()
#   .popitem()
#   .update() - add a new key-value entry into a given dict
#                within the parenthesis, you can have [key]=[value] or
#                [key]:[value], with any pairs entered separated by commas

#Use the help() function in Python to figure out how to use them and to find
# other dictionary methods


"---SUMMARY---"
#Associate “keys” with “values”
#Feels like indexing, except we are using keys instead of integer indices
#Makes counting and a number of other operations simple and fast
#Keys can be any “hashable” value, usually strings, sometimes integers
#Values can any type whatsoever