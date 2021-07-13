#include <iostream>

using namespace std;

int main() {

	// Only odd numbers of chars stack properly (needs spaces along side stars)

	int size;

	cout << "Enter size of diamond: ";
	cin >> size;

	// Top half of diamond (short lines to long lines)
	for (int i=1; i<=size; ++i) {  // 1, 2, 3, 4, ...
		cout << string(size-i, ' ');  // Less stars, more spaces
		for (int j=1; j<=i; ++j) { 
			cout << '*' << ' ';  // Extra space events out the diamond so it lines up
		}

	    cout << endl; // Next line
	}

	// Bottom half of diamond (long lines to short lines)
	// Size-1 bc we want a mirror affect and symmetry over one longest line, not 2
	for (int i=size-1; i>=1; --i) {  // 10, 9, 8, 7, ...
		cout << string(size-i, ' ');
		for (int j=i; j>=1; --j) {
			cout << '*' << ' ';
		}

		cout << endl; // Next line
	}

	return 0;
}
