#!/usr/bin/env python3
import sys

final_words = []

if len(sys.argv) > 1:
    for n in range (1, len(sys.argv)):
        str_converted = ""
        for char in sys.argv[n]:
            if char.isupper():
                str_converted += char.lower()
            else:
                str_converted += char
        final_words.append(str_converted)  	                
    print(" ".join(final_words))
    print()
else:
    print("Parameters entered: none")    
