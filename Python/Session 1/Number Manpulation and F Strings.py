#	ınt
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

#	Float
x = -35.59
y = 35e3
z = 12E4
k = -87.7e100
print(type(x))
print(type(y))
print(type(z))
print(type(k))

#	Complex
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

quantity = 3
itemno = 567
price = 49.95

myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

name = 'Hex'
age = 24
print(f"Hello, My name is {name} and I'm {age} years old.")
