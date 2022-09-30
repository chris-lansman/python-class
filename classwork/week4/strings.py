## STRINGS

my_string = "hello"

print("String length:", len(my_string))
#print(f"My string is {str(len(my_string))} characters long")
# Understanding how strings are stored in python
# Strings are accessible via 0-based array index notation
# print(my_string[0])
# print(my_string[1])
# print(my_string[2])
# print(my_string[3])
# print(my_string[4])

# # Finding the length of a string
# print(len(my_string))

# # You can "concatenate" strings
# print(my_string + " there!")
# # This is using a new syntax called a "formatted" string
# print(f"{my_string} there!")

# # Printing multi line strings without the newline (\n) special character
# multi = """This is a multi line
# string and allows you to put in new lines without having to explicitly express them"""
# print(multi)

# String slicing
# Note: Slicing is not "inclusive" (does not include) the right digit's character in a string
# print(my_string[0:1])
# print(my_string[0:2])
# print(my_string[0:3])
# print(my_string[0:4])
# print(my_string[0:5])
# # What do you think will happen here?
# print(my_string[0:10])
# print(my_string[99])

####################################
# Most commonly used string methods
####################################
s = " This IS a STRING "

# # returns the lowercase
# print(s.lower())
# # returns uppercase version of the string
# print(s.upper())
# returns a string with whitespace removed from the start and end
# print(s.strip())
# # tests if the string starts or ends with the given other string
# print(s.startswith('This'))
# print(s.endswith('STRING'))
# # searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
# print(s.find('a'))
# # returns a string where all occurrences of 'STRING' have been replaced by 'SOME OTHER STRING'
# print(s.replace('STRING', 'SOME OTHER STRING'))
# # returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
# print(s.split(' '))
# # opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
# test = ['This', 'Python', 'Class', 'Rocks!']
# s = '->'
# print(s.join(test))

#####################################
# Type conversions
#####################################
# pi = 3.14
# print(type(pi))
# # In python you can convert basic types (i.e. string, float, int), to other types by "casting them"
# print(type(str(pi)))
# print(type(int(pi)))

# # Python does not automatically convert strings to values
pi = 3.14
# print("Value of PI is:", pi)
# print("Data type of pi:", type(pi))

# # What do you think this will do?
# print(pi + 5)
# print(pi + "5")

# Explicit casting. We are explicitly telling the interpreter to change the data type of pi
# pi = str(pi)
# print("After the explicit cast data type of pi:", type(pi))

# # What do you think this will do?
# print(pi + pi)
# print(pi + "huh?")

#################################################################################
# Using % operators in python (these are C/C++ style printf formatters)
#################################################################################
# %s - string
# %d - integer value
# %f - float value
#Example
# print("There are %d apples in my %s, and Pi is %f" % (5, "basket", 3.14))