#!/usr/bin/python3

# Declare list
fruit_list = ["apple", "orange", "pear", "peach"]
print(fruit_list)
print("\n")

# Iterate through list
for i in fruit_list:
	print(i)
print("\n")

# Iterate through list adding extra strings
for i in fruit_list:
	print(i + " pie")
print("\n")

# Add extra items
fruit_list.append("cheery")
print(fruit_list)
print("\n")

# Remove item
fruit_list.pop(1)
print(fruit_list)
print("\n")

# Itertae using range
for num in range(1,5):
	print(num)
	
# Using if statement to figure out if the numbers that are divisible by three
for num in range(1, 50):
	if num % 3 == 0:
		print(num)
