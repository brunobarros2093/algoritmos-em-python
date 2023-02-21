#!/usr/bin/venv python3

import sys 

#EAFP - EASY TO ASK FORGIVENESS THAN PERMISSION 
try:
    names = open("names.txt").readlines() #FileNotFoundError
except FileNotFoundError: #bare except 
    print("[error] file not found")

try:
    print(names[3])
except:
    print("Missing Name")
    sys.exit()
