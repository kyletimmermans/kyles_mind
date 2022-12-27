username = "user1"


# It is False if there are no True's in any()
#    --------------------------------------------
#    |								  			                  ^
#    v								  			                  |
if any(not c.isalnum() for c in username) == False:



# Where True indicates c.isalnum() being False
#	    |						                         |	
#	    |	        ----------------------------
#	    |         |
#	    v	        v    
if any(not c.isalnum() for c in username) == False:



# c.isalnum() being False means there is a special char in the username
#	  |				   				     		                    |			
#	  -----------		  	     ------------------------
#				      |		         |
#           	v   	       v
if any(not c.isalnum() for c in username) == False:


'''
Therefore, if there are no True's in any() "== False", then there were
no isalnum() False's turned into True's by the not keyword,
and since there were no False's from isalnum(), then there were no
special characters.
'''
