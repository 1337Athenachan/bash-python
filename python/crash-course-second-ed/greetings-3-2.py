#!/usr/bin/python3

# Task: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them The text of each message should be the same, but each message should be personalized with the person’s name

# Store names in a variable
names = ["Sarah", "Sally", "John"]
greeting = "Welcome to the system"
# Print
print(f"Welcome to the system {names[0]}")
print(f"Welcome to the system {names[1]}")
print(f"Welcome to the system {names[-1]}")

# Could add the welcom message to a variable as well if required
print(f"{greeting} {names[-1]}")
