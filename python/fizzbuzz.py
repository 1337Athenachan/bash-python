#!/usr/bin/python3

# Loop 1-100 printing variuos outputs
for num in range(1, 100):

# If number is divisible by both print fizzbuzz		
	if num % 3 == 0 and num % 5 == 0:
		print("fizzbuzz")

# If number is divisible by 3 print fizz
	elif num % 3 == 0:
		print("fizz")

# If number is divisible by 5 print buzz
	elif num % 5 == 0:
		print("buzz")
	else:
		print(num)
	
