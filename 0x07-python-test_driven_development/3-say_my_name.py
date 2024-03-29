#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
	"""

	prints a neatly formatted name

	Args:
		first_name: users first name
		last_name: users last name

	Return:
		Zero

	"""

	if type(first_name) is not str:
		raise TypeError("first_name must be a string")

	if type(last_name) is not str:
		raise TypeError("last_name must be a string")

	if last_name:
		print("My name is {:s} {:s}".format(first_name, last_name))

	else:
		print("My name is {:s}".format(first_name))
