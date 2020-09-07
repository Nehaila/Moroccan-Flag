import turtle
import math

flag = turtle.Turtle()

flag.speed(10)

flag.penup()
flag.goto((-500,150))
flag.pendown()
for i in range(4):

	flag.begin_fill()

	flag.color("red")
	flag.forward(250)

	flag.left(90)
	flag.forward(150)
	flag.left(90)
	flag.forward(250)
	flag.left(90)
	flag.forward(150)
	flag.left(90)
	flag.forward(150)
	flag.left(90)
	flag.end_fill()

	flag.forward(125)
	flag.left(135)
	flag.forward(140)
	flag.left(135)
	flag.forward(108)

	flag.color("green")
	flag.width(10)
	flag.left(108)
	for j in range(4):
		flag.forward(100)
		flag.left(144)

	flag.forward(100)
	flag.setheading(0)
	flag.penup()
	flag.setheading(270)
	flag.forward(25)
	flag.setheading(0)
	flag.forward(110)
	flag.setheading(0)
	flag.pendown()








turtle.done()
