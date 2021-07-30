#include <iostream>

using namespace std;

int main()
{
	/*
		Normally to check if a number is even or odd, we can use the module operator.
		When we use "% 2", it will divide the number in half and return the remainder.
		All even numbers can be split in half with nothing left over, so the remainder
		will be 0, so we know it's even. All odd numbers when split in half, will always
		have one left over after being split in half, because they don't split evenly.

		E.g. 4 splits into two even groups with nothing left, while 7 splits
			 into 2 even groups and then has 1 left.

		4 =  | |  and | |

		7 =  | | |  and | | | and |

		_________________________________________________________________________________

		Now how do we check if a number is even or odd without the modulo operator?
		We can divide the number by 2 and then multiply that number by 2. If the 
		resulting number is the same as it was before it was divided, it is even.

		When an even number is divided, it has no remainder, so the number is clean
		and can then be multiplied by 2 to get the original number. However, when we
		divide an odd number in half, it should be some number and then .5 so we would
		get two numbers with a .5 which together make up the extra remainder of 1. Yet,
		when we divide an odd number by two, it will not include the .5's. Just the whole
		number. So when we multiply it by 2, it will not be the same number as the original,
		because it is missing a 1 (2 .5's).

		* Division is the true test of even or odd because it does not carry remainders,
		  which odd numbers need, the multiplication just reveals that the division
		  does not carry remainders
		  	-So if it the division multiplication works, it's even
		  	-If the division multiplication doesn't work, it's odd
	*/

	cout << endl;

	cout << "(4 / 2) * 2 = (2) * 2 = " << (4 / 2) * 2 << endl;
	cout << "(7 / 2) * 2 = (3) * 2 = " << (7 / 2) * 2 << endl;

	cout << endl;

	cout << "Even number came back after being divided by 2, but the odd number did not.\n" << endl;

	return 0;
}