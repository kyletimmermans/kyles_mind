'''
One way to get a substring within a larger text
is getting the value of the position of the beginning
character and then iterating through the rest of
the substring until we get the positional value of 
the last character.

Adding the positional value of the start character and then then
the number of hops it took to get to the last character, gives
us the positional value of the final character of the substring.

Once we have the start and end position of the substring,
we have the whole substring.

E.g. If we want the substring "Kyle"


		         Journey
	                   +3
                          ---
"Hello World, my name is Kyle and I like to program!"
 -------------------------
 		   +25
 		  Start


The start character is found at position [25], we add 3 to
get to the final character's position, so the final character's
position is [28].


* start + journey = end

* And the start -> end is the substring
'''

testString = "Hello World, my name is Kyle and I like to program!"

journey = 0  # Iterator for journey hops

for i in range(len(testString)):
	if testString[i] == "K":   # Start
		start = i
		while (testString[i+journey] != ' '):  # Start + Journey != a space
			journey += 1  # Save up journey hops


# Substring is start to end (start+journey)
print(testString[start:start+journey])
