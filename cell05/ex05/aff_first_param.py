#!/usr/bin/python3
import sys

params = sys.argv[1:]
if (len(params) > 0):
    print(params[0])
else:
    print("none")
