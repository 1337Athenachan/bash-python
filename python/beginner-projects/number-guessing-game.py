#!/usr/bin/python3

import random


def num_guess():
	num = random.randint(1,10)
	guess = 0
	num_trys = 5
	
	while guess != num and num_trys != 0:
		guess = int(input("What number do you want to choose"))
		
		if num_trys == 1:
			print("Sorry you ran out of guesses")
			exit()
		elif guess < num:
			num_trys -= 1
			print(f"Sorry too low, this is your {num_trys} attempt")
		elif guess > num:
			num_trys -= 1
			print(f"Sorry too high, this is your {num_trys} attempt")
		else:		
			print("correct!")	
		

num_guess()
