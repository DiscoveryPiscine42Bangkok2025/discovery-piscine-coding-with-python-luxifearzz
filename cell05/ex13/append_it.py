#!/usr/bin/python3
import sys

params = sys.argv[1:]
len_params = len(params)

if (len_params < 1):
    print("none")
else:
    for param in params:
        if (not param.endswith("ism")):
            print(param + "ism")
