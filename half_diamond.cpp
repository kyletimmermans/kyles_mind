#include <iostream>

using namespace std;

int main() {

	int size;

	cout << "Enter size of diamond: ";
	cin >> size;

	// Top half of diamond (short lines to long lines)
	for (int i=1; i<=size; ++i) {  // 1, 2, 3, 4, ...
		for (int j=1; j<=i; ++j) { 
			cout << '*';
		}

	    cout << endl; // Next line
	}

	// Bottom half of diamond (long lines to short lines)
	for (int i=size; i>=1; --i) {  // 10, 9, 8, 7, ...
		for (int j=i; j>=1; --j) {
			cout << '*';
		}

		cout << endl; // Next line
	}
}