import random as rand

class deck:
	cards = [{}]

	def __init__(self):
		for type in ["clubs", "diamonds", "hearts", "spades"]:
			for value in range(2,11):
				self.cards.append({
					"type" : type,
					"name" : str(value),
					"value" : value
				})
			self.cards.append({"type": type, "name": "Ace", "value": 11})
			self.cards.append({"type": type, "name": "King", "value": 10})
			self.cards.append({"type": type, "name": "Queen", "value": 10})
			self.cards.append({"type": type, "name": "Jack", "value": 10})

	def draw(self):
		drawn = self.cards.pop(rand.randrange(0, len(self.cards)))
		print(f"{drawn['name']} of {drawn['type']} has been drawn!")
		return drawn

	def reset(self):
		self.__init__()
