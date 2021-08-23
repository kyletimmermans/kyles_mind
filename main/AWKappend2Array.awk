#!/bin/awk -f

BEGIN{
  b[0]  # Init name array
  arraylen = 0  # Array size starts at 0
  while(( getline line<"grade_info.txt") > 0 ) {
     split(line,a," ")  # Split up line by spaces and store each member in array 'a'
     b[arraylen++] = a[1]  # Store the name from a into b in the next point of the array 'arraylen'
  }

  # Print out all values
  for (i in b) 
	  print b[i]
}
