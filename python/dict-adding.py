#!/usr/bin/python3

# Greeting
print("Hello, and welcome to my program!")
print("\n")
# Create dictionary
student_grades = {}

# While loop to start our program
off = False
while not off:

# Get user input
	name = input("What is the students name please: ")
	grade =	input("What grade did they recieve: ")
	student_grades[name] = grade
	print(f"Entry added complete!")
	print(student_grades)	
	print("\n")
	
# Add another entry
	add_another = input("Would you like to add an additional entry? y/n: ").lower()
	if add_another == "y":
		pass
	else:
		off = True	

# Goodbye!
print("Thanks for using this program, goodbye for now!")
