""" Ejercicio 2:
    Realiza una función que tome como parametro una frase y devuelva una 
    lista de palabras en mayuscula. 

      Ej: 
        mi_frase = "Este sabado tenemos el ultimo encuentro online"

        palabras = convertir(mi_frase)

        print(palabras)

        >>> ["ESTE", "SABADO", "TENEMOS", "EL", "ULTIMO", "ENCUENTRO", "ONLINE"]
 """

mi_frase = "Este sabado tenemos el ultimo encuentro online"

# nueva_frase = mi_frase.upper().split(" ")

# print(nueva_frase)

def mayuscula(a: str): 
    return a.upper()
    




def convertir(frase: str):
    frase_convertida = frase.split(" ")
    # return list(map(str.upper, frase_convertida))
    #f = list(map(lambda palabra : palabra.upper(), frase_convertida))
    f = list(map(mayuscula,  frase_convertida))
    return f  


     

palabras = convertir(mi_frase)
print(palabras)
