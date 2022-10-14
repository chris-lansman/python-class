# An operator is one of the six functions used to compare values.
# A comparison operator compares two values and returns a boolean value, either true or false.
# The < operator checks to see if the left value is less than the right value.
# The == operator checks to see if the two values are exactly equal.
# The != operator checks to see if the two values are not equal.
print (10 < 30) 
# true
print (30<20)
# false
print (20<=20)
# true
print (20!=29)
# true
# The 'if' check allows a comparison operator to be used, and then as a result can runa another function such as 'print'. 

if 10 < 20:
   print("Ten is less than 20!")
else:
   print("Ten is not less than 20!")

number = 23
guess = int(input('Enter an integer : '))
 
if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here
 
print('Done')

