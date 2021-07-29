/*
	When putting files into a folder, the files
	will be sorted based off the number of the
	ASCII character that starts the filename.

	For instance, A.pdf would come before B.pdf
	because 'A' has a smaller ASCII number than 'B'.

	
	However, if the files start with the same character:

	e.g. A1.pdf  and A2.pdf


	It will keep checking which characters
	come first until there is a difference
	between the filenames. In this case, 'A'
	is the same and then '1' comes before '2',
	so A1.pdf will come before A2.pdf. 
*/

#include <iostream>
#include <string>

using namespace std;

int main()
{	

	string str1 = "hellworld7.pdf";
	string str2 = "hellworld4.pdf";


	// If one filename length is greater than another, 
	// it takes up more char positions, thus, 
	// it goes after the smaller ones, because
	// the comparisons can keep going for the longer filename strings
	if (str1.length() > str2.length()) {
		cout << str2 << endl;
		cout << str1 << endl;
	} else if (str1.length() < str2.length()) {
		cout << str2 << endl;
		cout << str1 << endl;
	}


	// Increment through both filename strings and keep comparing the
	// chars that are in the same positions in both strings
	for (int i = 0, j = 0; (i < str1.length() || j < str2.length()); ++i, ++j) {
		if (int(str1[i]) < int(str2[j])) {   // If str1 char is less, it goes first 
			cout << str1 << endl;
			cout << str2 << endl;
		} else if (int(str2[j]) < int(str1[i])) {  // If str2 char is less, it goes first
			cout << str2 << endl;
			cout << str1 << endl;
		}
	}     // If it's the same char, go to next position in both strings

	
	return 0;
}