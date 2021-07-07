fruits = ["apple", "banana", "cherry"]
for x in fruits:
	if x == "banana":
		continue
	if x == "cherry":
		break
	print(x)
else:
	print("We have reached the end.")

for x in range(6):
	print(x)
else:
	print("Finally finished!")
