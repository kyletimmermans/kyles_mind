/*
	Exclamation points before a boolean will give the inverse
	of it's original value

	true --> false
	false --> true

	If statements will only run with a true statement

	Therefore, a "true" value will run or a "!false" which
	actually translates to "not false", i.e. true 

	!var is a good way of checking if something is false, if the 
	variable is false, it will run because "!" makes it true in the
	if-statement
	
	bool x = false

	"!x"  ==  "x == false" : Both of these statements are true
	
	We use !var when we want false things to run as true
	
	---------------------------------------------------------------
	
	"Not", implies false in the English language e.g. "Not something"
	which makes !var good to use because we read it in English as "Not something"
	making it "false" in a language / semantics kind of way. But at the same time,
	the code also puts false's in the true section (first block of if-statement.
	Thus, the !var style makes sense when we read it, and also works with the code
	by making false's run, instead of true's, when we need them to.
	
*/

#include <iostream>

using namespace std;

int main()
{

	bool x = false;

	if (x) {  // false
		cout << "This will not run" << endl;
	}

	if (!x) {  // true
		cout << "This will run" << endl;
	}

	// Output: This will run
	
	return 0;
}
