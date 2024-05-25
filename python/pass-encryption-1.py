#!/usr/bin/python3

import base64

# this program encrypts passwords
print("Welcome, this program will encrypt a password for you.")


def encrypt_pass(password):
	encoded_bytes = base64.b64encode(password.encode())
	print(encoded_bytes)


userpass = input("Please enter a password: ")
encrypt_pass(userpass)


