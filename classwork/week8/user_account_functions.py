known_users = ['chris', 'bob']
# Get user name from the console
def get_user_name():
    return str.lower(input("Enter user name:"))

# See if the user exists in our known list
def verify_user_exists(user_name):
    for user in known_users:
        # User found
        if user == user_name:
            return True
        else:
            # User not found
            return False
        
# Function to add user the known account list
def add_user_to_list(user_name):
    known_users.append(str.lower(user_name))
    print("User list updated")
    print_known_user_list()
# Let's say a user would like to remove their account from the system
# We can add a simple function to add more functionality to our program
def delete_user_account(user_name):
    if user_name in known_users:
        print(f"Removing user: {user_name} from the list of known users")
        known_users.remove(user_name)
# Lets add another helper function to print the user list on the fly
def print_known_user_list():
    print("Known users:")
    print(f"       {known_users}")
# Lets add another layer, lets have a function which uses another function to trigger some functionality
def remove_and_add_user(remove_user, add_user):
    delete_user_account(remove_user)
    add_user_to_list(add_user)