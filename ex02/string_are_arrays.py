#!/usr/bin/env python3
import sys, re

if len(sys.argv) < 2:
    print("None")
else: 
    str_key = "z"
    str_word = sys.argv[1]
    result = re.findall(re.escape(str_key), str_word)
    str_finalz = "z" * len(result) 
    print(f"{len(result)} {str_finalz}")
print()
