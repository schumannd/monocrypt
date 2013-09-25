#!/usr/bin/python
import sys
from random import shuffle
from copy import copy

alphabet = map(chr, range(32, 126))
alphabet.append('\n')

def removeUnsupportedCharacters(text):
    for char in text:
        if char not in alphabet:
            text = text.replace(char,'.')
    return text

def swapCharactersInText(text, alphabet1, alphabet2):
    convertedText = ""
    for char in text:
        index = alphabet1.index(char)
        convertedText += alphabet2[index]
    return convertedText

def encrypt(text):
    text = removeUnsupportedCharacters(text)

    key = copy(alphabet)
    shuffle(key)
    f = open('key.txt','w')
    f.write(''.join(key))

    cypher = swapCharactersInText(text, alphabet, key)
    f = open("cypher.txt",'w')
    f.write(cypher)

def decrypt(key, cypher):
    key = list(key)

    clearText = swapCharactersInText(cypher, key, alphabet)
    f = open("clear.txt",'w')
    f.write(clearText)

def readDecryptFiles():
    with open(sys.argv[1], "r") as cypherfile:
        cypher=cypherfile.read()
    with open(sys.argv[2], "r") as keyfile:
        key=keyfile.read()
    decrypt(key,cypher)

def readEncryptFile():
    with open(sys.argv[1], "r") as cleartextfile:
        cleartext=cleartextfile.read()
    encrypt(cleartext)

def main():
    if len(sys.argv) == 2:
        readEncryptFile()
    elif len(sys.argv) == 3:
        readDecryptFiles()
    else:
        print """
        how to encrypt using this monoalphabetic encryption tool:
        ./monoCrypt.py [/path/to/cleartext.txt] \n
        decryption:
        ./monoCrypt.py [/path/to/cypher.txt] [/path/to/key.txt] \n"""

if __name__ == "__main__":
    sys.exit(main())