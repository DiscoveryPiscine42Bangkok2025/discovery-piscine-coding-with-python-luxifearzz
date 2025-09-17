#!/usr/bin/python3
import sys

params = sys.argv[1:]
len_params = len(params)

if (len_params < 1):
    print("none")
else:
    for param in params:
        if (param.endswith("ism")):
            print(param)
        else:
            print(param + "ism")
