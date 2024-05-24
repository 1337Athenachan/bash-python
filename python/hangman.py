#!/usr/bin/python3

import random

# Greeting
print("Welcome to my hangman game")

# Create a list of words to use
words = ["cyber", "security", "expert"]
print(words)

secret_word = random.choice(words)
print(secret_word)

guess = input("What letter do you want to guess?: ")
for letter in secret_word:
	print(letter)
	if letter == guess:
		print("Correct!")
	else:
		print("Wrong!")



