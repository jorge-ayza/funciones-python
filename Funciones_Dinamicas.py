

def chequear_3_cifras( lista ):
    lista_3_cifras = []
    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)
        else:
            pass
    
    return lista_3_cifras

resultado = chequear_3_cifras([555, 99, 600])
# print(resultado)

# Practica 1
def todos_positivos( lista ):
    positivo = []
    for n in lista:
        if n > 0:
            positivo.append(n)
        else:
            return False
    
    if len(positivo) == len(lista):
        return True

lista_numeros = [1000,2,3,4,-999999]
resultado = todos_positivos(lista_numeros)
# print(resultado)

# Practica 2
def suma_menores( lista ):
    suma = 0
    for n in lista:
        if n in range(0, 1001):
            suma += n
        else:
            pass

    return suma

lista = [1,2,3,5000]
respuesta = suma_menores(lista)
# print(respuesta)

# Practica 3
def cantidad_pares( lista ):
    numeros_pares = []
    for n in lista:
        if n % 2 == 0:
            numeros_pares.append(n)
        else:
            pass
    suma_pares = 0
    for num in numeros_pares:
        suma_pares += num

    return suma_pares

lista1 = [2,1,2,3,4,-5,6]
respuesta1 = cantidad_pares(lista1)
print(respuesta1)