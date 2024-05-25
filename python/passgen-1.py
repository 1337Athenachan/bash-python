#!/usr/bin/python3

# Import modules
import string
import random

# Greeting
print("Welcome to my password generator!")
# Take user input to determine length
length = int(input("Enter a number for the password length please: "))

# Generating our character list
chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

# Add empty variable to store our pass
password = ""

# Generate password
for i in range(length):
	password += random.choice(chars)
	
print(f"You're password is: {password}")

# Ask user if they would like to save the pass to a file
save = input("Would you like to save the password?: ")
if save == "yes":
	fp = open('temp-pass.txt', 'w')
	fp.write(password)
	fp.close()
	print("You're password has been save to the file temp-pass.txt, thank you for using my program")
else:
	print("Thanks you for using my program, don't forget to save your password!")
	


