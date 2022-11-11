# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object builder, or a "blueprint" for creating objects.
# A term commonly used when a class 'object' is created is "constructed"
# Creating an instance of an object is like building a house.

# Class syntax:
#   define a class by starting with the keyword "class"
#Ex1 Create our first class
# class myFirstClass:
#     print("This is my first class!")

# # This constructs an instance of our class and destructs it
# myFirstClass()

#Ex2 - Create a class object instance
# class mySecondClass:
#     print("my second class!")

# myClass = mySecondClass()
# print(type(myClass))

#Ex3 - Class can have "member" variables
# Remember the "scope" idea from last week? A member variable is a 
# variable that is only valid in the context of the class.
# class myThirdClass:
#     myMemberVariable = "this is mine!"
    
# myClass = myThirdClass()
# print(myClass.myMemberVariable)
# # print(myMemberVariable)

# The above are all vary basic classes and not very useful in real life. 
# To really build a meaningful class we need to learn about the "__init__" function.
# The __init__ function is the first thing that is called when a class object is being "constructed"
# Its very important because we will use it to "initialize" (setup) the class into an initial state. 
# We will also use it to allow users of our class to enter values into the class object that gets created(more on this later)
#Ex4 Create a class with an __init__ call
# class myInitClass:
#     def __init__(self):
#         self.name = "chris"
#     def printMyName(self):
#         print(self.name)

# # Create a new instance of a 'myInitClass' class object
# myInit = myInitClass()
# # Now that we have a new instance, lets called the method(function) of that class to print some information
# myInit.printMyName()
# # This looks funny but works because in python all classes' functions first parameter is an 'instance' of a class.
# # This type of syntax while valid is never used.
# myInitClass.printMyName(myInit)

# I had said there were only two scopes in python. This was not 100% true (sort of...). 
# # Classes add an additional nuanced layer to the "locally scoped" variable concept.
# Classes can have two different types of variables:
#   1) Class instance variables
#       This is a variable who's scope is only valid if an instance of the class has been created
#   2) Static variables
#       This is a variable who's scope is valid even if we have not created an instance of a class yet.
#
#   In either case, this is critical to wrap your head around: 
#       Class member variables are not accessible by anything outside of the class.
#       WHY? Because they dont exist outside the class.

#Ex4 Create a class who has a static member variable and an instance member variable
# Syntax for creating a class-only member variable: 
# keyword: self
# class myMemberVariableClass:
#     staticVariable = 10
#     def __init__(self):
#         self.instanceVariable = "chris"

# # I have not yet created an instance of a class. 
# # Can I print 'staticVariable'?
# print(myMemberVariableClass.staticVariable)
# # Create an instance of our class
# myMember = myMemberVariableClass()
# # Can I print this instance member variable?
# print(myMember.instanceVariable)


# ? Is there such a thing as a static class method?
# YES! 
# Like static class variables which do not require an instance of a class to use
# We can define static class functions which can be called without an instance of a class.
# Syntax to create a static function
# @staticmethod
# This syntax looks funny but is called a 'decorator' in python and it tells the interpreter
# we are defining a static method
# Note: You do not HAVE to add the @staticmethod, this is 'good programming style', 
# all you really have todo in order to create a static method is omit the 'self' parameter to the method.
# class myStaticMethodClass:
#     @staticmethod
#     def staticMethodPrint():
#         print("This is a static method!")
#     def nonStaticMethodPrint(self):
#         print("This is NOT a static method")
# myStaticMethodClass.staticMethodPrint()
# myStaticMethodClass.nonStaticMethodPrint()

# Public/Private
# Most programming languages have the concept of public methods/variables and private methods/variables.
# The basic idea behind these terms is:
#   When you want users of your class to "see" variables and "use" functions you make them 'public'
#   When you dont want users of your class to "see" variables or "use" functions in your class you make them 'private'
# ?? Why would anyone want to do something like this??
# Real-world example from a previous lesson
# I want to create a user class that represents a user of my system
#    I need them to login to the system.
#       In order to login they need to type a password (public method)
#       The password needs to be encrypted and checked against a database (private method)
#           Q: Why is this one private? 
#           A: Because, we dont need a user of our class to know we have an encrypt method or how it works
#              they just need the ability to offer a login prompt and then the rest is "magically" handled behind the scenes. 
# Syntax to define a variable or method as 'private'
#   '__'
# ex) __myPrivateVariable

# Ex5 Defining public/private variables
# class myPublicPrivateClass:
#     # Static public variable
#     staticPublicVar = 9
#     # Static private variable
#     __staticPrivateVar = 3
# # Attempt to print the public static variable
# print(myPublicPrivateClass.staticPublicVar)
# # Attempt to print the private static variable
# print(myPublicPrivateClass.__staticPrivateVar)

#Ex6 Defining public/private class methods
# class myPublicPrivateClass:
#     def __init__(self):
#         None
#     def myPublicFunction(self):
#         print("This is a public function!")
#     def __myPrivateFunction(self):
#         print("This is a private function!")
#     def myPrivateFunctionCaller(self):
#         self.__myPrivateFunction()

# # Create an instance of our class
# myClassInstance = myPublicPrivateClass()
# # Lets call the public function
# myClassInstance.myPublicFunction()
# # Lets try and call the private function
# myClassInstance.__myPrivateFunction()
# # Lets call our helper function
# myClassInstance.myPrivateFunctionCaller()

