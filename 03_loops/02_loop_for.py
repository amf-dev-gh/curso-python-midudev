###
# Bucle for
# El bucle for se utiliza para iterar sobre una secuencia (lista, tupla, diccionario, conjunto o cadena).
###

print("Bucle for")
# Iterar listas
frutas = ["manzana", "banana", "cereza", 'mandarina', 'kiwi']
for fruta in frutas:
    print(fruta)

# Iterar ITERABLES, strings
nombre = "Andrés"
for char in nombre:
    print(char)

# Enumerate
# Enumerate devuelve un objeto iterable que contiene pares de índice y valor.
frutas = ["manzana", "banana", "cereza", 'mandarina', 'kiwi']
for index, fruta in enumerate(frutas):
    print(f"En el indice {index} la fruta es: {fruta}")

# Bucles anidados
# Un bucle dentro de otro bucle.
lestras = ["A", "B", "C"]
numeros = [1, 2, 3]
for letra in lestras:
    for numero in numeros:
        print(f"{letra}{numero}")

# Comprensión de listas (list comprehension)
# Una forma concisa de crear nuevas listas.
animales = ["perro", "gato", "pájaro", "pez", "conejo", "torutga"]
animales_mayus = [animal.upper() for animal in animales] # Hacer X cosa para cada elemento x de la lista
print(animales_mayus)

# Muestra los números pares de una lista
pares =[n for n in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]if n % 2 == 0] # Compresion de listas con un condicional
print(pares)

