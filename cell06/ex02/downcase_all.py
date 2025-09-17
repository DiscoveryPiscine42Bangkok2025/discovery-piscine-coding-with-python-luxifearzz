#!/usr/bin/python3
import sys

def downcase_it(string):
    return string.lower()

params = sys.argv[1:]

if (len(params) < 1):
    print("none")
else:
    for param in params:
        print(downcase_it(param))
