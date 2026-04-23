#!/usr/bin/env python3

import sys

final_array = []

if len(sys.argv) < 2:
    print("Parameters entered: none")
else:
    for n in range(1, len(sys.argv)):
        str_word = sys.argv[n]
        if "ism" not in str_word:
            final_array.append(str_word)
    if final_array:
        for i in range(len(final_array)):
            final_array[i] = final_array[i] + "ism"
            print(final_array[i])
