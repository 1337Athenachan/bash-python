#!/usr/bin/python3

# Task: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations You’ll have to think of someone else to invite

# Variable to store our list
people = ["Stalin", "Hitler", "Churchill"]
people = people
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
people[0] = "Roosevelt"

# Adding update message
print("List updated")
print("\n")

# Reprint our invitations back onto the screen with updated list
print(f"Greetings {people[0]}, {greeting} ")
print(f"Greetings {people[1]}, {greeting} ")
print(f"Greetings {people[2]}, {greeting}\n ")

# Bigger table, print message updating user info
print("Sir! Wwe have found a bigger table and require three more guests\n")
print("List updated!\n")

# Add extra people to the list 
people.append("Franco")
people.append("Truman")
people.append("Mussolini")

# Print out statement
print(f"Greetings {people[0]}, {greeting} ")
print(f"Greetings {people[1]}, {greeting} ")
print(f"Greetings {people[2]}, {greeting} ")
print(f"Greetings {people[3]}, {greeting} ")
print(f"Greetings {people[4]}, {greeting} ")
print(f"Greetings {people[5]}, {greeting} ")

# Table has broken and only two guests can fit for the party
print("Sir! the table has broken and only two guests can fit for the party\n")

# Removing guests with pop
print(f"Sorry {people[0]} there isn't eneough room at the party")
people.pop(0)
print(f"Sorry {people[0]} there isn't eneough room at the party")
people.pop(0)
print(f"Sorry {people[0]} there isn't eneough room at the party")
people.pop(0)
print(f"Sorry {people[0]} there isn't eneough room at the party")
people.pop(0)
print(f"Sorry {people[0]} there isn't eneough room at the party")

# Letting the two guest know they are both still invited
print(f"Thakns for staying {people[0]} and {people[1]}, you're still invited to the party!")

# Removing last two names with del and finishing the task
del people[1]
print(people)
del people[0]
print(people)
