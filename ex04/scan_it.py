#!/usr/bin/env python3

import sys, re

if len(sys.argv) < 3:
    print("Parameters entered: none")
elif len(sys.argv) > 3: 
    print("Too many parameters entered!")
else:
    str_key = sys.argv[1]
    str_word = sys.argv[2]
    result = re.findall(re.escape(str_key), str_word, re.IGNORECASE) 
    print(len(result))
print()
