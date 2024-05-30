#!/usr/bin/python3

import random

options = ("rock", "paper", "scissors")

player_choice = input(f"What {options} option would you like to choose?: ")

cpu_choice = random.choice(options)

if player_choice == cpu_choice:
	print(f"You got a tie, the player choose {player_choice} and the computer choose {cpu_choice}")

elif player_choice != cpu_choice:
	
	if player_choice == "rock" and cpu_choice == "scissors":
		print(f"You: {player_choice} CPU: {cpu_choice} You Win!")
	elif player_choice == "rock" and cpu_choice == "paper":
		print(f"You: {player_choice} CPU: {cpu_choice} You Lose!")
	elif player_choice == "scissors" and cpu_choice == "paper":
		print(f"You: {player_choice} CPU: {cpu_choice} You WIN!")
	elif player_choice == "scissors" and cpu_choice == "rock":
		print(f"You: {player_choice} CPU: {cpu_choice} You Lose!")
	elif player_choice == "paper" and cpu_choice == "scissors":
		print(f"You: {player_choice} CPU: {cpu_choice} You Lose!")	
	elif player_choice == "paper" and cpu_choice == "rock":
		print(f"You: {player_choice} CPU: {cpu_choice} You Win!")	
	else:
		print("incorrect syntax")
		
