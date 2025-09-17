#!/usr/bin/python3
import sys

params = sys.argv[1:]

if (len(params) != 2):
    print("none")
else:
    range_from_params = list(range(int(params[0]), int(params[1])+1))
    print(range_from_params)
