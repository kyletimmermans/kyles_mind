'''
Nested For Loop Logic:


A nested loop is a loop within a loop, an inner loop within the body of an outer one. 
How this works is that the first pass of the outer loop triggers the inner loop, which 
executes to completion. Then the second pass of the outer loop triggers the inner loop 
again. This repeats until the outer loop finishes.
	
	-https://tldp.org/LDP/abs/html/nestedloops.html

E.g.

1st:				    2nd:
---				    ---
	
    Start (Outer to Inner)		   Finish (Inner to Outer)
\				     ^	
 \ Outer loop triggers 		      \ Once the inner-most loop finishes,
  \  inner loops, until we	       \  we move up to the outer-loops
   \   get to the inner-most loop       \  and finish the loops one by one 
    \					 \   until we get to the outer-most loop 
     V                                    \    and finish it last
'''


for i in range(2):
	print("For loop i")
	
	for j in range(2):
		print("\tFor loop j")
		
		for k in range(2):
			print("\t\tFor loop k")


'''
Output:

For loop i
	For loop j
		For loop k
		For loop k
	For loop j
		For loop k
		For loop k
For loop i
	For loop j
		For loop k
		For loop k
	For loop j
		For loop k
		For loop k
'''
