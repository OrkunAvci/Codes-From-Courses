from turtle import Turtle

class Player(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("turtle")
		self.pensize(3)
		self.pencolor("white")
		self.fillcolor("white")
		self.penup()

	def move(self, dirc):
		if dirc == "w":
			self.forward(2.5)
		else:
			self.back(2.5)
