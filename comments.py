
# Comments 
# There are two types of comments:
# 1) Single-Line Comments
# 2) Multi-Line Comments

# 1) Single-Line Comment : 
# ****  Single Line comments use "#" symbol

# 2) DocStrings (used as Multi-Line Comments)
# These are not technically comments but docstrings are used as multi line comments
# if they are not assigned to a variable 
# **** Doc-String use triple single or double quotes ***
# Eg:
""" 
This is a
multi-line 
comment"""

'''
Note 1: These triple quotes acts as documentation inside a function.

Eg: def greet():
    """This function prints a greeting message."""
    print("Hello!")
'''

''' 
Note2: DocStrings in functions helps to describe the function more efficiently.

Docstring: A string immediately after a function definition, used to describe the function
Access via:	Function_name.__doc__ or help(function_name)
Preferred syntax: Triple double-quotes """ ... """
Format: Short description + parameters + return + optional notes
'''
