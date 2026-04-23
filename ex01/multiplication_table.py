#!/usr/bin/env python3

int_number = int(input("Enter a number: "))
print (int_number)

for number in range(0, 10, 1):
	result = number * int_number
	print(str(number) + " * " + str(int_number) + " = " + str(result))
print()
