#!/usr/bin/python3

import sys
import requests

# cat file then pipe it to the python program 'cat url.txt | python3 url-alive-test.py'

def urls(outfile):
	read_url = sys.stdin.read().splitlines()
	
	good_urls = []
	bad_urls = []
	
	for url in read_url:
		try:
			response = requests.head(url)
		
			if response.status_code == 200:
				good_urls.append(url)
			
		except requests.exceptions.MissingSchema:
			bad_urls.append(url)
			continue
			
	with open(outfile, "w") as file:
		file.write("\n".join(good_urls))
		
	print(f"Saved URLS To File: {outfile}")	
				

outfile = "filtered-urls.txt"

urls(outfile)			
			
