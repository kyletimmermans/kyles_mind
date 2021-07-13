'''
An array is considered "beautiful" if all the numbers in the array,
can either be divided by the index they are in and yield a whole number
or he index they are in can be divided by the value that they hold

a[i] / i   or    i / a[i]

e.g. [1, 2, 3, 4, 5] or [2, 1, 3, 4, 5] are working examples that pass this
'''

import itertools  # Get all permutations of given array

# beautiful arrangement if all elements can:
# i/a[i] or a[i]/i into a whole number
def arrangements(n):
    # Create list based on int n
    myList = []     # e.g. 5 -> [1, 2, 3, 4, 5]
    for i in range(n):
        myList.append(i+1)  # No 0, start at 1
    
    # Get permutations list and check if each works
    answerCounter = 0   # If we get a hit, +1 for answerCounter
    perms = []  # Store permutations in list
    for x in itertools.permutations(myList):
        perms.append(list(x))   # tuple -> list
    
    # For each array in permutations, check if each of the numbers in a single array are beautiful
    for i in perms:
        for idx, val in enumerate(i):  # j = index, y = value
            idx = idx + 1  #+1, we start @ 1
            if (((idx/val).is_integer() or (val/idx).is_integer()) and idx == n):
                answerCounter = answerCounter + 1    # If everything is good up until last number, including last, +1
            elif ((idx/val).is_integer() or (val/idx).is_integer()):  # Make this one second, otherwise always passes the other if-statements
                continue  # If we're before the end number and its good, keep going
            else:
                break  # Even if one of the numbers is not working, go to next
               
    return answerCounter


print(arrangements(2))