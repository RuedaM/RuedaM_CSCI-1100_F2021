#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 17:32:52 2021

@author: maxrueda
11/05/21
CSCI 1100
Lect. Exercises 17.2 - IMDb Most People
"""

"""
2. Write a Python program that finds the name of the movie in our Internet
    Movie Database that involved the most unique individuals. Print the number
    of individuals on one line and the name of the movie on the next line. You
    do not need to consider the possibility of ties and you should assume all
    actors and movies have the correct capitalization. Finally, print the
    number of movies involving only one individual (yes, there are such
    movies). For example, if the name of the movie is Ben Hur with 2,342
    individuals, and 165 movies have only one individual then the output from
    your program will look like:
Enter the name of the IMDB file ==> imdb_data.txt
2342
Ben Hur
165
   Note that you only need to create one dictionary for this exercise. Start
    by planning the organization of this dictionary and thinking through how
    you are going to use it. As with Lecture Exercises 16, make sure you use
    dict() to initialize your empty dictionary
"""

imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

movies = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    
    if movie in movies:
        movies[movie].add(name)
    else:
        movies[movie] = set()
        movies[movie].add(name)

mostActors = 0
for movie in movies:
    if (len(movies[movie]) > mostActors):
        mostActors = len(movies[movie])
        mAMovie = movie
print(mostActors)
print(mAMovie)

soloCount = 0
for movie in movies:
    if (len(movies[movie]) == 1):
        soloCount += 1
print(soloCount)