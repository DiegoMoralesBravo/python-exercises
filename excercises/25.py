# ### Question 25
# Level 1
#
# Question:
# Define a class, which have a class parameter and have a same instance parameter.
#
# Hints:
# Define a instance parameter, need add it in __init__ method
# You can init a object with construct parameter or set the value later

class Objeto():
    def __init__(self, parametro):
        self.parametro = parametro

    def imprimir(self):
        print(self.parametro)


valor = Objeto('hola')
valor.imprimir()
