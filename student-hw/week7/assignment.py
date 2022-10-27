# What is a ‘list’?
#   A: An ordered data type in python. Can hold many different types of data.
# Give an example snippet of code that creates a list.
#   A: my_list = ['bob', 'mike', 'harry']
# Can python lists hold many different types of data or only one type?
#   A: Many different types, i.e. int, float, other lists, etc
# What does the following code print out?
# my_list = ['a', 3, [2, 1], "hello"]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
#   A: 'a',3,[2,1],hello
# What does the following code print out?
# my_list = ['a', 3, [2, 1], "hello"]
# print(type(my_list[0]))
# print(type(my_list[1]))
# print(type(my_list[2]))
# print(type(my_list[3]))
#   A: str, int, list, str
# Try and make sense of the return types for each of the list elements
# What is a ‘tuple’ in python?
#   A: A type of list that cannot be changed once it has been created.
# Can you modify a tuple once it has been created?
#   A: No.
# What does the following code output?
# my_tuple = ("hello", "world")
# my_tuple[0] = "new string!"
#   A: TypeError: 'tuple' object does not support item assignment
#  What is a ‘dictionary’ in python?
#   A: A ordered list of key/value pairs.
# What is a ‘key’?
#   A: An entry in a dictionary which specifies a unique entry.
# What is a ‘value’?
#   A:  a value associated with a key in a dictionary
# What does the following code print?
# my_dictionary = {"chris": 36, "bob": 27}
# print(my_dictionary["chris"])
#   A: 36
# What happens if we try to find a dictionary entry by its value?
# my_dictionary = {"chris": 36, "bob": 27}
# print(my_dictionary[36])
#   A: KeyError: 36
# What does the following code output? Take note of the index values:
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# print('Item 0 is', shoplist[0])
# print('Item 1 is', shoplist[1])
# print('Item 2 is', shoplist[2])
# print('Item 3 is', shoplist[3])
# print('Item -1 is', shoplist[-1])
# print('Item -2 is', shoplist[-2])
# print('Character 0 is', name[0])
#   A: 
# Item 0 is apple
# Item 1 is mango
# Item 2 is carrot
# Item 3 is banana
# Item -1 is banana
# Item -2 is carrot
# Traceback (most recent call last):
#   File "c:\Users\clansman\OneDrive - NVIDIA Corporation\Documents\PythonClass\ClassFile.py", line 8, in <module>
#     print('Character 0 is', name[0])
# NameError: name 'name' is not defined