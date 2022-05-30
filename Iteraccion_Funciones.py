from random import shuffle
from secrets import choice

# Lista inicial
palitos = ['-', '--', '---', '----']

# mezclar palitos
def mezclar( lista ):
    shuffle(lista)
    return lista

# pedir usuario intento
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)

# comprobar el intento
def chequear_intento( lista, intento ):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te haz salvado")

    print(f"Te ha tocado {lista[intento - 1]}")

# palitos_mezclados = mezclar(palitos)
# seleccion = probar_suerte()
# chequear_intento(palitos_mezclados, seleccion)

# Practica 1
dado1 = [1,2,3,4,5,6]
dado2 = [1,2,3,4,5,6]

def lanzar_dados( dado1, dado2 ):
    shuffle(dado1)
    shuffle(dado2)
    return (choice(dado1), choice(dado2))

def evaluar_jugada( dado1, dado2 ):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buena chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    
# valor1, valor2 = lanzar_dados(dado1, dado2)
# print(valor1, valor2)
# print(evaluar_jugada(valor1, valor2))

# Practica 2
def reducir_lista( lista ):
    lista = set(lista)
    lista = list(lista)
    lista.sort()
    lista.pop(len(lista) - 1)
    return lista

lista_numeros = [1,2,15,7,2,30,15]
# print(reducir_lista(lista_numeros))

# Practica 3
def lanzar_moneda():
    moneda = ['cara', 'cruz']
    return choice(moneda)

def probar_suerte( cara_cruz, lista ):
    
    if cara_cruz == 'cara':
        
        while len(lista) - 1 >= 0:
            lista.pop(len(lista) - 1)         
        
        return f"La lista se autodestruirá: { lista }"

    else:
        return f"La lista fue salvada: {lista}"

lista_numeros = [1,2,3,4,5]
moneda = lanzar_moneda()
suerte = probar_suerte( moneda, lista_numeros)
print(moneda)
print(suerte)