from turtle import Turtle

class Plate(Turtle):

	def __init__(self, side):
		super().__init__()
		self.shape("square")
		self.pensize(5)
		self.shapesize(1,5,1)
		self.left(90)
		self.pencolor("white")
		self.fillcolor("white")
		self.penup()
		self.goto(side * 360, 0)

	def move_up(self):
		self.forward(5)

	def move_down(self):
		self.back(5)
