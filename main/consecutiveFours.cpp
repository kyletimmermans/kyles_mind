/*
        Find four consecutive values in a list
               -Consecutive = All in a row and all equal
        
        E.g. 12344445
        
        1  2  3         4            4             4          4      5
                  [i-3] == 4   [i-2] == 4    [i-1] == 4   [i] == 4
                  
        If the 3 values before and up to the current value all
        equal 4, then we have 4 fours right next to each other (in a row), 
        thus we have 4 consecutive 4s.
        
        The -1, -2, -3 ... and so on checks that the positions are right next to
        each other (all connected), and the '==' checks that they are equal to 4.
                -  [] gets their positions
                        -Get a group of 4 indexes (make a group)
                -  == makes sure we have consecutiveness as they all need to equal 4
                        -Make sure they all equal 4 (all the same)
*/   


#include <iostream>

using namespace std;


bool isConsecutive(int values[], int size)
{
        bool isCons = false;

        for (int i = size - 1; i >= 0; i--)
        {       
                // Check that each of the 3 previous, values before the current value, are all matching (4 matching values)
                // We don't have to check if they are all equal to each other, if each index's value equals 4, then they are all the same
                if (values[i] == 4 && values[i-1] == 4 && values[i-2] == 4 && values[i-3] == 4)
                {
                        isCons = true;
                }
        }

        return isCons;
}

int main()
{
        int size;
    
        cout << "Enter the number of values: ";
        cin >> size;

        int values[size];  // Create array after we know it's size

        for (int i = 0; i <= size - 1; i++)
        {   
                cout << "Enter a value: ";
                cin >> values[i];
        }   
        
        if (isConsecutive(values, size) == true)  
                cout << "The list has consecutive fours!" << endl; 
        else  
                cout << "The list has no consecutive fours!" << endl;  

        return 0;
}
