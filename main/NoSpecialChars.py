username = "user1"


# It is False if there are no True's in any()
#ㅤㅤ--------------------------------------------
#ㅤㅤ|ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ^
#ㅤㅤvㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ|
if any(not c.isalnum() for c in username) == False:



# Where True indicates c.isalnum() being False
#ㅤㅤㅤㅤㅤ|ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ|	
#ㅤㅤㅤㅤㅤ|ㅤㅤㅤㅤㅤ----------------------------
#ㅤㅤㅤㅤㅤ|ㅤㅤㅤㅤㅤ|
#ㅤㅤㅤㅤㅤvㅤㅤㅤㅤㅤv    
if any(not c.isalnum() for c in username) == False:



# c.isalnum() being False means there is a special char in the username
#ㅤㅤㅤㅤ|ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ|			
#ㅤㅤㅤㅤ-----------ㅤㅤㅤㅤㅤㅤㅤ------------------------
#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ|ㅤㅤㅤㅤㅤㅤㅤ|
#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤvㅤㅤㅤㅤㅤㅤㅤv
if any(not c.isalnum() for c in username) == False:


'''
Therefore, if there are no True's in any() "== False", then there were
no isalnum() False's turned into True's by the not keyword,
and since there were no False's from isalnum(), then there were no
special characters.

So if we get all False's in the any() e.g. any(False, False, False) then
all of the c.isalnum() were True and became False of the 'not' keyword and if
isalnum() was True for every character, then all of the characters were
alphanumeric and not special characters.

And if we even get one True in the any() e.g. any(False, True, False). then
one of the c.isalnum() was False and became True because of the 'not' keyword
and if isalnum() was False, then one of the characters in the username was
not alphanumeric and therefore a special character.
'''
