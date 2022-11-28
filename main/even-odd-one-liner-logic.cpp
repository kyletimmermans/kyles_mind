#include <iostream>
using namespace std;

/*
	
	!(n%2) is a quick hack to find out whether or not a number is even or odd.
	This conditional first works by taking the modulo of two numbers, which returns
	the remainder after the two numbers are divided. In this case 'n' will always be
	divided by 2. If the resulting remainder is 0, we know the number was even because
	the number 'n' could be split into two even groups with nothing left over. If the 
	modulo returns 1, we know the number was odd because it was split into two uneven groups,
	one group has 1 more than the other.

	After we get either 0 or 1, we then have to deal with the NOT operator '!' which gives the
	logical opposite of whatever the result of the modulo was. If it was 0, which indicates even,
	the NOT operator will return the opposite, which is 1 or 'True', and the even condition will be
	placed in the first block of if the if statement, where true statements go. If the modulo result 
	was 1, which indicates odd, the NOT operator will again return the opposite, which is 0 or 'False',
	and the condition will be put in the second block of the if statement, where the false statements go.

	The "hack" here is that we want the 0 (even) to be placed into the true block and the 1 (odd) to be placed into
	the false block, however, 0 returns false and goes into the second block and 1 returns true and goes into the
	first block, so the NOT operator will turn our 0 (even) into a 1 and place this condition into the first block
	and the NOT operator will turn our 1 (odd) into a 0 and go into the second block.

*/

int main()
{
	int n = 7;

	if ( !(n % 2) ) {			// Even (False) (0) --> Even (True)  (1)
		cout << "even" << endl;		// Odd  (True)  (1) --> Odd  (False) (0)
	} else {
		cout << "odd" << endl;
	}

	return 0;
}
