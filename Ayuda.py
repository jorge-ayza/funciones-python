dic = {'clave1':100, 'Clave':500}

a = dic.popitem()

print(a)
print(dic)

# Practica 1
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
limpio = texto.lstrip(',:_#')

print(limpio)

# Practica 2
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(4, "naranja")

print(frutas)

# Practica 3
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

cojuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(cojuntos_aislados)

# Practica 4
