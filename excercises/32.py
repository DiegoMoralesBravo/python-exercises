# ### Question 32
# Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
#
# Hints:
#
# Use % operator to check if a number is even or odd.

def funcion(x):
    msn = ''
    if x % 2 == 0:
        msn = 'Its an even number'
    else:
        msn = 'Its an odd number'
    return msn


print(funcion(2))
