#!/usr/bin/python
import sys
from random import shuffle
from copy import copy



def encrypt(text):
    alphabet = map(chr, range(32, 126))
    alphabet.append('\n')

    for char in text:
        if char not in alphabet:
            text = text.replace(char,'.')
    key = copy(alphabet)
    shuffle(key)
    f = open('key.txt','w')
    f.write(''.join(key))

    cypher = ""
    for char in text:
        index = alphabet.index(char)
        cypher += key[index]
    f = open('cypher.txt','w')
    f.write(cypher)

def decrypt(key, cypher):
    alphabet = map(chr, range(32, 126))
    alphabet.append('\n')

    key = list(key)
    clearText = ""
    for char in cypher:
        index = key.index(char)
        clearText += alphabet[index]
    f = open('clear.txt','w')
    f.write(clearText)

def main():
    # One parameter: encryption
    if len(sys.argv) == 2:
        with open(sys.argv[1], "r") as cleartextfile:
            cleartext=cleartextfile.read()
        encrypt(cleartext)
    # two parameters: decryption
    elif len(sys.argv) == 3:
        with open(sys.argv[1], "r") as keyfile:
            key=keyfile.read()
        with open(sys.argv[2], "r") as cypherfile:
            cypher=cypherfile.read()
        decrypt(key,cypher)
    else:
        print """how to encrypt using this monoalphabetic encryption tool: \n
                ./monoCrypt.py [/path/to/cleartext.txt] \n
                decryption: \n
                ./monoCrypt.py [/path/to/key.txt] [/path/to/cypher.txt]\n"""

if __name__ == "__main__":
    sys.exit(main())