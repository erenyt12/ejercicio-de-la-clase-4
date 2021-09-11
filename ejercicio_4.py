"""  Ejercicio 5:
      Realizar una función asociar() que reciba como parametro dos listas 
      de la misma longitud de elementos y devuelva un diccionario de pares 
      clave-valor asociando cada elemento de ambas listas segun su indice. 

      Ej:
        empleado = ['Juli', 'Carlos', 'Roberto', 'Marta']
        categoria = ['Categoria B', 'Categoria C', 'Categoria A', 'Categoria D']

        diccionario = asociar(empleado, categoria)

        print(diccionario)

        >>> {
            'Juli': 'Categoria B', 
            'Carlos': 'Categoria C', 
            'Roberto': 'Categoria A', 
            'Marta': 'Categoria D'
          } """


empleado = ['Juli', 'Carlos', 'Roberto', 'Marta']
categoria = ['Categoria B', 'Categoria C', 'Categoria A', 'Categoria D']


def asociar(lista_1, lista_2):
    """ recibe dos listas de la misma longitud de elementos y devuelve un diccionario de pares 
    asociando cada elemento de ambas listas segun su indice """
    