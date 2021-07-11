from turtle import Turtle

class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.pensize(3)
		self.pencolor("red")
		self.fillcolor("red")
		self.penup()

	def move(self):
		self.forward(2.5)

	def collide(self):
		self.left(180)
