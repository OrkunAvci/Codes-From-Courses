import csv

with open("data.csv", "r") as file:
	data = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
	for row in data:
		print(row)
	print()

#	Or we can register our own dialect:
with open("data.csv", "r") as file:
	csv.register_dialect('my_dialect', delimiter=',', skipinitialspace=True, quoting=csv.QUOTE_ALL)
	data = csv.reader(file, dialect="my_dialect")
	for row in data:
		print(row)
	print()

#	csv.DictReader
with open("data.csv", "r") as file:
	data = csv.DictReader(file)
	for row in data:
		print(row)
	print()

#	Sniffer
with open('data.csv', 'r') as file:
	sample = file.read(64)	#	Argument is the number of bytes to return.
	print(csv.Sniffer().has_header(sample))
	deduced_dialect = csv.Sniffer().sniff(sample)

with open('data.csv', 'r') as file:
	reader = csv.reader(file, deduced_dialect)
	for row in reader:
		print(row)
