# ### Question 13
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

counterL = 0
counterD = 0
word = input()
for letter in word:
    if letter.isdigit():
        counterD += 1
    else:
        counterL += 1
print(f'Letters {counterL} \nDigits {counterD}')
