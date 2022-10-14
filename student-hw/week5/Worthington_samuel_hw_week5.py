#
#a comparison compares different values of data
#the < operator campares the value between two integers and that the (one here) is less than < (the one here)
#the equal == operator states that two things are equal
#!= means not equal
#10<30 would return nothing since there is no previous code telling tit to return something return 10<30 would return true \
#technically would return nothing but false
#true
#true
#checks if the the following statement is true
number= 23
guess= int(input('enter an integer'))
if guess == number:
    print('congrats on wasting 30 seconds of your life')
elif guess<number:
    print("your guess is too low think bigger")
else:
    print("the numbers smaller than that idiot")