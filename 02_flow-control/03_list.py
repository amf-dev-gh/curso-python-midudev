###
# Secuencias mutables de elementos
# Pueden contener elementos de diferentes tipos
###

# Creacion de listas

print("Crear listas")
lista1= [1,2,3,4,5] # lista de enteros
lista2= ["Hola", "Adios", "Python"] # lista de strings
lista3= [1, "Hola", 3.14, True] # lista de diferentes tipos
lista4= [] # lista vacia
matrix= [[1,2,3], [4,5,6], [7,8,9]] # lista de listas (matriz)

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(matrix)

# Acceder a elementos por su indice
print("Acceder a elementos por su indice")
print(lista1[0]) # 1
print(lista2[1]) # Adios
print(lista2[-1]) # Python (ultimo elemento) si es con valores negativos empieza desde el final
print(matrix[1][1])

# Slicing (rebanado) de listas
print("Slicing (rebanado) de listas")
lista1= [1,2,3,4,5]
print("Quiero solo los numeros del medio", lista1[1:4]) # [2,3,4] (desde el inicio del valor1 hasta el principio del indice 4, sin incluirlo)
print("Quiero los 3 primeros numeros", lista1[:3])
print("Quiero una copia de la lista", lista1[:]) # copia de la lista

# Revertrir una lista
print("Revertir una lista")
lista1= [1,2,3,4,5,6,7,8,9,10]
#print(lista1[desde:hasta:paso]) # el paso es opcional, si no se pone es 1 pero significa que se va de uno en uno
print(lista1[::2]) # [1,3,5,7,9] (de 2 en 2)
print("Lista revertida", lista1[::-1])

# Modificar una lista
print("Modificar una lista")
lista1= [1,2,3,4,5]
lista1[0]=10 # Cambia el primer elemento por 10
print(lista1[0])

# Añadir elementos a una lista
print("Añadir elementos a una lista")
lista1= [1,2,3,4,5]
lista1 = lista1 + [6, 7, 8]
print(lista1)

# Mas eficiente
lista1= [1,2,3,4,5]
lista1 += [66, 77, 88]
print(lista1)

# Recuperar la longitud de la lista
lista1= [1,2,3,4,5, 6, 7]
print(len(lista1))