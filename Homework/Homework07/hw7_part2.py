#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 08:57:48 2021

@author: maxrueda

Rueda, Maximillian
11/11/21
CSCI 1100
Homework 7.2 - Well-Rated and Not-So-Well-Rated Movies

This code...
"""

import json



def get_genres(movies):
    genreSet = set()
    for movieDict in movies.values():
        for genre in movieDict["genre"]:
            genreSet.add(genre.lower())
    
    return genreSet

def get_movies(minYear, maxYear, genre, movies):
    shortMovieDict = dict()
    for movieID in movies.keys():
        if (movies[movieID]["movie_year"] >= minYear) \
       and (movies[movieID]["movie_year"] <= maxYear) \
       and (genre.title() in movies[movieID]["genre"]):
            shortMovieDict[movieID] = movies[movieID]
    
    return shortMovieDict

def rating(movieID, shortMovies, ratings, w1, w2):
    imdbRating = shortMovies[movieID]['rating']
    twitRating = sum(ratings[movieID]) / len(ratings[movieID])
    combRating = (w1 * imdbRating + w2 * twitRating) / (w1 + w2)
    
    return combRating



if __name__=="__main__":
    minYear = int(input("Min year => ").strip())
    print(minYear)
    maxYear = int(input("Max year => ").strip())
    print(maxYear)
    w1 = (input("Weight for IMDB => ").strip())
    print(w1)
    w1 = float(w1)
    w2 = float(input("Weight for Twitter => ").strip())
    print(w2)
    
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    
    genreSet = get_genres(movies)
    
    
    while True:
        print("")
        genre = input("What genre do you want to see? ").strip()
        print(genre)
        
        if (genre.lower() == "stop"):
            break
      
        elif (genre.lower() not in genreSet):
            print("")
            print("No {} movie found in {} through {}".format(genre.title(), minYear, maxYear))
            continue
        
        else:
            shortMovies = get_movies(minYear, maxYear, genre, movies)
            
            finalList = []
            for movieID in shortMovies:
                if (movieID in ratings) and (len(ratings[movieID]) >= 3):
                    combRating = rating(movieID, shortMovies, ratings, w1, w2)
                    finalList.append((shortMovies[movieID]["movie_year"], shortMovies[movieID]["name"], combRating))
            
            
            bestYear = 0
            bestMovie = ""
            bestScore = 0
            worstYear = 0
            worstMovie = ""
            worstScore = 10
            for finalTup in finalList:
                if (finalTup[2] >= bestScore):
                    bestYear = finalTup[0]
                    bestMovie = finalTup[1]
                    bestScore = finalTup[2]
                if (finalTup[2] <= worstScore):
                    worstYear = finalTup[0]
                    worstMovie = finalTup[1]
                    worstScore = finalTup[2]
            
            if (bestMovie == ""):
                print("")
                print("No {} movie found in {} through {}".format(genre.title(), minYear, maxYear))
            else:
                print("")
                print("Best:")
                print(" "*8 + "Released in {}, {} has a rating of {:.2f}".format(bestYear, bestMovie, bestScore))
                print("")
                print("Worst:")
                print(" "*8 + "Released in {}, {} has a rating of {:.2f}".format(worstYear, worstMovie, worstScore))