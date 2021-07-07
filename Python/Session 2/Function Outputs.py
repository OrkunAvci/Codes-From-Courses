import time

#	Simple return
def simple(x):
	return "Function returns: '" + x + "'"

print(simple("Sent to function"))

#	Return multiple
def multi_return():
	str = "Something"
	integer = 6
	return str, integer

print(multi_return())

#	Return function (Function factory?)
def by_factor(factor):
	def multiply(number):
		return factor * number
	return multiply

double = by_factor(2)
triple = by_factor(3)

print(double(5))
print(triple(10))

def my_timer(func):
	def _timer(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(f"Execution time: {end - start}")
		return result
	return _timer

@my_timer
def delayed_mean(sample):
	time.sleep(1)
	return sum(sample) / len(sample)

print(delayed_mean([10, 2, 4, 7, 9, 3, 9, 8, 6, 7]))
