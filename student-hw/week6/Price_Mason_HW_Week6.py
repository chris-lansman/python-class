# 3) If the if statement is not true, then the program moves on to the else statement
# 4) It helps shorten the code and make it simpler
# 5) Creates a loop
# 6) It prints 'C'
number = 22
if number > 22:
    print('A')
elif number == 23:
    print('B')
elif number >= 22:
    print('C')
# 7) It will loop 10 times
loops = 20
number_loops = 1
while loops != 0:
    if loops % 2 == 0:
        loops = loops - 2
    print(number_loops)
    number_loops += 1
# 8) It keeps the program in a loop
# 9)1
#   2
#   3
#   4
#   The for loop is over
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')
# 10) It makes a loop with a range
# 11) It sets a range for the 'for...in' statement
# 12) It breaks a loop
# 13) It starts the loop over
# 14) 11 times
for i in range(1, 100):
    print(i)
    if i > 10:
        break