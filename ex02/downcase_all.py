#!/usr/bin/env python3
import sys

class downcase_it:
    def to_lower(str_word):
        return str_word.lower()

if len(sys.argv) < 2:
    print("None")  
else: 
    for n in range(1, len(sys.argv)):
        str_word = sys.argv[n]
        print(downcase_it.to_lower(str_word))
    print()
