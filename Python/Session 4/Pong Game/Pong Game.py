import turtle
import keyboard

from Ball import Ball
from Scoreboard import Scoreboard
from Plate import Plate

if __name__ == "__main__":
	window = turtle.Screen()
	window.title("Pong Game")
	window.bgcolor("black")
	scoreboard = Scoreboard()
	player = Plate(1)
	computer = Plate(-1)	#	No AI for you.
	ball = Ball()

	while True:
		ball.move()
		try:
			if keyboard.is_pressed("w"):
				player.move("w")
			elif keyboard.is_pressed("s"):
				player.move("s")
		except:
			pass
		if abs(ball.xcor() - player.xcor()) < 5 or abs(ball.xcor() - computer.xcor()) < 5:
			ball.collide()

	turtle.done()
