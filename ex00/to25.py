#!/usr/bin/env python3

int_number = int(input("Enter number less than 25: "))

if int_number > 25:
    print("Error")
else:
    print(int_number)
    number = int_number - 1
    while number > 0:
        print("Inside the loop, my variable is " + str(number))
        number = number - 1
print()

