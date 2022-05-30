def suma(*args):
    return sum(args)

print(suma(5,6,10,50))

# Practica 1
def suma_cuadrados( *args ):
    cuadrados = []
    for arg in args:
        cuadrados.append(arg**2)

    return sum(cuadrados)

print(suma_cuadrados(2,3,4,5))

# Practica 2
def suma_absolutos( *args ):
    numeros_absolutos = []
    for arg in args:
        if arg < 0:
            numeros_absolutos.append(-arg)
        else:
            numeros_absolutos.append(arg)
    
    return sum(numeros_absolutos)

print(suma_absolutos(-10, 1, -20, 3))

# Practica 3
def numeros_persona( nombre, *args ):
    return f"{nombre}, la suma de tus números es {sum(args)}"

print(numeros_persona('Jorge', 1,2,3,4,5,6))