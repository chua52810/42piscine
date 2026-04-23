#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("None")
else: 
    print(f"Parameters: {len(sys.argv)-1}") 	
    for n in range (1, len(sys.argv)):
        print(f"{sys.argv[n]}: {len(sys.argv[n])}")
    print()
