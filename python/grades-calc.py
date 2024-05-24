#!/usr/bin/python3

# Taking input and converting it to interger

score = input("What score did you get?: ")
iscore = int(score)

# Looping through options

if iscore >= 90:
	print("Congradulations you recived over 90 points, which gets you an A")	

elif iscore >= 80:
	print("Congradulations you recived 80-89 points, which gets you a B")


elif iscore >= 70:
	print("Congradulations you recived 70-79 points, which gets you a C")

else: 
	print("Sorry, you only score below 69 points, which gets you a D, but better luck next time!")


# This program can easily break, and it is only made for practice purposes.

