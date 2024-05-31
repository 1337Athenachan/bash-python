#!/usr/bin/python3

# Task: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations You’ll have to think of someone else to invite

# Variable to store our list
people = ["stalin", "hitler", "churchill"]
print(people)

# Greeting for later use with our var
greeting = "please could you attend our party."

# Concat our two variables using specific points in the list
print(f"Greetings {people[0]}, {greeting} ")
print(f"Greetings {people[1]}, {greeting} ")
print(f"Greetings {people[2]}, {greeting}\n ")

# Guest can't make it
print(f"Unfortunatly {people[0]} can't make it, you will have to invite someone else!\n")

# Updating our list
people[0] = "roosevelt"

# Adding update message
print("List updated")
print("\n")

# Reprint our invitations back onto the screen with updated list
print(f"Greetings {people[0]}, {greeting} ")
print(f"Greetings {people[1]}, {greeting} ")
print(f"Greetings {people[2]}, {greeting} ")
