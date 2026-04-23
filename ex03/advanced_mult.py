#!/usr/bin/env python3

big_loop = 0
while big_loop <= 10:
    results = []
    small_loop = 0
    while small_loop <= 10:
        results.append(str(big_loop * small_loop))
        small_loop = small_loop + 1
    print(f"Table of {big_loop}: {' '.join(results)}")
    big_loop = big_loop + 1    	
print()



