import random
# Control flow is required to add "smarts" to your programs.
# Control flow allows you shape the execution of your programs.

# Expanding the basic 'if' with 'else'

# if False:
#     print("This was false!")
# else:
#     print("This was true!")
    
# # Adding more logical possibilities
# bill_total = 39.54
# if bill_total < 20:
#     print("This was a small bill")
# elif bill_total < 30:
#     print("This was a medium bill")
# else:
#     print("Woah! this was a large bill!")
    

# # Repeating a control loop with the 'while' statement
# # CAUTION: If you do not have a way for the loop to "exit"
# # your program will be stuck in an infinite loop. 
# repeat_loop = True
# loop_count = 1
# while repeat_loop:
#     if loop_count < 10:
#         print(f"looping {loop_count} number of times")
#         loop_count += 1
#     else:
#         repeat_loop = False
# else:
#     print("The loop ended!")

# Example of a forever loop and how to get out of it
# while True:
#     print("looping")

# ###############################################
# # Lets upgrade our simple guessing game's game
# ###############################################
# # Lets make our target number a little more interesting 
# # by using the random class. 
# number = random.randrange(0,100)
# number_guessed = False
# print ("Guess a number between 1-100")
# while not number_guessed:
#     guess = int(input('Enter an integer : '))

#     if guess == number:
#         # New block starts here
#         print('Congratulations, you guessed it.')
#         number_guessed = True
#         # New block ends here
#     elif guess < number:
#         # Another block
#         print('No, it is a little higher than that')
#         # You can do whatever you want in a block ...
#     else:
#         print('No, it is a little lower than that')
#         # you must have guessed > number to reach here
# else: #This else is optional
#     print("Guessing game finished.")

# The "For" Loop
# For loops are used to iterate over some finite number of objects
# A for loop goes in a logical sequence (i.e. 1,2,3,4,5....)
# Simple for loop
# for val in range(1,10): #Note: The loop exits before the 10th run (i.e. (1,9])
#     print(val)
# else: #optional
#     print("The loop exited")

# Ranged iterations perform a '<' "Less than" check at the bottom of the loop before 
# looping back around. So we say a loop includes the lowest value but only extends
# up to (but not including) the last value.

# # Another way to exit loops
# while True:
#     num = input('Enter a value : ')
#     if num.isdigit():
#         print("Yey! you gave me a number")
#     else:
#         print("Boo! You did not give me a number")
#         print('****Loop terminated due to bad input***')
#         break

# The 'continue' statement
# Allows a loop to "skip" this iteration of the loop and continue back to the top
# while True:
#     print("         ****Top of the loop****")
#     num = input('Enter a value : ')
#     if num.isdigit():
#         print("Yey! you gave me a number")
#         if int(num) < 10:
#             continue
#     else:
#         print("Boo! You did not give me a number")
#         print('****Loop terminated due to bad input***')
#         break
#     print("         ****Bottom of the loop****")
