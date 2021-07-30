#include <iostream>

using namespace std;

class A {  // Create a class 'A' with a public int b = 5
   public: int b;
   A() { b = 7; }
};

int passByValue(int x) {
	return ++x;  // This will not affect the original value that is passed in
}		  // It will only affect the copy that is made

void passByReference(int &var1, int &var2) {  // Pass in the address of var1 and var2
	var1 += 1;
	var2 += 1;
}

void passByPointer(int *ptr) {  // Pass a pointer (a derefernced address), and change the value
	*ptr = 200;					// So the same address has a new value stored
}	


int main()
{	
	// Normal pointer
	cout << "\nNormal pointer" << endl;
	int myVar = 4;  // Initialize a variable called myVar
	int *myPointer = &myVar;  // Get the memory address of myVar, store in a pointer called myPointer
	cout << myPointer << " | " << *myPointer << endl;  // Dereferencing the pointer again gives actual value
	cout << endl;

	// Dot operator
	cout << "Dot operator" << endl;
	A a = A();  // Create object a from class A
	cout << a.b << endl;  // Pull b from a
	cout << endl;

	// Arrow operator
	cout << "Arrow operator" << endl;
	A* x = &a;  // Create pointer x to class A
	cout << x->b << endl; // Pull b from x
	cout << endl;

	// Pass by value
	cout << "Pass by value" << endl;
	int c = 70;  // No change to original value
	int d = passByValue(c);  // Copy receives change only
	cout << c << endl;
	cout << d << endl;
	cout << endl;

	// Pass by reference
	cout << "Pass by reference" << endl;
	int y = 1, z = 2;
	cout << "y = " << y << ", z = " << z << endl;  // Before pass by reference
	passByReference(y, z);
	cout << "y = " << y << ", z = " << z << endl;  // After pass by reference
	cout << endl;

	// Pass by pointer
	cout << "Pass by pointer" << endl;
	int test = 50;
	int *v = &test;
	cout << "&v = " << v << ", *v = " << *v << endl;  // Before pass by pointer
	passByPointer(v);
	cout << "&v = " << v << ", *v = " << *v << endl;  // After pass by pointer
	cout << endl;

	// Pointer arithmetic
	cout << "Pointer arithmetic" << endl;
	int myArr[3] = {10, 100, 1000};
	int *arrPtr = myArr;
	cout << *arrPtr++ << " " << *arrPtr++ << " " << *arrPtr << endl; // ptr++ goes to next mem address
	cout << *arrPtr-- << " " << *arrPtr-- << " " << *arrPtr << endl; // ptr-- goes down a mem address
	*arrPtr += 10;  // We can add integers to a pointer (+ or +=)
	cout << *arrPtr << endl;
	*arrPtr -= 20;  // We can subtract integers from a pointer (- or -=)
	cout << *arrPtr << endl;
	cout << *v-*arrPtr << endl; // We can also get the difference between two pointers
	cout << endl;

	return 0;
}