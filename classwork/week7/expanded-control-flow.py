#####################################################################
# Expanding the 'if' statement to consider multiple boolean values
#####################################################################
# and logic:
#   Only evaluates to True if every boolean expression being evaluated 
#   evaluates to True.
# or logic:
#   Evaluates to True if one of the boolean expressions being evaluated
#   evaluates to True.

# Example 1
# if True and True and False:
#     print("True!~")
# else:
#     print("Almost true!")

# Example 2 - 'and' statements
num = 10
den = 20
# if ((num >= 10) and (den <= 40)):
#     print(f"area of the rectangle is {(num*den)}")
    
# # Example 3 - 'or' statements
# if (den/num > 0) or (num == 10):
#     print(f"area of the rectangle is {(num*den)}")

# # Example 4 - Tricky parentheses 
# if (num >= 10) and ((den <= 10) or (num == 10)):
#     print("Think we hit this tricky print?")
# else:
#     print("We did not hit the tricky print")

# # Example 5 - LOTS of and/or's    
# if ((num <= 11) and True and (den >= 15) and ((den/num) > 0)) or (num == 10) or ((den >= 15) and ((den/num) > 0)):
#     print("Whew! That is a lot of ands and ors!")
# else:
#     print("We confused ourselves.... ")
    
# # Example 6 - 'and' in 'while'
# while True and not False:
#     print("We made it!")
#     break;

# # Example 6 - 'and' in 'while'
# while (num < den) and (num != den):
#     print(f"num:{num}")
#     num += 1

# # Example 7 - 'or' in 'while'
# while True or False:
#     print("We made it!")
#     break;

# Example 8 - 'or' in 'while'
# while (num >= 0) or ((den/num) >= 0):
#     print(f"num:{num}")
#     num -= 1

