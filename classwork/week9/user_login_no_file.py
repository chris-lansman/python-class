import getpass
from password_cipher import *

known_users = {'bob':'slwwcbrj'}

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
        
login()
print(known_users)