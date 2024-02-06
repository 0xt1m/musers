import os
import subprocess
import pwd, grp

DEFAULT_USERS_FILE = "default_users.txt"
USERS_FILE = "users.txt"

def current_users():
	users = []
	for p in pwd.getpwall():
		users.append(p[0])
	return users

def get_users(u_file):
	with open(u_file, "r") as users_file:
		users = users_file.read().splitlines() 

	return users

def delete_user(username):
    try:
        subprocess.run(['userdel', '-r', username], check=True)
        print("[+] Successfully deleted")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting user {username}: {e}")


default_users = get_users(DEFAULT_USERS_FILE)
users = get_users(USERS_FILE)

current_users = current_users()

for user in current_users:
	if user not in default_users and user not in users:
		print("[!] Check this out")
		print(f"[!] User: {user} is not in any of your lists")
		rm_user = "0"
		while rm_user == "0":
			rm_user_input = input(f"[!] Do you want to delete user {user}? [y/n] ").lower()
			if rm_user_input == "y": 
				rm_user = True
			elif rm_user_input == "n":
				rm_user = False
			else: 
				pass
		
		if rm_user == True:
			print(f"[+] Deleting user: {user}")
			delete_user(user)