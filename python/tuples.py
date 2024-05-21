#!/bin/python3

#Create a dictionary
d = dict()

#Add items
d['Bill'] = 35
d['Alice'] = 29
d['Lisa'] = 33

#For loop to display items
for (key,value) in d.items():
	print(key,value)

#New line to make it esier to read in the terminal
print('\n')

#Creating a list of tuples
tups = d.items()
print(tups)
print('\n')

#Tuples can be compared

(2, 4, 6) < (3, 5, 7)

#This would compare the first two numbers

#Using sorted
d = {'a':10, 'b':21, 'c':33}
t = sorted(d.items())
print(t)
print('\n')

#Another for loop for iteration
for k, v in t:
	print(t)
print('\n')

#Using the sorted list instead
for k, v in sorted(d.items()):
	print(k, v)

