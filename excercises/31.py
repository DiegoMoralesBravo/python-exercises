# ### Question 31
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
#
# Hints:
#
# Use len() function to get the length of a string

def funcion(x, y):
    if len(x) > len(y):
        print(x)
    elif len(x) < len(y):
        print(y)
    elif len(x) == len(y):
        print(x)
        print(y)


x, y = input().split(' ')
funcion(x, y)
