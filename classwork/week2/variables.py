# Python variables
# Variables are case sensitive! my_variable is not the same as MY_Variable
# Variables can be formatted in many different ways but there are "best practices".
# Think of coding "best practices" as similar to writing an essay by hand:
    # The better your penmanship the easier it is to read and understand the words.
    # By putting indents for paragraphs you are informing readers about changes in the body of the document.
# Good coding practices makes code:
    # Eaiser to read
    # Eaiser to understand
    # Easier to maintain.

# Good programming tip: 
#   Python formatting etiquette says variables with multiple words should use underscores(_) to separate the words 
this_is_a_variable = "This is a variable which holds a 'string' type"

# However, you could also have made your variable look like this.
# This formatting sytle is also called "camel case" and is prevalent in C/C++ languages
thisIsAVariable = "This is also a variable"

is_this_a_variable = thisIsAVariable

print(is_this_a_variable)
# print(thisIsAVariable)

# These are some ILLEGAL variable names
# 2my_variable <- variables cannot start with a number
# my-var <- you cannot use dashes(-) in variable names
# my var <- you cannot use spaces( ) in variable names
