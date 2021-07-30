/*
	The Spaceship operator is offered in the C++20 standard
	A.k.a the three way operator. 

	Have to use -std=c++20 with g++ command
*/

#include <iostream>
#include <compare>  // Needed for spaceship operator

using namespace std;

int main()
{
	int a = 1, b = 2;

	auto ans = a <=> b;  // Spaceship operator here

	/*
		Spaceship operator takes two parameters, a and b.
			-If a < b, the result is:    ans < 0
			-If a > b, the result is:    ans > 0
			-If a == b, the results is:  ans == 0
		
		* Pivots around 0
	*/

	if (ans < 0)
		cout << "a < b" << endl;
	else if (ans > 0)
		cout << "a > b" << endl;
	else if (ans == 0)
		cout << "a == b" << endl;

	return 0;
}
