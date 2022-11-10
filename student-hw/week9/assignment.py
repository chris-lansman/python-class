# What does the ‘open’ function do?
#   A: Opens a file for reading/writing
# What are the first two parameters passed to the open() function?
#   A: 1) File name, 2) file "mode"
# What does the following code do?
# fo = open("dummyFile.txt", "r")
# Do you think this code will produce an error or work?
#   A: It will work as long as the file exists and it opens it for read only
# fo = open("dummyFile.txt", "w+")
#   A: It will work as the long as the file exist and will open it for write only and create the file if it does not exist.
# print(type(fo))
# print(fo)
# Take note of the output from the two print statements. 
# What does the first tell you about fo?
#   A: Tells you it has a file handle to a textIOWrapper type.
# What does the second tell you about fo that is different than type(fo)?
#   A: It tells you the file name and its mode.
# What does the close() method do on a file object?
#   A: Closes a file handle object.
# Ex) fo.close()
# What does it mean to ‘append’ to a file?
#   A: Write to a file without deleting whatever was in there.
# What is the code to open a file in ‘append’ mode?
#   A: fo = open("filename", "a+")
# hint ‘a+’
# Run the following code and tell me the contents of dummyFile.txt after:
# fo = open("dummyFile.txt", "a+")
# for i in range(10):
#      fo.write("This is line %d\r\n" % (i+1))
#   A: 
# This is line 1

# This is line 2

# This is line 3

# This is line 4

# This is line 5

# This is line 6

# This is line 7

# This is line 8

# This is line 9

# This is line 10

#  What does the ‘r’ mode do when opening a file?
#   A: Opens a file in "read-only" mode.
