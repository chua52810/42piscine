#!/usr/bin/env python3

original_array = [2,8,9,48,8,22,-12,2]
new_set = set()

length = len(original_array)

for i in range(length):
    if original_array[i] > 5:
    	result = original_array[i] + 2
    	new_set.add(result)

sorted_list = sorted(new_set)

print("Original array:", original_array)
print("New set:", sorted_list)
print()
