#include <stdio.h> // Header files
#include <stdlib.h>

// main func w/ args
int main(int argc, char **argv) 
{

   // If no args or more than one arg (argv[0] - program name, argv[1] - year)
   if (argc != 2) {
      printf("Too few / too many args given!");
      exit(1); // Exit with error
   }

   // atoi() converts char array to int
   int year = atoi(argv[1]);

   /* 
      Is divisible by 4 && not divisible by 100 = leap year
      Is divisible by 400 = leap year
      Everything else = not leap year
   */
   if ((year % 4 == 0) && (year % 100 != 0)) { // Fits both criteria
      printf("%s was a leap year\n", argv[1]);  
   } else if (year % 400 == 0) {  // Fits one criteria but gets second chance
      printf("%s was a leap year\n", argv[1]);
   } else {  // Fits no criteria
      printf("%s was not a leap year\n", argv[1]);
   }
   
   
   /*
      Can also be written as a one-liner:
      
      if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
         leap year
      else
         not leap year
   */
   
   
   /*
        Explanation of if-statement flow:
        
        1. If condition1 && condition2 are both true, then leap year
        2. If either condition1 && condition2 is false,
           we check the next if-statement if condition3 is true
        
        
        2 trues:
        condition1==true && condition2==true --> leap year
        
        1 true, 1 false:
        condition1==true && condition==false
        |
        |
         ---> condition3==true --> leap year
         
        
        * condition 1 and 2 or just condition 3 (1 && 2) || 3
         
        * E.g. Blue and yellow makes green
          Also just green makes green
   */
   
   // Terminate program successfully
   return 0;
}
