#!/bin/python3

#Sorting tuples by value this time
c = {'a': 10, 'b': 1, 'c':25}
tmp = list()
for k, v in c.items():
	tmp.append((v, k))	#Swaps them around
		
print(tmp)

#Sorting and then reversing the order
tmp = sorted(tmp, reverse=True)
print(tmp)

