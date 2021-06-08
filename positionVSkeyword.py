# Positional Arguments vs. Keyword Arguments

def example(num1, num2):
	print("num1 = " + str(num1) + " " + "num2 = " + str(num2))

# Positional Example
example(1, 2)

# Keyword Example
example(num2=2, num1=1)

'''
Both of these function calls have the same output

Positional arguments fit in to each parameter both depending on where they lay

e.g.

def example(num1, num2)
	          \    /	
       example(1, 2)


Keyword arguments can lay anywhere because they are mapped to their parameter by name,
thus, they can be placed anywhere, and still be drawn out to where they are supposed to go
from the argument --> to the parameter keyword --> to the original parameter
e.g.		
			   ____________	
			  |			   |	
def example(num1, num2)    |
			       / 	   |	
			      /       _|
			     /       /
		        /       /
		       /       /
		      /	   	  /
		     /       /
example(num2=2, num1=1)
'''