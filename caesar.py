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
All user Prompts
"""
def prompt ():

    """
    Prompts user for a message
    (Plaintext or ciphertext)
    """
    message = raw_input('Message: ')

    """
    Prompts user for an
    interger key to encrypt with
    """
    key = raw_input('Key: ')

    """
    Prompts user for a direction
    to encrypt (Left or Right)
    """
    direction = raw_input('(L)eft or (R)ight? ')
    if direction[0].strip() == "l":
        direction = "-"
    elif direction[0].strip() == "r":
        direction = "+"
    else:
        print direction

"""
Encryption method
"""
def encryption (message, key, alphabet):
""" Need to convert the string to individual chars and add the key
to the chars, then join back to a string. (i think)
"""
    return" ".join(str(ord(char)) for char in message)
"""
Decryption method
"""
def decryption (message,key,alphabet):
    pass

"""
Prompts the user if they would like
to encrypt or decrypt the text.
"""
while True:
    method = raw_input('(E)ncryption or (D)ecryption? ')
    if method[0].strip() == "e":
        prompt()
        encryption()
    elif method[0].strip() == "d":
        prompt()
        decryption()
    else:
        pass
