# Check for users, 
# delete, 
# changepasswords

import os
import pwd, grp


def current_users():
	users = []
	for p in pwd.getpwall():
    	users.append(p[0])
    return users

def get_users():
	with open("users.txt", "r") as users_file:
		users = users_file.read().splitlines() 

	return users


file_users = get_users()
current_users = current_users()
