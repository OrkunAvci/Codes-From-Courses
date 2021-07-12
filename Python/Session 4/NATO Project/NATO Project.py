import string
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

dictionary_form = {}
for entry in data.values:
	dictionary_form[ entry[0] ] = entry[1]

plain = input("Give me a string: ")

codes = [dictionary_form[ ch.upper() ] for ch in plain if ch.upper() in string.ascii_uppercase]
coded = " ".join(codes)
print(coded)
