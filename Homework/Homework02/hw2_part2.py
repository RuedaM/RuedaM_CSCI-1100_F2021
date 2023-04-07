#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:07:42 2021

@author: maxrueda

Rueda, Maximillian
9/23/21
CSCI 1100
Homework 2.2
"""



def encrypt(word):
    word = word.replace(" a","%4%")
    word = word.replace("he","7!")
    word = word.replace("e","9(*9(")
    word = word.replace("y","*%$")
    word = word.replace("u","@@@")
    word = word.replace("an","-?")
    word = word.replace("th","!@+3")
    word = word.replace("o","7654")
    word = word.replace("9","2")
    word = word.replace("ck","%4")
    return word
    
def decrypt(word):
    word = word.replace("%4","ck")
    word = word.replace("2","9")
    word = word.replace("7654","o")
    word = word.replace("!@+3","th")
    word = word.replace("-?","an")
    word = word.replace("@@@","u")
    word = word.replace("*%$","y")
    word = word.replace("9(*9(","e")
    word = word.replace("7!","he")
    word = word.replace("%4%"," a")
    return word
    

String = input("Enter a string to encode ==> ")
print(String)
print()


EncryptedString = encrypt(String)
print("Encrypted as ==>", EncryptedString)


DifferentLength = abs(len(String) - len(EncryptedString))
print("Difference in length ==>", DifferentLength)


DecryptedString = decrypt(EncryptedString)
print("Deciphered as ==>", DecryptedString)


if DecryptedString == String:
    print("Operation is reversible on the string.")
else:
    print("Operation is not reversible on the string.")