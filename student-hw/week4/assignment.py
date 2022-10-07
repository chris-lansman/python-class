# https://docs.google.com/document/d/1HVnGl5aEmlXxEhY-1ChkUBqqq2CJBk_huc7-6hSxJfs/edit#heading=h.of1d8kugmv5v
# 
# 
# 
# 2) Answer the following questions regarding strings:
# a)Is the python class for a string called “str”?
#   A: Yes
# b)Name two ways you can create a string in python?
#  A: Implicityly: s = "hello"
#  A: Explicitly: s = str("hello")
# c)What is the output of the following bit of code?
    # name = “Chris”
    # print(name)
#   A: Output: Chris
# d) What is the output of the following bit of code?
    # pi = 3.14
    # print(“The value of pi is “ + str(pi))
    # A: Output: The value of pi is 3.14
# e) What is the purpose of the “str()” class in question d?
#   A: If you did not explicitly convert the floating point value of pi(3.14) to a string type the compiler would have thrown an error and not run the program.
# What does the method str.lower() do?
#   A: Takes a string and converts every character to a lower case character
# What does the method str.find() do?
#   A: The method will search for a substring within a string and return the index to the first letter in the substring it found in the original string.
# Are strings arrays?
#   A: Yes
# What is the first “index” value in a string?
#   A: 0
# What does ‘slicing’ a string mean?
#   A: Slicing is a method of splitting a string up into smaller parts
# Given a string s = “Hello”
# Hint: You can copy this code into a python file and run each one of these and print their output to see what the answers are.
# What does s[1:4] give us? 
#   A: ell
# What does s[0:3] give us?
#   A: el
# What does s[:] give us?
#   A: hello
# What does the int() class do?
#   A: Holds integer values, creates an int object from the int class. Allows us to work with numbers.
# Hint: try running ‘help(int))’ inside the python command line interpreter
# What does the str() class do?
#   A: Holds text strings. Allows you to work with strings.
# Hint: try running help(str)) inside the python command line interpreter 
# Given the following string: s = “3”
# What does print(s) return?
#   A: 3
# What does print(int(s)) return?
#   A: 3
# What does int() do in this case?
#   A: Converts the string "3" into the intenger value 3
# Given the following string: s = “3.14”
# What does print(s) return?
#   A: 3.14
# What does print(int(s)) return?
#   A: Error, the compiler is not smart enough to know how to convert the string "3.14" into an integer value. Had the value been a floating point to start ex) s = 3.14,
# then the compiler would have been able to properly round it down.
# Hint: There is an error here, don't try and solve it just see what the interpreter does when you attempt to run this code.
# What does print(float(s)) return?
#   A: 3.14
