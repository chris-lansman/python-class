# Python Data Structures
#   List, Tuple, Dictionary, Sequence, Set

##################
# Lists in Python
##################
# Excerpt from the reading for this week:
# A list is an example of usage of objects and classes. When we use a variable i 
# and assign a value to it, say integer 5 to it, you can think of it as creating 
# an object (i.e. instance) i of class (i.e. type) int.

# A class can also have methods i.e. functions defined for use with respect to 
# that class only. You can use these pieces of functionality only when you have 
# an object of that class. For example, Python provides an append method for the 
# list class which allows you to add an item to the end of the list. For example, 
# mylist.append('an item') will add that string to the list mylist. Note the use 
# of dotted notation for accessing methods of the objects.

#  List syntax
# variable_name = []

# Example - shopping list
# shopping_list = ["apples", "oranges", "pears"]
# print(type(shopping_list))
# print(shopping_list)
# print('I have', len(shopping_list), 'items to purchase.')

# # Useful list methods
# shopping_list.append("bananas")
# print(shopping_list)

# # Sort a list alphabetically
# shopping_list.sort()
# print(shopping_list)

# # A list is really just an 'array' of things
# # Lets try this familiar array access syntax to replace something in the list.
# shopping_list[0] = "watermelon"
# print(shopping_list)

# # Using python to treat our list as an 'iterable'
# # To look for a entry and if found remove it
# for item in shopping_list:
#     if "watermelon" == item:
#         shopping_list.remove("watermelon")
# print(shopping_list)

##########
# Tuples
##########
# Tuple syntax
# variable_name = ()

# Example - shopping list
# shopping_tuple = ("apples", "bananas", "pears")
# print(type(shopping_tuple))

# print('Number of items in the tuple is', len(shopping_tuple))

# IMPORTANT
#   Tuples are IMMUTABLE, they CANNOT be changed once created
# shopping_tuple[0] = "monkey"

###############
# Dictionaries
###############
# A dictionary is like an address-book where a persons name and some information about them is included.
# Its a 'key' - 'value pair' system
# Dictionary syntax 
# variable_name = {}

# # Example store inventory
# store_inventory = {'apple':'3.99',
#                    'orange':'1.99',
#                    'banana':'0.99'}
# # print("An orange costs", store_inventory["orange"])

# # What happens if an item is not found?
# # print("An orange costs", store_inventory["oranges"])

# # How can we print every item in the stories inventory? 
# # Think: iterable....
# # We get an iterable by using the dictionary class method 'items'
# for item, cost in store_inventory.items():
#     print(f"{item} : {cost}")
    
# # Helpful dictionary object function to print the value of each entry
# print(store_inventory.values())

# # Adding a new entry to the dictionary 
# store_inventory.update({"watermelon":'5.99'})
# print(store_inventory.values())

# # Updating a key:value pair in the dictionary
# store_inventory.update({"apple":'11.99'})
# print(store_inventory.values())

##############
# Sequences
##############
# In python the following data types are all sequences and support slicing and indexing
#   strings, lists, tuples
# shop_list = ['apple', 'mango', 'carrot', 'banana']
# name = 'lansman'

# # Indexing or 'Subscription' operation #
# print('Item 0 is', shop_list[0])
# print('Item 1 is', shop_list[1])
# print('Item 2 is', shop_list[2])
# print('Item 3 is', shop_list[3])
# print('Item -1 is', shop_list[-1])
# print('Item -2 is', shop_list[-2])
# print('Item -2 is', shop_list[-3])
# print('Item -2 is', shop_list[-4])
# print('Character 0 is', name[0])

# # Slicing on a list #
# print('Item 1 to 3 is', shop_list[1:3])
# print('Item 2 to end is', shop_list[2:])
# print('Item 1 to -1 is', shop_list[1:-1])
# print('Item start to end is', shop_list[:])

# # Slicing on a string #
# print('characters 1 to 3 is', name[1:3])
# print('characters 2 to end is', name[2:])
# print('characters 1 to -1 is', name[1:-1])
# print('characters start to end is', name[:])

#######
# Sets
#######
# Sets are unordered collections of simple objects
# IMPORTANT: sets are "unordered", this means the way you put items in
# does not mean they will come out in the same order.
# Set syntax:
# #   set(['item', 'item', 'item'])
# groceries = set(['apples','bananas','oranges'])

# # Example 1 - test for item in set
# print("apples" in groceries)

# # Example 2 - print out set (Note the order it comes out)
# for item in groceries:
#     print(item)
    
# # Example 3 - add an item from the set
# groceries.add("pear")
# for item in groceries:
#     print(item)
    
# # Example 3 - remove an item from the set
# groceries.remove("apples")
# for item in groceries:
#     print(item)    