import turtle
import random
def spiral():
	turtle.speed(0)
	t = turtle
	t.color('blue')
	t.colormode(255)
	x = 10
	a = 91
	# Draw the base
	for j in range(150):
		t.color(0,0,100+j)
		t.width(1)
		for i in range(4):
			t.forward(x)
			t.left(a)
		x += 7
	# Move up
	#t.penup()
	#t.left(90)
	#t.forward(50)
	#t.pendown()

spiral()
holdit = input()
