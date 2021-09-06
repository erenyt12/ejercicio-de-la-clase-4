""" => Ejercicio 1:
    Realiza una función separar(lista) que tome una lista de números enteros 
    y devuelva dos listas la primera con los números pares 
    y la segunda con los números impares.

    Ej:
        pares, impares = separar([6,5,2,1,7])
        print(pares)
        print(impares)

        >>> [2, 6]
        >>> [1, 5, 7] """


numeros = [6,5,2,1,7, 0]



def separar(una_lista: list[int]) -> tuple[list[int], list[int]]:
    """ Toma como parametro una coleccion de numeros y los separa en dos listas(pares e impares) 
    y retorna ambas colecciones"""
    pares = list(filter(lambda x: x % 2 == 0 and x != 0, numeros ))
    impares = list(filter(lambda x : x % 2 != 0 or x == 0, numeros))

    return (pares, impares)


pares, impares = separar(numeros)
print(pares)
print(impares)
 