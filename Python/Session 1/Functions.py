def my_function(fname):
	print(fname + " and me")

my_function("Linux")

#	Arbitrary Arguments
def arb_func(*args):
	print("Fine with " + args[0])
#	print("Error on " + args[2])
arb_func("Emil", "Tobias")

#	Keyword Arguments
def kw_func(child3, child2, child1):
	print("The youngest child is " + child3)
kw_func(child1 = "Emil", child2 = "Tobias", child3 = "Linux")

#	Arbitrary Keyword Arguments
def arb_kw_func(**kwargs):
	print("His last name is " + kwargs["lname"])
arb_kw_func(fname = "Tobias", lname = "Refsnes")

def illust(**kwargs):
	print(kwargs)
	for key, value in kwargs.items():
		print("%s is %s" % (key, value))
illust(this="random", that="valid")

#	Anonymous Functions
square = lambda x: x*x
print(square(5))
