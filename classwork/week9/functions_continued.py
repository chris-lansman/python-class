# Variable 'scope'
# The scope of a variable is "how long" that variable is valid for. 
# The scope of variables is very important to take note of and track.
# If you fail to track the scope, you may make a change to a variable in 
# one scope and then fail to have the correct value in another.

# There are two types of scope in python:
#   Global - variable is valid anywhere in the file
#   Local - variable is only valid in the context of its current scope


# This is an example of a GLOBAL variable
# x = 50
 
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
 
# func(x)
# print('x is still', x)

# Using the 'global' keyword to modify a variable within a different scope
# def func():
#     global x
#     x = 2
 
# func()
# print('x is', x)

# Failure to pay attention to scope
# def func(x):
#  This is an example of a LOCAL variable
#     y = x
#     print("y is ", y)

# func(8)
# print(y)
