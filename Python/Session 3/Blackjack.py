from Blackjack_Deck import deck

def play_blackjack():
	active_deck = deck()
	computer = active_deck.draw()["value"]
	player = active_deck.draw()["value"]
	print("Computer is at", computer)
	print("You are at", player)
	res = True
	while res and player <= 21:
		res = True if input("Draw another card?(y or n)") == "y" else False
		if res:
			player += active_deck.draw()["value"]
			print("You are at", player)
	if player > 21:
		print("You lost!")
		return
	while player > computer <= 21:
		computer += active_deck.draw()["value"]
		print("Computer is at", computer)
	if computer > 21:
		print("Computer went overboard! You won!")
		return
	else:
		print("You lost!")

if __name__ == "__main__":
	res = True
	while res:
		play_blackjack()
		res = True if input("Play again?(y or n)") == "y" else False
		print()
		print()
		print()
