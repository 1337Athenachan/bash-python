#!/usr/bin/python3

import turtle

# screen setup
wn = turtle.Screen()
wn.title("Ping Pong, by Scada ")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)		# sets animation speed
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)		# modify shape
pad_a.penup()		# stops it drawing lines
pad_a.goto(-350, 0)	# starting position


# paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)		# sets animation speed
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)		# modify shape
pad_b.penup()		# stops it drawing lines
pad_b.goto(350, 0)	# starting position


# ball
ball = turtle.Turtle()
ball.speed(0)		# sets animation speed
ball.shape("square")
ball.color("white")
ball.penup()		# stops it drawing lines
ball.goto(0, 0)	# starting position

# functions
def pad_a_up():
	y = pad_a.ycor()	# returns y coordinates
	y += 20
	pad_a.sety(y)
	
def pad_a_down():
	y = pad_a.ycor()	# returns y coordinates
	y += -20
	pad_a.sety(y)

# keyboard binding
wn.listen()	# listens for keyboard input
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")

# main game loop
while True:
	wn.update()
