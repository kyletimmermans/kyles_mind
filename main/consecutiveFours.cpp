/*
        Find four consecutive values in a list

        E.g. 123477779

        1  2  3  4    7        7        7       7    9
                    [i-3] == [i-2] == [i-1] == [i]

        If the 3 values before and up to the current value all
        match, we have 4 values that are all the same and right next
        to each other, thus we have 4 consecutive numbers that are the same.
        
        The -1, -2, -3 ... and so on checks that the positions are right next to
        each other (all connected), and the '==' checks that they are the same number
                -[] position and == makes sure we have consecutiveness
*/                      

#include <iostream>

using namespace std;


bool isConsecutive(int values[], int size)
{
        bool isCons = false;

        for (int i = size - 1; i >= 0; i--)
        {
                if (values[i] == values[i-1] && values[i] == values[i-2] && values[i] == values[i-3])
                {                               // Check that each of the 3 previous
                        isCons = true;          // values before the current value, are all matching (4 matching values)
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
