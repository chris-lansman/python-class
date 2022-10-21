# 2) An operator is something that mathematically compares to things.
# 3) It compares two values
# 4) It sees if said value is less than the other stated value
# 5) It compares two values and returns whether or not they are equal
# 6) It compares to values and returns whether or not they are not equal
# 7):
#   a) True
#   b) False
#   c) True
#   d) True
# 8) It checks if the thing is true, and if it is, then it does whatever is under the if statement
x = 10
y = 20
if x < y:
    print(x, "is less than", y)
else:
    print(x, "is not less than", y)
number = 23
guess = int(input('Enter an integer'))

if guess == number:
    print('''Congratulations, you guessed it.
    Unfortunately, you do not win any prizes.''')
elif guess < number:
    print("No, it's a little higher than that.")
else:
    print("No, it's a little lower than that.")

print('Done')