###########################################
# Week 3 Questions and Answers
###########################################

# 1) Create a simple python program that:
# Asks for a person’s name (hint: input)
name = input("What is your name?")
# Asks for a person’s age (hint: input)
age = input("What is your age?")
# Outputs the person’s age and name to the screen.(hint: print)
print("Your name is: " + name)
print("your age is: " + age)
# We have not covered this type of "formatted" output yet but we will in class. This is another way to print variables
print(f"Your name is {name}, and you are {age} years old")

# Extra-credit
# Copy the following code into your program in step 4 to determine how many days has passed in years based on their age:
print(str((365*int(age))) + " days have passed since the year you were born")

# Solve the following mathematical equations using python:
print(99566 + 2321)
print(3567 * 3333)
print(3445 / 1111)
print(22 % 2)
# What type of “operator” is ‘%’
# A: Modulo
print(3 | 5 )
# What type of operator is ‘|’?
# A: OR
# What do you think the following snippets of code evaluate to?
print(3 + 5)
print(3 + (1 + 5))
print(25 / 5)
print(25 / (3 + 2))
print((2 + (3 * 4)))
print((2 +3) * 4)
# Run the python program below that takes the length and width from the user and then prints the output to the console.
print("The area of the rectangle is " + str((int(input("enter width ")) * int(input("enter length ")))))
# Pay attention to the order of operations which is being controlled by the parentheses ‘(‘ ‘)’ 
# What would happen if we accidentally left one out?
# Try to run the following code
# print("The area of a rectangle is " + str(int(input("enter width ")) * int(input("enter length ")))))
