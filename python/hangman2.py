#!/usr/bin/python3

import random

# Create greeting
print("welcome to my hangman game!")

# Create word list
words = ["cyber", "security", "tester"]

# Randomly choose word
secret_choice = random.choice(words)


# Testing purposes
#print(secret_choice)

# Creating a list to store our symbols
display_word = []

for letter in secret_choice:
	display_word += "_"
print(display_word)	
	
# Game end condition		
game_over = False

# Add while loop to finish the game 
while not game_over:

# Player input
	guess = input("Please Enter your guess: ")	

# For loop to iterate range len on position of secret choice
	for position in range(len(secret_choice)):
#		print(position)
		letter = secret_choice[position]
#		print(letter)
		if letter == guess:
			display_word[position] = letter
	print(display_word)
	
# print display and end game			
	if "_" not in display_word:
		print("You Win!")
		game_over = True


