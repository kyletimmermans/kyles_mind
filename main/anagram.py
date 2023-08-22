s1 = "helloworld"
s2 = "worldhello"

''' 
Get the frequency of letters in both strings and store them
If the letter is not in the frequency table already,
add it. Otherwise, find and increase that letter's counter value 
in the frequency table
'''

def anagram(strone, strtwo):
	freqone = []
	for i in strone:
		if i not in freqone:
			freqone.append([i, 1])
		else:
			for j in freqone:
				if j[0] == i:
					j[1] = j[1] + 1

	freqtwo = []
	for i in strtwo:
		if i not in freqtwo:
			freqtwo.append([i, 1])
		else:
			for j in freqtwo:
				if j[0] == i:
					j[1] = j[1] + 1

	# Letters come in at different times
	# This lines them up the same to be compared
	if sorted(freqone) == sorted(freqtwo):
		return True
	else:
		return False

# Driver
if anagram(s1, s2) == True:
	print("Anagram!")
else:
	print("Not an Anagram!")
