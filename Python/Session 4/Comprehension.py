#	Dict:
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double of each value in the dictionary
double_values = {k: v*2 for (k, v) in dict1.items()}
print(double_values)

double_keys = {k*2:v for (k, v) in dict1.items()}
print(double_keys)

numbers = range(10)
squares = {n: n**2 for n in numbers if n % 2 == 0}	#	Turns into a dict.
print(squares)


fahrenheit = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}
celsius = list(map(lambda x: (float(5) / 9) * (x - 32), fahrenheit.values()))
celsius_dict = dict(zip(fahrenheit.keys(), celsius))
print(celsius_dict)

#	Or:
celsius = {k: (float(5) / 9) * (v - 32) for (k, v) in fahrenheit.items()}
print(celsius_dict)

#	Multiple Conditions:
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
dict1_triple_cond = {k: v for (k, v) in dict1.items() if v > 2 if v % 2 == 0 if k != "d"}
print(dict1_triple_cond)

even_odd = {k: ('even' if v % 2 == 0 else 'odd') for (k, v) in dict1.items()}
print(even_odd)

#	List:
list1 = [i * i for i in range(1, 11)]
print(list1)
#	Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#	Using filter function
evennumbers = filter(lambda x: x % 2 == 0, range(1, 11))
#	filter() returns an iterator.
print(list(evennumbers))
#	Output: [2, 4, 6, 8, 10]

list1 = map(lambda x: x * x, range(1, 11))
#Returns an iterator(map object)
print(list(list1))
#	Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list_nested = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
list_plain = [num_inner for list_inner in list_nested for num_inner in list_inner]
print(list_plain)
#	Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

divisible_by_six = [num for num in range(13) if num % 2 == 0 if num % 3 == 0]
print(divisible_by_six)
#	Output: [0, 6, 12]

l1 = [[num for num in range(10) if num % 2 == 0] for inner_list_index in range(3)]
print(l1)
#	Output:[[0, 2, 4, 6, 8], [0, 2, 4, 6, 8], [0, 2, 4, 6, 8]]
