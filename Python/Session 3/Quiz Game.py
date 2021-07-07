import requests as req

res = req.get("https://opentdb.com/api.php?amount=20&category=9&type=boolean")
data = res.json()["results"]

for entry in data:
	print("Difficulty: ", entry["difficulty"])
	print(entry["question"])
	answer = input("True or False? ")
	if answer == entry["correct_answer"]:
		print("Correct!")
	else:
		print("Correct answer was", entry["correct_answer"])
	print()
