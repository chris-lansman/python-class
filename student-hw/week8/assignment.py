# What is a function in programming?
#   A: A function is a modular piece of software that can be reused in other programs.
# What does the following code output?
    # def hello_world():
    #     # block belonging to the function
    #     print('hello world')
    # # End of function
# hello_world()  # call the function
# hello_world()  # call the function again
#   A: hello world
#      hello world

# What is a “parameter” to a function?
#   A: A parameter is an optional variable that can be passed to a function.

# Run the following code and note the output:
# def print_max(a, b):
#     if a > b:
#         print(a, 'is maximum')
#     elif a == b:
#         print(a, 'is equal to', b)
#     else:
#         print(b, 'is maximum')
 
# # directly pass literal values
# print_max(3, 4)
#   A: 4 is maximum

# What is a ‘local variable’?
#   A: A local variable is a variable who's scope is only "local" i.e. valid in a specific context of code. This could be
#   a function, a if block, or any loop block. It is no longer valid when the block ends.

# What is ‘scope’ in terms of variables?
#   A: Scope means "lifetime", i.e. how long a variable is valid for.

# Try the following code to see the difference between a local variable and a specifically scoped variable:
# x = 50
 
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
 
# func(x)
# print('x is still', x)