#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("None")
else: 
    str_ans=input("What was the the parameter? ")
    if str_ans == sys.argv[1]:
    	print("Good job!")    	
    else:
    	print("Nope, sorry...")
    print()
