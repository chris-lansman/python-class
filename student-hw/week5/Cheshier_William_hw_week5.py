#An operator is a mathematical symbol that compares two different numbers

#4: The < operator see if the number to the left is less than the number to the right.
#5: The == operator sees if the number to the left is equal to the number to the right.
#6: The != operator see if the number to the left is not equal to the number to the right.

#7: 10 < 30--True
# 30 < 20--False
# 20 <= 20--True
# 20 != 29--True

#8: The if check makes sure that something is true or false, and based on that answer, it may or may not continue the code.
#9:
# if 10 < 20:
#    print("Ten is less than 20!")
# else:
#    print("Ten is not less than 20!")--Returns "10 is less than 20!"

number = 9876543210
guess = int(input('Enter an integer : '))
 
if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes because it took you so long!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here
 
print('Done')
# This last statement is always executed,
# after the if statement is executed.
