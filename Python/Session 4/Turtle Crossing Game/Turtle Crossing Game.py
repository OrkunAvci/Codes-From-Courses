import turtle
import keyboard

from Car import Car
from Player import Player

if __name__ == "__main__":
	window = turtle.Screen()
	window.bgcolor("black")
	player = Player()
	player.goto(0, -200)
	player.left(90)
	cars = []
	for i in range(5):
		cars.append([])
		for j in range(5):
			car = Car()
			car.goto(-400 + (j * 200),-100 + (i * 50))
			if i % 2 == 0:
				car.left(180)
			cars[i].append(car)
	while player.ycor() < 200:
		for line in cars:
			for car in line:
				car.move()
		try:
			if keyboard.is_pressed("w"):
				player.move("w")
			elif keyboard.is_pressed("s"):
				player.move("s")
		except:
			pass
	turtle.done()
