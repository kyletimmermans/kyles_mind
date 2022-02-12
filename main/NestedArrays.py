'''
An index of an array is a value
e.g. The first choice (index 0) is 3 

In nested arrays, an index becomes a value and that value becomes and index which
in turn gets us another value.

The inner array will act as the index for the next outer array.

Index --> Value --> Index --> Value

We evaluate from right to left by simplifying the inner-most array
to the outer-most array.
'''

choices = [3, 2]
#Index:    0  1

items = ['$', '&', '!', '@']
#Index:   0    1    2    3

print(items[choices[0]])
# 0 --> 3 --> 3 --> @
print(items[choices[1]])
# 1 --> 2 --> 2 --> !

'''
Output:
@
!
'''
