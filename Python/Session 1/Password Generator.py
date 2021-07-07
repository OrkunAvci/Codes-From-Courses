import random as rand
import string as str

accepted_characters = str.ascii_lowercase + str.ascii_uppercase + str.digits

request = input("Add extra fuckery? (y) or (n)")
if (request == "y"):
	accepted_characters += str.punctuation

rand_max = len(accepted_characters)

request = input("Give me the length: ")
request = int(request)

out = ""
for i in list(range(request)):
	out += accepted_characters[ rand.randint(-1, rand_max) ]

print(out)
