# Python basic program logic control flow

# This week we are only going to dive into using the 'if' statement along with our comparison operators we learned.

# The most basic if check:
# if True:
#     print("This was a true statement!")
    
# Breaking down the "syntax" of a control statement.
#   The start of the control statement uses a keyword, 'if'
#   Followed by a comparison statement to evaluate
#   finally ending with a colon ':' which tells the compiler where the logical expression ends.
# Note: Spacing is beginning to come into play here. You HAVE TO HAVE at least one space on the line following the logic statement. 
# If not the compiler will not know which code to execute (more examples of what this means to follow)

# This would NOT compile
# if True:
# print("Hello")

# A slightly more complicated if check:
# if 3 < 5:
#     print ("3 is greater than 5")

# Lets try combining our new if check with what we learned from a previous class and take input to evaluate
# Note: DONT FORGET to wrap the 'user_input' in a type conversion since input is returning a string value
# and not an integer value. You cannot compare a string to a integer here.
# user_value = input("Enter a number:")
# if (int(user_value) > 5):
#     print("The user entered value was greater than 5!")


# ### Simple, fun guessing game
# number = 23
# guess = int(input('Enter an integer : '))

# if guess == number:
#     # New block starts here
#     print('Congratulations, you guessed it.')
#     print('(but you do not win any prizes!)')
#     # New block ends here
# elif guess < number:
#     # Another block
#     print('No, it is a little higher than that')
#     # You can do whatever you want in a block ...
# else:
#     print('No, it is a little lower than that')
#     # you must have guessed > number to reach here

# print('Done')
# # This last statement is always executed,
# # after the if statement is executed.