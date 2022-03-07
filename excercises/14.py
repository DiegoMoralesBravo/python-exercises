# ### Question 14
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

counterL = 0
counterD = 0
word = input()
for letter in word:
    if letter.isupper():
        counterD += 1
    else:
        counterL += 1
print(f'Lower {counterL} \nUpper {counterD}')
