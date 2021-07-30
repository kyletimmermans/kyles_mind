/*
	The DeFacto Programming Challenge

	Print integers 1 to N 
		-Print “Fizz” if an integer is divisible by 3 
		-Print "Buzz” if an integer is divisible by 5 
		-Print “FizzBuzz” if an integer is divisible by both 3 and 5
*/

#include <stdio.h>

void fizzbuzz(int num) {
	if (num % 3 == 0 && num % 5 == 0) {  // Check this condition first (both), don't want the
		printf("%i, FizzBuzz\n", num);	 // other conditions popping before this if also true
	} else if (num % 3 == 0) {
		printf("%i, Fizz\n", num);		 // Now check solo conditions on their own
	} else if (num % 5 == 0) {
		printf("%i, Buzz\n", num);
	} else {
		printf("%i\n", num);  // Print normal numbers anyway
	}
}									  

int main()
{	
	// Do fizzbuzz() on numbers 1-20
	for (int i = 1; i < 21; ++i) {  // 20 is the first whole number before 21
		fizzbuzz(i);
	}

	return 0;
}