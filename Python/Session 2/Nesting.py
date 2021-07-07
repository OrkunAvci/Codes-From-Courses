nest = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']

print(nest[0])
print(nest[1])
print(nest[1][1])
print(nest[1][1][1])
print('ddd' in nest)
print('ddd' in nest[1])
print('ddd' in nest[1][1])

#	Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linux",
    "year" : 2011
  }
}

for reference, values in myfamily.items():
	print()
	print(reference)
	print("{")
	for key, value in values.items():
		print("	", key, ":", value)
	print("}")
