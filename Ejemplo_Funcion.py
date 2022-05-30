precios_cafe = [('capuchino',1.5), ('Expresso', 2.2), ('Moka', 1.9)]

def cafe_mas_caro( lista ):

    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe, precio in lista:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro, precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"EL cafe mas caro es {cafe} cuyo precio es {precio}")