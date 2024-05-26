#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

# greeting
print("Welcome to my html parser!")

# url parser for webpages
def get_page(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')

# find first anchor tag
	print(soup.a)

# find all anchor tags
	print(soup.find_all("a"))

# use loop to print just the href tags that contain url links
	for link in soup.find_all('a'):
    		print(link.get('href'))

# find specific anchor tags
	try:
		var = soup.find(id="vector-main-menu-dropdown")	
		print(var.string)
	except:
		print("Error: No strings to show in this section")
# get title and text from a wepage
	try:
		print(soup.title)
		print(soup.text)
		print(soup.title.string)
	except:
		print("Error: No strings to show in this section")	
# optionally ask a user what they want parse, or add hardcode it for easy use
get_page(input("What page would you like to parse?: "))


