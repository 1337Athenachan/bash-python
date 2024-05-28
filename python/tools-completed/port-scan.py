#!/usr/bin/python3

import socket
from _datetime import datetime

# greeting with current date and time
print("Time Started: ", datetime.now())
print("-" * 75 )
print("Hello, and welcome to my port scanner.")
print("-" * 75 )

# decalre target with user input
target = input("What IP would you like to scan?: ")

# store code in a function
def port_scan(target):
	try:
		ip = socket.gethostbyname(target)
		
		
		print(f"scanning the target {ip}")
		print("Time Started: ", datetime.now())
		
# iterate through port range to determine which ones are open		
		for port in range(20,90):
			sock = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
			sock.settimeout(1)
			result = sock.connect_ex((ip, port_scan))
			if result == 0:
				print("Port {}: Open".format(port))
			sock.close	
		
	except socket.gaierror:
		print("Hostname could not be resolved")
			
	except socket.error:
		print("Could not connect to the server")
			
		
port_scan(target)
