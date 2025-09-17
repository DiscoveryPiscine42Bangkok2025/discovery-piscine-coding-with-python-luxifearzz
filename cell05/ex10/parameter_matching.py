#!/usr/bin/python3
import sys

params = sys.argv[1:]

if (len(params) != 1):
    print("none")
else:
    user_input = input("What was the parameter? ")
    if (params[0] == user_input):
        print("Good job!")
    else:
        print("Nope, sorry...")
