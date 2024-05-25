#!/usr/bin/python3

import base64

# this program decrypts passwords
print("Welcome, this program will decrypt a password for you.")


def decrypt_pass(password):
	decoded_bytes = base64.b64encode(password.encode())
	decoded_data = decoded_bytes.decode()
	print(f"The decrypted data is: {decoded_bytes}")


userpass = input("Please enter a password to decrypt: ")
decrypt_pass(userpass)
