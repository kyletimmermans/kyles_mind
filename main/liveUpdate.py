'''
Let's say we want to skip all the pre-existing 
lines of a file and create a listener that only
shows the new lines that are added to a file after
we run the program
'''

with open('test.txt', 'r') as f:
	for line in f:  # Pass all the lines and go to the last line
        	pass
	while True:   # Now that we're at the last line, wait for all the new lines to come in
		line = f.readline()
		if line:
			print(line)
      
'''
E.g.

test.txt:
1  <-- Pass
2  <-- Pass
3. <-- Pass
   <-- Start Reading New Input

1. We run liveUpdate.py
2. The program opens the file and goes to the last line
3. The program is waiting for new input to be added to the end of the file
4. We edit 'test.txt' and add a '4' to the the next line
5. The program sees the new addition and prints the '4'

* Start listening after all the passes
'''
