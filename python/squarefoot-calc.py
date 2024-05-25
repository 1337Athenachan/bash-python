#!/usr/bin/python3

print("Welcome, this program will calculate the area square feet.")

def sqr_foot(w,h):
	area_sqft = w * h
	print(f"The Area Square Feet Is: {area_sqft}")
	
	
width = int(input("What is the width?: "))
height = int(input("What is the height?: "))	

sqr_foot(width,height)

