# initializing list
questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']

# using zip() to combine two containers and print values
for question, answer in zip(questions, answers):
	print('What is your {0}?  I am {1}.'.format(question, answer))

dic = {"Key1": "Value1", "Key2": "Value2"}

# using items to print the dictionary key-value pair
print("The key value pair using items is : ")
for i, j in dic.items():
	print(i ,j)

kings = {'Akar': 'The Great', 'Chandragupta': 'The Maurya',
		'Modi': 'The Changer'}

# using items to print the dictionary key-value pair
for key, value in kings.items():
	print(key, value)

# initializing list
lis = [1, 3, 5, 6, 2, 1, 3]

# using sorted() to print the list in sorted order
print("The list in sorted order is : ")
for i in sorted(lis):
	print(i, end=" ")

# using sorted() and set() to print the list in sorted order use of set() removes duplicates.
print("The list in sorted order (without duplicates) is : ")
for i in sorted(set(lis)):
	print(i, end=" ")

# using revered() to print the list in reversed order
print("The list in reversed order is : ")
for i in reversed(lis):
	print(i, end=" ")

colors = ['red','green','blue']
for color in enumerate(colors):
	print (color)
