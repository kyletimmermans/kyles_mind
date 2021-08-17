/*

When iterating and adding/subtracting values to a stack:

stackSize must be a static number because using myStack.size() causes problems as 
push() or pop() will continue to change size() and change the end condition. We want to stop when 
we reach size() but push() changes size() while in the for-loop

If we use a static number, push() won’t break it, because it won't change
the end condition

*push() or pop() breaks size() because they change the number of size()
while going through the iteration

*/

#include <iostream>
#include <stack>

using namespace std;

int main()
{

	stack<int> myStack;    //  10 - Top of stack
	myStack.push(40);      //  20
	myStack.push(30);	   //  30
	myStack.push(20);      //  40 - Bottom of stack
	myStack.push(10);



	/*
		i(0) ++     myStack.size(3) --
		i(1)		myStack.size(2)

		1 < 2 and that is the end condition,
		ending the for loop prematurely
	*/
	for (int i = 0; i < myStack.size(); ++i) {		
		myStack.pop();
	}


	// Instead, use a while-loop to prevent
	// the i and size() end condition problem
	while (!myStack.empty()) {
		myStack.pop()
	}


	return 0;
}

