def multiplicar( numero1, numero2 ):
    return numero1 * numero2

resultado = multiplicar( 5, 10 )
print(resultado)

# Practica 1
def potencia( base, exponente ):
    return base**exponente

resultado = potencia(10, 2)
print(resultado)

# Practica 2
dolares = 50
def usd_a_eur( monto ):
    return monto * 0.85

euros = usd_a_eur(dolares)
print(f"El cambio de {dolares}$ dolares a euros es {euros}€")

# Practica 3
palabra = "jorge ayza"
def invertir_palabra( palabra ):
    palabra_invertida = ""

    for letra in palabra:
        palabra_invertida = letra + palabra_invertida

    return palabra_invertida.upper()

print(invertir_palabra(palabra))

