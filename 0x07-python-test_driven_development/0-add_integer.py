#!/usr/bin/python3
def add_integer(a, b=98):
	"""
	Adds two integers

	Args:
		a: first parameter
		b: second parameter with default value of 98

	Return:
		The return is the sum of a and b

	"""

	if type(a) is float:
		a = int(a)

	if type(b) is float:
		b = int(b)

	if type(a) is not int:
		raise TypeError("a must be an integer")

	if type(b) is not int:
		raise TypeError("b must be an integer")

	return a + b
