'''
Bogosort - Generate random numbers until it's sorted

Worst case: Infinity
'''

import random

myList = [1, 9, 8, 7, 6, 4, 5, 3, 2, 0, 10]

sortedList = sorted(myList)

'''
-While the list is not equal to it's sorted state
 then it's unsorted

-If it's not equal to it's sorted self, it's not sorted

-Is this all the same elements, but sorted?

*Take what it's supposed to be, if it's not
 what it's supposed to be, keep going
'''
while (sortedList != myList):
	myList = [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
			  random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
			  random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
			  random.randint(0, 10)]
	print(myList)

# On success
print(myList)
