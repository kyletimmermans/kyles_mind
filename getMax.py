def getMax(arr):
	max = 0  # Start off w/ max = 0, always will have items greater or equal to 0 (guaranteed new max value)
	for i in arr:   # for each item in array
		if i > max:  # If there is a number that is greater than the max,
			max = i  # Then this number will be the new max
	return max

arr = [70, 100, 40]
print(getMax(arr))