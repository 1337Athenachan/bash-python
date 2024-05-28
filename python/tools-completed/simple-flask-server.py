#!/usr/bin/python3

from flask import Flask

# in flask you have to manually set the app variable. 
app = Flask(__name__)

# set app variable, and route to main folder
@app.route("/")

# what the server will do, currently it returns a string
def hello_world():
	return "hello world"

# call function	
if __name__ == "__main__":
	app.run()
