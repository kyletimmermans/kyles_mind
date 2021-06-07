'''
Explanation:

The newest and first elements to go into newList
cannot be dupes because they are have not been seen yet.
Once the element is in newList and it is found in both newList
and oldList, it has already been added, thus making it a dupe.
'''

oldList = ["hello", "cool", "cool", "awesome"]
newList = []

for i in oldList:
	if i not in newList:
		newList.append(i)

print(newList)

# Output = ['hello', 'cool', 'awesome']