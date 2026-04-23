#!/usr/bin/env python3

text = input("Enter a string: ")
str_converted = ""

for char in text:
    if char.isupper():
        str_converted += char.lower()
    elif char.islower():
        str_converted += char.upper()
    else:
        # Keeps numbers/symbols as they are
        str_converted += char

print(str_converted)
