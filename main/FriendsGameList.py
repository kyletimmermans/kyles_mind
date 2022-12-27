import pandas as pd
from tabulate import tabulate

friends_data = [
    ['user2', 'Halo'],
    ['user2', 'Smash Bros'],
    ['user3', 'Halo'],
    ['user4', 'CoD'],
    ['user4', 'Smash Bros']
]

final_data = pd.DataFrame(columns=["Friends", "Games Owned"])

'''
Following for-loop logic: 

Get all games of one friend until we hit the next friend,and store 
all the games of that one friend in their 'Games Owned' column, 
then do that friend's games, and so on...

When current user changes, the new user becomes the current user.
If we see the same user again (last_friend), then keep going
'''
print("For-Loop Logic Path:\n")
last_friend = ""
for i in range(len(friends_data)):
    # Until new friend
    temp_friend = friends_data[i][0]
    if temp_friend == last_friend:
        continue
    print(temp_friend)
    # On next user, don't repeat the same user
    last_friend = temp_friend
    games = []
    j = i
    # For each friend's games
    while friends_data[j][0] == temp_friend:
        games.append(friends_data[j][1])
        print("   "+friends_data[j][1])
        j = j + 1
        # If we get to the end, don't go further
        if j == len(friends_data):
            break
    
    final_data.loc[i] = [temp_friend, ', '.join(games)]

print("\n\nFinal Table:\n")
print(tabulate(final_data, showindex=False, headers='keys', tablefmt='psql'))


'''
For-Loop Logic Path:

user2
   Halo
   Smash Bros
user3
   Halo
user4
   CoD
   Smash Bros


Final Table:

+-----------+------------------+
| Friends   | Games Owned      |
|-----------+------------------|
| user2     | Halo, Smash Bros |
| user3     | Halo             |
| user4     | CoD, Smash Bros  |
+-----------+------------------+
'''
