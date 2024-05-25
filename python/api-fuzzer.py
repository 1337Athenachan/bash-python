#!/usr/bin/python3

import requests
import sys

# to run this program you first need to cat a wordlist and then pipe it to the python3 script, dirb, small text is good
print("Syntax: cat '/wordlist' | python3 api-fuzzer.py")

def loop():
	for word in sys.stdin:
		res = requests.get(url=f"https://<Target_IP>/{word}/")		# change this
		if res.status_code == 404:
			loop()
		else:
			data = res.json()
			print(data)
			print(res.status_code)
			print(word)
#		data = res.json()
#		print(data)


