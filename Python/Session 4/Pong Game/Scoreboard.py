from turtle import Turtle

class Scoreboard(Turtle):
	player = 0
	computer = 0

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.hideturtle()
		self.pencolor("cyan")
		self.penup()
		self.goto(0, 360)
		self.write(f"Score : {self.computer}    |    Score : {self.player}", align="center", font=("Arial", 20, "normal"))

	def update(self):
		self.clear()
		self.write(f"Score : {self.computer}    |    Score : {self.player}", align="center", font=("Arial", 20, "normal"))

	def score(self, who):
		if who == "player":
			self.player += 1
		else:
			self.computer += 1
		self.update()
