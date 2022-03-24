# ### Question 48
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
#
# Hints:
#
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.

lista = [x for x in range(1, 21)]
listaFilter = list(filter(lambda x: x % 2 == 0, lista))
print(listaFilter)
