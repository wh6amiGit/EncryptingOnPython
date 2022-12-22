#!usr/bin/python3

import os
import sys
import pyAesCrypt as crypt

decrypt_to_direct = str(input("Enter the director for decrypt ==> "))

def decrypt(file):
	password = '123'
	buffer_sz = 512*1024
	crypt.decryptFile(file, os.path.splitext(file)[0], password, buffer_sz)
	print(f"File {file} decrypt")
	os.remove(file)

def search(dir):
	for name in os.listdir(dir):
		path = os.path.join(dir, name)
		if os.path.isfile(path) == True:
			decrypt(path)
		else:
			search(path)

search(decrypt_to_direct)
