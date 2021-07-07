import random
import math

#	Limits
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

#	Prep
generated = random.randint(lower, upper)
expected = math.ceil(math.log(upper - lower + 1, 2))
guesses = 0
guess = lower - 1

#	Game
while generated != guess:
	guess = int(input("Guess a number:- "))
	guesses += 1
	print()
	if generated > guess:
		print(f"Go higher than {guess}.")
	elif generated < guess:
		print(f"Go lower than {guess}.")

#	Result
print(f"Expected guess count was {expected}.")
print(f"You found the number {guess} in {guesses} guesses.")
