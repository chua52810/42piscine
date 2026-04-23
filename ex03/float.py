#!/usr/bin/env python3

def check_number_type(str_input):
    try:
        # Convert input to a float so we can check its math
        num = float(str_input)
        
        # .is_integer() checks if the decimal part is .000...
        if num.is_integer():
            return "integer"
        else:
            return "decimal"
    except ValueError:
        return "invalid input"

user_val = input("Give me a number: ")
result = check_number_type(user_val)

print(f"This number is a {result}.")

