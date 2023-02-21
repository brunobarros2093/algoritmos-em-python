#!/usr/bin/venv python3


names = open("names.txt").readlines()
#LBYL - Look Before You Leap
if len(names) >= 3:
    print(names[1])
