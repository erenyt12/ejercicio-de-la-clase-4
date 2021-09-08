
from functools import reduce
""" Ejercicio 3:
    Realiza una fn aculado, que devuelva el valor acumulado 
    de la suma de una lista de numeros mas 100.

    Ej: 
      mis_numeros = [2, 4, 6]

      valor_final = acumulado(mis_numeros)

      print(mis_numeros) """


# Lista de numeros
Numeros = [2, 4, 6, 7, 9]

# Funcion 
def acumulando(list: list[int]) -> int:
    """ recupera los valores de una lista y los suma, al resultado se le suma 100  """
    resultado = reduce(lambda x, y: x + y, list, 100)
    print(resultado)

# Utilizacion de la fn 
acumulando(Numeros)




# Funcion sin importar reduce
def sum(num: list[int]) -> int:
    """ toma los valores de una lista y los suma, al resultado se le suma el valor " 100" """
    resultado = sum(num, 100)
    print(resultado)


# Utilizacion de la fn 
# sum(Numeros)


