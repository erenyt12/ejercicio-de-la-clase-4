# imprimir = lambda x: print(x)
# imprimir(2)

# def imprimirDos(x):
#     print(x)

# imprimirDos(2)


numeros = [1, 9, 8, 5]


def devolver(num):
    for i in num :
        yield i


a = list(devolver(numeros))
print(a)



