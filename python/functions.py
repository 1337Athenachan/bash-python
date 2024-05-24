#!/usr/bin/python3

# A simple function
def function():
	print("Hello!")

function()

# Let's make one for a new line
def nl():
	print("\n")
	
nl()
function()

def final_thoughts():
	print("You’ve done it. You’ve refined your introduction and your thesis. You’ve spent time researching and proving all of your supporting arguments. You’re slowly approaching the finish line of your essay and suddenly freeze up because—that’s right—it’s time to write the conclusion.")
	
nl()
final_thoughts()
nl()

# Passing in data to the function
def add():
	a = int(input("Enter a number: "))
	b = int(input("Enter a number: "))
	c = a + b
	print(c)

add()
nl()

# Passing in data to the function
arg1 = 4
arg2 = 4
def add2(arg1, arg2):
	total = arg1 + arg2
	print(total)

print("About to start the program\n....")
nl()
add2(arg1, arg2)

# Final code challenge

uname = input("What is your name please?: ")

def greeter(uname):
	print(f"Hello {uname}, it's great to see you again! ")
	
greeter(uname)
	
