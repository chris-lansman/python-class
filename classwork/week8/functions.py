# Functions are reusable pieces of programs. 
# They allow you to give a name to a block of statements, 
# allowing you to run that block using the specified name 
# anywhere in your program and any number of times. This is 
# known as calling the function. We have already used many 
# built-in functions such as len and range.

# The function concept is probably the MOST 
# important building block of any non-trivial software (in any programming language)

# Python syntax to define a function:
#   def function_name():
#       def - keyword that tells the interpreter you are about to define a function
#       function_name - the name of your function
#       () - parenthesis tells users if your function takes and "parameters"

# Our first function hello_world
# def hello_world():
#     print("Hello world!")
# # IMPORTANT: The interpreter does not "know" you want to call the function called hello_world
# #            unless you explicitly tell it you wanted to. If you do not do so with '()'
# #            then the interpreter will assume you are only referencing the function object..
# # Ex) Not a function call....
# hello_world
# print(type(hello_world))
# # Ex) An actual function call with proper syntax...
# hello_world()
# print(type(hello_world()))

# Lets put our "programming hats on!"
#   We want to write a program that solves for the area of a number of shapes
#   We want to make this program available to others so they dont have to re-write it themselves.
#   ---Brainstorming---
#       Calculate the area of a square
#       Calculate the area of a rectangle
# In the old days we might have done something like this...
# num_side1 = 2
# num_side2 = 4
# print(f"The area of this rectangle is {num_side1*num_side2}")
# # Now we want to do it again for a different rectangle and maybe take the input from a user
# num_side1 = input("Input a first side value:")
# num_side2 = input("Input a second side value:")
# print(f"The area of this rectangle is {int(num_side1)*int(num_side2)}")
# Lets 'function'ify' this code
# Define a function which calculates the area of a square or a rectangle
# def calculate_area(side1, side2):
#     if (int(side1) == int(side2)):
#         print(f"The area of this square is {int(side1)*int(side2)}")
#     else:
#         print(f"The area of this rectangle is {int(side1)*int(side2)}")
    
# # num_side1 = input("Input a first side value:")
# # num_side2 = input("Input a second side value:")
# # calculate_area(num_side1, num_side2)

# # **** Let's take this idea a step further ****
# # Define a function which:
# # 1) gathers user input
# # 2) verifies the input
# # 3) returns back integer value
# def get_user_input():
#     while True:
#         # Verify the input, if its good, convert and return
#         # else retry entry
#         side_val = input("Give me an integer number:")
#         if side_val.isdigit():
#             break
#         else:
#             print("Error, you did not provide an integer value, please re-try your entry")
#     return int(side_val)

# # Now that we 'know' we have valid integer input we can drop the conversions
# # which are "dangerous" in that if they error out we have no way to recover 
# # from the failure with this basic code (there are ways to recover which are more advanced)
# def calculate_area(side1, side2):
#     if (side1 == side2):
#         print(f"The area of this square is {side1*side2}")
#     else:
#         print(f"The area of this rectangle is {side1*side2}")
            
# # Get user's input
# side1 = get_user_input()
# side2 = get_user_input()
# # Calculate the area
# calculate_area(side1, side2)
    
# Real world problem statement:
#   Create a program which allows a user to do the following:
#   1) Login to the system
#   1a) if the user does not exist, allow them to create an account
#   1a.1) If a new account is created add it to the list of known accounts
# known_users = ['chris', 'bob']
# def get_user_name():
#     return str.lower(input("Enter user name:"))

# # See if the user exists in our known list
# def verify_user_exists(user_name):
#     for user in known_users:
#         # User found
#         if user == user_name:
#             return True
#         else:
#             # User not found
#             return False
# # Add user to the database
# def add_user_to_list(user_name):
#     known_users.append(str.lower(user_name))

# while True:
#     user_name = get_user_name()
#     if verify_user_exists(user_name):
#         print(f"User {user_name} found. Welcome back!")
#     else:
#         print(f"User {user_name} not found, adding user to list of known users")
#         add_user_to_list(user_name)
#     break
# print(known_users)

# # Let's say a user would like to remove their account from the system
# # We can add a simple function to add more functionality to our program
# def delete_user_account(user_name):
#     if user_name in known_users:
#         print(f"Removing user: {user_name} from the list of known users")
#         known_users.remove(user_name)
        
# delete_user_account("chris")

# print("Known users left in the list:")
# print(known_users)

# # Lets add another helper function to print the user list on the fly
# def print_known_user_list():
#     print("Known users left in the list:")
#     print(f"       {known_users}")

# print_known_user_list()

# # Lets add another layer, lets have a function which uses another function to trigger some functionality
# def remove_and_add_user(remove_user, add_user):
#     delete_user_account(remove_user)
#     add_user_to_list(add_user)
    
# # Now lets add one user and remove another
# remove_and_add_user('chris', 'kenny')
# print_known_user_list()
# from user_account_functions import *

# while True:
#     user_name = get_user_name()
#     if verify_user_exists(user_name):
#         print(f"User {user_name} found. Welcome back!")
#     else:
#         print(f"User {user_name} not found, adding user to list of known users")
#         add_user_to_list(user_name)
#     break
        
# delete_user_account("chris")
# print_known_user_list()
# remove_and_add_user('chris', 'kenny')
# print_known_user_list()