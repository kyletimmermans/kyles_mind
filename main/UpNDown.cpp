#include <iostream>

using namespace std;

int main()
{
	/*
		For loops start with initializer and then keep checking
		condition until we reach it.
			-Iterate up or down and the check condition

		Conditions with '>' or '<' and without '='' means one before target 
		and conditions with '=' (<= or >=) means up to and on top of target.
			
			* When no '=' in condition, target cannot be > than itself or < itself


						        -
					   	   -    #
				      -    #    #     
			     -    #    #    #		5 is not less than 5 (5 < 5)
			-    #    #    #    #         
			#    #    #    #    #
	 		-    -    -    -    -
		   < 5  < 5  < 5  < 5  == 5
	*/
	for (int i = 1; i < 5; ++i)
		cout << i << endl;


	/*
		   -
		   #    -	
		   #    #    -
		   #    #    #	  -     		1 is not greater than 1 (1 > 1)
		   #    #    #    #    -
		   #    #    #    #    #  
		   -    -    -    -    -
		  > 1  > 1  > 1   > 1  == 1
	*/
	for (int j = 5; j > 1; --j)
		cout << j << endl;


	return 0;
}