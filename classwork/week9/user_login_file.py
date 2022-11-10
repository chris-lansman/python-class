# Built-in python library that allows taking in a password without revealing it on the command line
import getpass
# Helper functions to encrypt and decrypt our password
from password_cipher import *
# Allows us to read in our password file 
import json

import os
# Current working directory (cwd)
# This bit of snazzy code will sort out where on your computer this file is being run from
# It will save off this value and then add on one last backslash (\) so its the proper path.
# You have to "escape" a backslash as its a special character with another backslash to tell
# the interpreter you wanted just one '\'
cwd = os.path.dirname(__file__)
cwd = cwd + "\\"

# Empty user list
known_users = {}

# Reads a json formatted username/password file and stores it into known_users
def load_user_database():
    with open(cwd + 'passwords.json') as file:
        data = file.read()
    global known_users
    known_users = json.loads(data)

# Writes the current known_user's dictionary to our password.json file
def write_users_to_file():
    # Serializing json
    json_object = json.dumps(known_users, indent=4)
    with open(cwd + "passwords.json", "w") as outfile:
        outfile.write(json_object)
        
# Checks the entered password against the stored password
def check_password(user_name):
    password = getpass.getpass()
    encrypted_password = encryptPassword(password)
    if encrypted_password == known_users.get(user_name):
        return True
    else:
        return False

# Let the user specify the message to encrypt/decrypt:
def login():
    user_name = input("Enter user name:")
    if user_name in known_users:
        if check_password(user_name):
            print("Successfully logged in!")
        else:
            print("Login failed, incorrect password, please re-enter")
    else:
        print("User does not exist! Adding user to database")
        print("Please create a password")
        known_users.update({user_name:''})
        password = getpass.getpass()
        known_users[user_name] = encryptPassword(password)

# Print the known_users list before we get started
print("Known users before we load file:", known_users)
# print the known users list once we have loaded it from the file
load_user_database()
print("Known users after we load file:", known_users)
login()
print("Final known users:", known_users)
write_users_to_file()