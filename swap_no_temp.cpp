/*
		Algorithm:
		
		1. Place both variables into the first variable with addition
		2. Take the second variable and have it equal the doubled-up first variable
		   minus itseld, giving the second variable the original first
		   variable value
		3. Subtract the new second variable from the doubled-up first value,
		   which yields the original second variable value into the first variable

 		Summary:

 		Add up both variables. Remove what you need to place the opposite values into
 		the opposite variables. But keep in mind when you want to do the final subtraction,
		we have already done one swap.
*/

#include <iostream>

using namespace std;

int main() {

	int a = 7;
	int b = 4;

	cout << "Before: " << "a=" << a << ", " << "b=" << b << endl;

	a = a + b; // 7 + 4 = 11 
	b = a - b; // 11 - 4 = 7   
	a = a - b; // 11 - 7 = 4   

	cout << "After: " << "a=" << a << ", " << "b=" << b << endl;
	
	return 0;
}
