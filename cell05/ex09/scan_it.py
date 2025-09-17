#!/usr/bin/python3
import sys, re

params = sys.argv[1:]
if (len(params) != 2):
    print("none")
else:
    result = re.findall(params[0], params[1])
    print(len(result) or "none")
