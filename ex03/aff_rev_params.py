#!/usr/bin/env python3
import sys

if len(sys.argv) > 2:
    for n in range (len(sys.argv)-1,0,-1):
        print(sys.argv[n])
else:
    print("Parameters entered: none")
