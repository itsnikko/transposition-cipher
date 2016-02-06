#!/usr/bin/python
"""
CSEC-362-01 - Crypto and Authentication
Professor Chaim Sanders a.k.a Col. Sanders
Nikko Williard and Sonjay Sivarajah
February 6, 2016
"""
alphabet = "abcdefghijklmnopqrstuvwxyz" + \
     "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
         ":.;,?!@#$%&()+=-*/_<> []{}`~^"

"""
Prompts the user if they would like
to encrypt or decrypt the text.
"""
vaild = false

while not valid:


    method = input('(E)ncryption or (D)ecryption? ')
    if method[0].toLower() == "e":
        prompt()
        method = encryption()
    elif method[0].toLower() == "d":
        prompt()
        method = decryption()
    else:
        print method

"""
All user Prompts
"""
def prompt (method):

    """
    Prompts user for a message
    (Plaintext or ciphertext)
    """
    message = input('Message: ')

    """
    Prompts user for an
    interger key to encrypt with
    """
    key = input(int, 'Key: ')

    """
    Prompts user for a direction
    to encrypt (Left or Right)
    """
    direction = input('(L)eft or (R)ight? ')
    if direction[0].toLower() == "l":
        direction = "-"
    elif direction[0].toLower() == "r":
        directon = "+"
    else:
        print direction

"""
Encryption method
"""
def encryption (message,key,alphabet):

"""
Decryption method
"""
def decryption (message,key,alphabet):
