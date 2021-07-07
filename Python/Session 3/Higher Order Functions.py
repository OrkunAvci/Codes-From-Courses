def shout(*args):
	return f"This is returned from a function {args[0]}.".upper()


def whisper(*args):
	return "This is returned from a function.".lower()


def greet(*args):
	greeting = args[0](args[1:])
	print(greeting)


greet(shout, "text")
greet(whisper)
