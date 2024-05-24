#!/bin/python3

# List - brackets
# Tuple - square braces
# Set - the set keyword
# Dictionary - curly braces

# List
list1 = ["Bill", "Alice", "Jane", 25, 80.8]
print(list1)
print("\n")
list1[0] = "Sandy"
print(list1)
print("\n")

# Dictionary
dict1 = {
	1: "Bill",
	2: "Alice",
	3: "Jane",
}
print(dict1)
print("\n")
dict1[0] = "Sandy"	#Appends to the end
print(dict1)
print("\n")

# Tuple
tup1 = ("Bill", "Alice", "Jane", 25, 80.8)
print(tup1)
print("\n")
#tup1[0] = "Sandy"	# Doesn't work with Tuple
#print(tup1)
#print("\n")

# Set
set1 = set(["Bill", "Alice", "Jane", 25, 80.8])
print(set1)
print("\n")
#set1[0] = "Sandy"	# Doesn't work with Set
#print(set1)
#print("\n")
