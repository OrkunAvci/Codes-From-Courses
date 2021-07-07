import random as rand

options = ["rock", "scissors", "paper"]

user_option = input("Roll for it. ")
user_option = user_option.lower()

comp_option = options[ rand.randint(-1,2) ]
print(f"Computer has chosen {comp_option}.")

if user_option == comp_option:
	print("It is a draw!")
elif options[ options.index(user_option) - 1 ] == comp_option:
	print("Computer wins!")
else:
	print("You win!")
