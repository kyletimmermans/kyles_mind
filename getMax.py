'''
Start max at 0 so the following numbers will definitely become the max
and max will be replaced by the biggest number in the array.
Go through the array, if a number there is a bigger number, replace it as the new max.
Continue to replace the max with the biggest number. After the final element has been 
evaluated, the biggest number (max), will have been found. The max number is almost pushed
to the end, as it has to be compared to the other numbers and will return the largest number
from all the comparisons.
'''

def getMax(arr):
	max = 0  # Start off w/ max = 0, always will have items greater or equal to 0 (guaranteed new max value)
	for i in arr:   # for each item in array
		if i > max:  # If there is a number that is greater than the max,
			max = i  # then this number will be the new max
	return max

arr = [70, 100, 40]

print(getMax(arr))
