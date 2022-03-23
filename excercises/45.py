# ### Question 45
# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
#
# Hints:
#
# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.

def funcion(x):
    if x % 2 == 0:
        return True
    else:
        return False


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaFiltro = list(filter(funcion, lista))

print(listaFiltro)
