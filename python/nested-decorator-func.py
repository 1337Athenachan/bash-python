#!/usr/bin/python3

# nested functions
def out():
	print("Outside Function")
	
	def inner():
		print("Inner Function")
	
	inner()

out()

print("\n")

# decorator functions
def add(n1, n2):
	return n1 + n2
def sub(n1, n2):
	return n1 - n2
def multiply(n1, n2):
	return n1 * n2
def divide(n1, n2):
	return n1 / n2	
def calculate(calc, n1, n2):
	return calc(n1, n2)

result = calculate(multiply, 3,4)	

print(result)

