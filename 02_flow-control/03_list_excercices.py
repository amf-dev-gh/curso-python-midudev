
###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
print("EJERCICIO 1: MEnsaje secreto")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
print("Mensaje secreto", mensaje[7:], sep="--->")

#--------------------------------------------

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
print("EJERCICIO 2: Intercambio de posiciones")
numeros = [10, 20, 30, 40, 50]
numeros_ntercambiados = numeros[:]
numeros_ntercambiados[0] = numeros[-1]
numeros_ntercambiados[-1] = numeros[0]
print(numeros_ntercambiados)

# Forma rapida en una linea
# numeros[0], numeros[-1] = numeros[-1], numeros[0] # Intercambio en una sola línea.
# print(numeros)

#---------------------------------------------

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
print("EJERCICIO 3: El sándwich de listas")
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
# sandwich = [pan, ingredientes, pan_abajo] Esto hace una lista con listas internas
sandwich = pan + ingredientes + pan_abajo # Esto hace una lista con todos los elementos juntos
print(sandwich)

#---------------------------------------------

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lc
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print("EJERCICIO 4: Duplicando la lista")
lista = [1, 2, 3]
lista += lista
print(lista)

#---------------------------------------------

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
print("EJERCICIO 5: Extrayendo el centro")
lista = [10, 20, 30, 40, 50]
centro = len(lista) // 2
print(lista[centro])

#---------------------------------------------

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
print("EJERCICIO 6: Reversa parcial")
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida)
