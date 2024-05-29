#!/usr/bin/python3

import time

def countdown(t):
	
		while t:
	
			mins, sec = divmod(t, 60)
			timer = "{:02d}:{:02d}".format(mins, sec)
			print(timer, end="r")
			time.sleep(1)
			t -= 1
	
			print(" Timer Completed!")
		
# added to catch any errors with input		
try:
	t = int(input("What time would you like to enter?: "))
except:
	print("Please enter a valid integer number.")
	quit()
	
countdown(t)
