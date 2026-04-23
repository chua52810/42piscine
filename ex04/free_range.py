#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("None")
elif sys.argv[1] > sys.argv[2]:
    print("Error! First number need to be smaller than second number")
else:
    new_array = []
    for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
        new_array.append(i)
    print(new_array)
