#!/usr/bin/python3
import sys

params = sys.argv[1:]
if (len(params) >= 1):
    print('\n'.join(params[::-1]))
else:
    print("none")
