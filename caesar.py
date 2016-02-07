#!/usr/bin/python
"""
CSEC-362-01 - Crypto and Authentication
Professor Chaim Sanders a.k.a Col. Sanders
Nikko Williard and Sonjay Sivarajah
February 6, 2016
"""

"""
All user Prompts
"""
message = ''
key = ''

def prompt ():
    global message
    global key
    """
    Prompts user for a message
    (Plaintext or ciphertext)
    """
    message = raw_input('Message: ').lower()

    """
    Prompts user for an
    interger key to encrypt with
    """
    key = raw_input('Key: ')

"""
Encryption method
"""
def encryption (message, key):
    """
    Need to convert the string to individual chars and add the key
    to the chars, then join back to a string. (i think)
    """
    ret = ""
    for char in message:
        """
        rotation testing
        """
        ret += chr((ord(char) - ord('a') + int(key) % 26) + ord('a'))
    print ret
    exit()
"""
Decryption method
"""
def decryption (message,key):
    ret = ""
    for char in message:
        var = (ord(char) - int(key)) % 26
        if var < 33:
            var += 33
        if var < 0:
            var += 126
        ret += chr(var)
    print ret
    exit()
"""
Prompts the user if they would like
to encrypt or decrypt the text.
"""
while True:
    method = raw_input('(E)ncryption or (D)ecryption? ')
    if method[0].strip() == "e":
        prompt()
        encryption(message,key)
    elif method[0].strip() == "d":
        prompt()
        decryption(message,key)
    else:
        pass
