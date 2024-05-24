#!/usr/bin/python3

import random

# Cretae greeting
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

# Adding our game into a while loop to keep it running until the user has finished the game
game_over =False

while not game_over:
# Player input
    guess = input("Guess a letter?: " ).lower()
# For loop to iterate the letters
# It will print correct for every choice you get right
    for position in range(len(secret_choice)):
        letter = secret_choice[position]
        if letter == guess:
            display_word[position] = letter
            
    print(display_word)
    if "_" not in display_word:
        print("You win!")
        game_over = True  


