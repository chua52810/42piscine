#!/usr/bin/env python3

def add_one(x):
    x += 1
    print(f"Output from add_one(0) function, x = {x}, in this case x becomes a local variable.")
    
x = 0
print(f"Global variable, x = 0")
print(f"Call function add_one() using global variable x, i.e, add_one(x).")
add_one(x)
print(f"Exit function, back to Main.")
print(f"x = {x}, i.e, x revert to global variable 0 once it exit the function.")
print()
print(f"If a variable is defined both globally and locally with the same name, changes to the local variable inside functions do not affect the global variable, unless explicitly declare variable as global.")


