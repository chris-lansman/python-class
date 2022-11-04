#2: Functions are reusable pieces of programs.
# #3: def hello_world():
    # block belonging to the function
    # print('hello world')
# End of function
 
# hello_world()  # call the function
# hello_world()  # call the function again-----returns hello world, hello world

#4: Function parameters are are values you give to a function so it can do something with those values.

# #5: def print_max(a, b):
#     if a > b:
#         print(a, 'is maximum')
#     elif a == b:
#         print(a, 'is equal to', b)
#     else:
#         print(b, 'is maximum')
 
# # directly pass literal values
# print_max(3, 4)---returns 4 is maximum

#6: Local variables are variables that when used inside a function, it does something differently than when it is operated outside the function.
#6a: The scope of the variable is the use of that variable depending on its location.

# #7: 
# x = 50
 
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
 
# func(x)
# print('x is still', x)----returns "x is 50, Changed local x to 2, x is still 50"
