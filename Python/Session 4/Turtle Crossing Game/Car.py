from turtle import Turtle

class Car(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("square")
		self.pensize(3)
		self.pencolor("white")
		self.fillcolor("white")
		self.penup()
		self.speed("fastest")

	def move(self):
		self.forward(2.5)
		if (abs(self.xcor()) > 500):
			self.revert()

	def revert(self):
		self.hideturtle()
		self.back(1000)
		self.showturtle()
