#!/usr/bin/env python3

original_array = [2,8,9,48,8,22,-12,2]
new_array = []

length = len(original_array)

for i in range(length):
    result = original_array[i] + 2
    new_array.append(result)

print("Original array:", original_array)
print("New array:", new_array)
print()
