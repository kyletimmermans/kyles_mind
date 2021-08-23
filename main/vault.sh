#!/bin/bash

# vault.sh is used to show the importance of if-statement ordering
# We first want to check if the person got the password right,
# then we want to give them another chance if it's still < 3 tries.
# Finally, we want to let them know after 3 tries, that they are locked
# out.

# If we did this in a different order, it would break. What if we
# checked if it was < 3 tries before checking if it was correct?
# We would be re-inputing the password even if it was correct,
# because it still will be true because the try number is < 3
# and that condition brings us back to the top. 

for i in {1..3}
 do
   read -p 'What is the password? ' password
   if [ $password == 'secret' ]; then
      echo 'Welcome!'
      break
   elif [ $i -lt 3 ]; then     # If not correct and < 3
      echo 'Limited to three tries'
   else  # If 3 and not correct, kick out
     echo 'Good Bye'
     break
   fi
 done