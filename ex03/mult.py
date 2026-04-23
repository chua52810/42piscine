#!/usr/bin/env python3

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: ")) 
result = first_num * second_num

print(str(first_num) + " * " + str(second_num) + " =" + str(result) + ".")

if result <0:
	print("The result is negetative.")
elif result>0:
	print("The result is positive.")	
else:
	print("The result is zero.")	
print()
