def prueba(num1, num2, *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [100, 200, 300, 400]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}

prueba(15, 50, *args, **kwargs)

# Practica 1
def cantidad_atributos( **kwargs ):
    return f"El numero de parametros es {len(kwargs)}"

print(cantidad_atributos(x=1, y=2, z=3, u=4))

# Practica 2
def lista_atributos( **kwargs ):
    lista_valores = []

    for valor in kwargs.values():
        lista_valores.append(valor)

    return lista_valores

print(lista_atributos(x='uno', y='dos', z=3, u='cuatro'))

# Practica 3
def describir_persona( nombre, **kwargs ):
    print(f"Caracteristicas de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"\t{clave} : {valor}")

rasgos = {'color de ojos': 'cafes', 'color de cabello': 'negro', 'piel':'morena'}

describir_persona('Jorge', **rasgos)