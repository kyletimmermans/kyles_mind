# Walrus Operator - Assign and check variable condition on the same line
import os

if cwd := (os.getcwd()) != "/var/log":
	print("Current dir is not /var/log")

# Is the same as

cwd = (os.getcwd()
if cwd != "/var/log":
	print("Current dir is not /var/log")


'''
Walrus operator combines two lines together
Think of it like moving the assignment up one line
and the condition stays on the same line
'''

# Watch out for the mistake of assgining the condition to the variable
# E.g.

if cwd := (os.getcwd() == "/var/log"):   # Will not run as it's: if (cwd) w/ cwd being 'false'
	print("Current dir is /var/log")

'''
Instead of cwd being to "os.getcwd" as a string like '/home',
it has been assigned to "os.getcwd == /var/log" as a boolean
which is false

Make sure to put parenthesis around the assignment so we get a value
instead of putting them around the condition and changing the value to
a boolean.

x = 4    vs    x = (4 == 4)
 int               bool
'''

