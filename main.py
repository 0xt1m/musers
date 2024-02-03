# Check for users, delete, changepasswords

import os


def get_users():
	with open("users.txt", "r") as users_file:
		users = users_file.read().splitlines() 

	return users


print(get_users())