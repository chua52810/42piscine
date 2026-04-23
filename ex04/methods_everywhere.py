#!/usr/bin/env python3
import sys

class modify:
    def __init__(self, name):
        self.name = name
    
    def shrink(self):
        return self.name[:8]

    def enlarge(self):
        return self.name.ljust(8, 'z')
        
if len(sys.argv) < 2:
    print("No parameters entered.")
    sys.exit()

for i in range(1, len(sys.argv)):
    str_word = sys.argv[i]

    if len(str_word) == 8:
        print(str_word)

    elif len(str_word) > 8:
        mod = modify(str_word)
        print(mod.shrink())

    else:
        mod = modify(str_word)
        print(mod.enlarge())
