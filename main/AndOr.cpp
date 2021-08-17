#include <iostream>

using namespace std;


int main()
{

	bool var1 = true;
	bool var2 = true;
	bool var3 = true;
	bool var4 = true;
	bool var5 = false;


	// && operator needs everything to be true, this will not run
	if (var1 && var2 && var3 && var4 && var5) {
    		cout << "&&" << endl;
	}


	// || operator needs only one thing to be true, this will run
	if (var1 || var2 || var3 || var4 || var5) {
		cout << "||" << endl;
	}


	return 0;
}
