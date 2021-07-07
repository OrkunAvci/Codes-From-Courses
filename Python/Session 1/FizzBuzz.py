for i in range(1, 100):
	x = ""
	if i % 3 == 0:
		x += "Fizz"
	if i % 5 == 0:
		x += "Buzz"
	if i % 3 != 0 and i % 5 != 0:
		x += str(i)
	print(x)
