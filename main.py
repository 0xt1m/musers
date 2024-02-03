# Check for users, 
# delete, 
# changepasswords

import os
import pwd, grp

for p in pwd.getpwall():
    print(p[0], grp.getgrgid(p[3])[0])

def get_users():
	with open("users.txt", "r") as users_file:
		users = users_file.read().splitlines() 

	return users


print(get_users())