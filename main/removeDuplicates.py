'''
Explanation:

The newest and first elements to go into newList
cannot be dupes because they have not been seen yet.
Once the element is in newList and it is found in both newList
and oldList, it means that it has already been added, thus making it a duplicate.

* If it's in newList already, we'll be adding a copy,
  a duplicate. If it's not in newList, we haven't seen
  it and it is not a copy, it is completely new and unique.
'''

oldList = ["hello", "cool", "cool", "awesome"]
newList = []

for i in oldList:
	if i not in newList:
		newList.append(i)

print(newList)

# Output = ['hello', 'cool', 'awesome']
