import os
# Current working directory (cwd)
# This bit of snazzy code will sort out where on your computer this file is being run from
# It will save off this value and then add on one last backslash (\) so its the proper path.
# You have to "escape" a backslash as its a special character with another backslash to tell
# the interpreter you wanted just one '\'
cwd = os.path.dirname(__file__)
cwd = cwd + "\\"

# Basic file IO (input/output)
# Reading and writing from files is extremely easy in python
# NOTE: When working with files, you need to be in the directory where the file lives
#       else your program will not be able to find the file. Or will write a file somewhere
#       else that you did not expect.

# Opening a file
# Syntax:
#   file_object = open("filename", "mode")
# Where mode can be:
# r  - for reading – The file pointer is placed at the beginning of the file. This is the default mode.
# r+ - Opens a file for both reading and writing. The file pointer will be at the beginning of the file.
# w  - Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, 
#      creates a new file for writing.
# w+ - Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, 
#      it creates a new file for reading and writing.

# # Ex1) Attempt to open file and if it does not exist create it. Then write simple output to it.
# print("My current working directory is:\n", cwd)
# f = open(cwd + "ex1.txt", "w+")
# f.write("This is some simple output")
# f.close()
# # Ex2) Open a file and read out its contents
# f = open(cwd + "ex1.txt", "r")
# print(f.read())
# f.close()

# # Ex3) Incorrect mode
# # What happens if we accidentally open for "read-only" and then attempt to write to a file?
# f = open(cwd + "ex1.txt", "r")
# f.write("Some more simple output")
# f.close()
# # Ex4) Incorrect mode
# # What happens if we accidentally open for "write-only" and then attempt to read from the file?
# f = open(cwd + "ex1.txt", "w")
# contents = f.read()
# f.close()

# # Ex5) Helpful method 'readlines'
# f = open(cwd + "samplefile.txt", "r")
# f1 = f.readlines()
# print(type(f1))
# print(f1)