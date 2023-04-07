#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 15:40:57 2021

@author: maxrueda
10/19/21
CSCI 1100
Lect. Exercises 13.2
"""

"""
2. Given a file containing test scores, one per line, we want to have a new
    file that contains the scores in increasing order. To do this, write a
    Python program that asks the user for two file name strings, one for the
    input scores and the second for the output, sorted scores. The program
    should open the first file (to read), read the scores, sort them, open the
    second file (to write), and output to this file the scores in increasing
    order. There should be one score per line, with the index on each line.

    As an example, suppose the input file is scores.txt and it contains:
75
98
75
100
21
66
83
15

    then running your program should look like (in Spyder):
Enter the scores file: scores.txt
scores.txt
Enter the output file: scores_sorted.txt
scores_sorted.txt

    When you look at the contents of scores_sorted.txt you should see
0:  15
1:  21
2:  66
3:  75
4:  75
5:  83
6:  98
7: 100

    (Output the indices using two integer spaces {:2d} and the scores using
     three {:3d}.) You only need to submit the Python file. We will test with
     the example above and with a new file you have not seen.
"""

file1 = input("Enter the scores file: ").strip()
print(file1)
file2 = input("Enter the output file: ").strip()
print(file2)

valuesList = []

inputFile = open(file1, "r")
for line in inputFile:
    valuesList.append(int(line.strip()))
inputFile.close()

valuesList.sort()


outputFile = open(file2, "w")

for index in range(len(valuesList)):
    outputFile.write("{:2d}: {:3d}\n".format(index, valuesList[index]))
outputFile.close()