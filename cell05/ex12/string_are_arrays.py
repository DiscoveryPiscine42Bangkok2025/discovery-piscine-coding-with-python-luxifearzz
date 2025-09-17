#!/usr/bin/python3
import sys, re

params = sys.argv[1:]

if (len(params) != 1):
    print("none")
else:
    string = params[0]
    zs = re.findall('z', string)
    print(''.join(zs) if len(zs) > 0 else "none")
