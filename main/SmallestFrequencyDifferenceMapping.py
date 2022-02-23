#!/bin/usr/env python3

# Map letters with closest frequency numbers

frequency_list_one = {'a': 1.000, 'b': 2.000, 'c': 3.000}

frequency_list_two = {'x': 1.001, 'y': 2.002, 'z': 3.003}

translation = {}

def mapping(list_one, list_two):
	# For all elements of one list, check each element against
	# the other list, to find its counterpart

	# Least difference, means they are the closest together (more likely to be the same char)
	for key, value in list_one.items():
		difference = 999  # Start largest difference possible
		for key_two, value_two in list_two.items():
			if (abs(value - value_two)) < difference:  # If we get a smaller difference, this number is then a closer number
				difference = abs(value - value_two)  # abs() because difference could be negative, just want how far apart, no signs
				saved_key = key_two  # Keep track of the closest key
		translation[key] = saved_key
	return translation

print( mapping(frequency_list_one, frequency_list_two) )

# Output: {'a': 'x', 'b': 'y', 'c': 'z'}