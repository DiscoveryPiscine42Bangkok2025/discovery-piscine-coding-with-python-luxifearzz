#!/usr/bin/python3
import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    len_string = len(string)
    while (len_string < 8):
        string += 'Z'
        len_string += 1
    print(string)

params = sys.argv[1:]

if (len(params) < 1):
    print("none")
else:
    for param in params:
        len_param = len(param)
        if (len_param < 8):
            enlarge(param)
        elif (len_param > 8):
            shrink(param)
        else:
            print(param)
