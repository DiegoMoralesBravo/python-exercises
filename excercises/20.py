# ### Question 20
# Level 3
#
# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
#
# Hints:
# Consider use yield
def function(n):
    for x in range(n):
        yield x


x = function(10)
for valor in x:
    print(valor)
