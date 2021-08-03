/*
	Reverse the first half of a Stack in C++

	Stack: FILO - First in, Last out (Like dropping things into a vertical tube)
*/

#include <iostream>
#include <stack>

using namespace std;

stack<int> stackHalfReverse(stack<int> aStack) {
	int stackHalfSize = aStack.size() / 2;  // Declare stack half now, bc it changes a lot below,
						// Don't want stack size to change while we're on it

	int tempArray[stackHalfSize]; // Hold the first half of stack

	for (int i = 0; i < stackHalfSize; ++i) {  // issue here
		tempArray[i] = aStack.top();  // Save first half of stack
		aStack.pop();  // Remove the element we just saved
	}

	for (int i = 0; i < stackHalfSize; ++i) {  // Put it back in backwards (reversed)
		aStack.push(tempArray[i]);
	}

	return aStack;
}


int main()
{	
	/*		
		10 - Top of Stack (First out)
		20
		30
		40
		50
		60
		70
		80
		90
		100 - Bottom of Stack (Last out)
	*/

	stack<int> myStack;    
	myStack.push(100);				
	myStack.push(90);
	myStack.push(80);
	myStack.push(70);
	myStack.push(60);
	myStack.push(50);
	myStack.push(40);
	myStack.push(30);
	myStack.push(20);
	myStack.push(10);

	myStack = stackHalfReverse(myStack);  // Reverse stack

	/*		
		50 - Top of Stack (First out)
		40
		30
		20
		10
		60
		70
		80
		90
		100 - Bottom of Stack (Last out)
	*/

	// Print results
	while (!myStack.empty()) { // While stack not empty (if empty is false, run)
		cout << myStack.top() << endl;
		myStack.pop();
	}

	return 0;
}
