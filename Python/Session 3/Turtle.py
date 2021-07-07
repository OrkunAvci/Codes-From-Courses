import math
import turtle

window = turtle.Screen()
window.title("First Turtle Program")
tur = turtle.Turtle()

tur.begin_fill()
tur.circle(60)
tur.end_fill()

turtle.bgcolor("blue")
turtle.pencolor("purple")
tur.pensize(2)

tur.speed(1)
tur.fillcolor("red")
tur.begin_fill()
tur.forward(128)
tur.right(90)
tur.forward(128)
tur.right(135)
tur.forward(math.sqrt(2) * 128)
tur.end_fill()

tur.speed(10)
tur.fillcolor("purple")
tur.begin_fill()
tur.left(45)
tur.forward(128)
tur.left(90)
tur.forward(128)
tur.home()
tur.end_fill()

tur.right(90)
tur.stamp()
tur.forward(128)
tur.stamp()
tur.right(90)

for i in range(0, 5):
	tur.circle(i * 20)

turtle.done()
