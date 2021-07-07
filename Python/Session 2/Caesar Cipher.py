import string as str

usable_characters = str.ascii_lowercase + str.ascii_uppercase + str.digits

def encryption(plain, offset):
	crypted = ""
	for c in plain:
		crypted += (usable_characters[ (usable_characters.index(c) - offset) % len(usable_characters) ])
	return crypted

def decryption(crypted, offset):
	plain = ""
	for c in crypted:
		plain += (usable_characters[(usable_characters.index(c) + offset) % len(usable_characters)])
	return plain

original = input("Enter the original string: ")
offset = int(input("Enter the offset: "))

crypted = encryption(original, offset)
print(crypted)

original = decryption(crypted, offset)
print(original)
