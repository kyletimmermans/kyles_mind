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

   // Is divisible by 4 && not divisible by 100 = leap year
   // Is divisible by 400 = leap year
   // Everything else = not leap year
   if ((year % 4 == 0) && (year % 100 != 0)) { // Fits both criteria
      printf("%s was a leap year\n", argv[1]);  
   } else if (year % 400 == 0) {  // Fits one criteria but gets second chance
      printf("%s was a leap year\n", argv[1]);
   } else {  // Fits no criteria
      printf("%s was not a leap year\n", argv[1]);
   }
   
   // *E.g. Blue and yellow makes green
   //       Also just green makes green

   // Terminate program successfully
   return 0;
}
