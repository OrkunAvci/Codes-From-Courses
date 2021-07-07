count = 0
while count < 3:
	count = count + 1	#	There is no ++ operator.
	print("Hello Mortal")

a = [1, 2, 3, 4]
while a:
	print(a.pop())

count = 0
while count < 5: count += 1; print("This is a one liner!")

i = 0
while i < 4:
	i += 1
	print(i)
	break
else:	# Not executed as there is a break
	print("No Break")
