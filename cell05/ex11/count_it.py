#!/usr/bin/python3
import sys

params = sys.argv[1:]
len_params = len(params)

if (len_params < 1):
    print("none")
else:
    print("parameters:", len_params)
    for param in params:
        print(f"{param}: {len(param)}")
