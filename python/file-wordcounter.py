#!/bin/python3

#Open file
fhand = open('test.txt')

#Prepare a dictionary
counts = dict()
for line in fhand:
	words = line.split()	#Splits up the words
	for word in words:
		counts[word] = counts.get(word, 0) + 1

ist = list()
for key, val in counts.items():
	newtup = (val, key)
	ist.append(newtup)

ist = sorted(ist, reverse=True)

for val, key in ist[:10]:
	print(key, val)
	
#Shorter version
print('\n')
	
c = {'a':11, 'b':15, 'c':5}
print(sorted([(val, key) for key, val in c.items()]))

