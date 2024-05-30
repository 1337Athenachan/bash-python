#!/usr/bin/python3

# Task: Store a person’s name, and include some whitespace characters at the beginning and end of the name Make sure you use each character combination, "\t" and "\n", at least once Print the name once, so the whitespace around the name is displayed Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip()

name = "\t\t\n\t\tEric\t\t"
print(name)

# Adding space to see what effect it has more clearly
print("\n")
print("-" * 75)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
 
