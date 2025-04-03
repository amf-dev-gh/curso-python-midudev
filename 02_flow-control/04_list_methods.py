from os import system
if system("clear") != 0: system("cls")

lista = [10, 20, 30, 40, 50]

# Metodo para agregar un alemento a la lista
lista.append(60) # Añade un elemento al final
print(lista)

lista.insert(1, 100) # Aññade un elemento en la posicion que le pasemos como primer parametro. El segundo paramentro es el elemento a a agregar (solo acepta 1 elemento)
print(lista)

lista.extend([200, '🤞', 800, '🤞']) # Este metodo agrega tantos parametros como querramos al final de la lista. Similar a la concatenacion, porque acepta otra lista como parametro
print(lista)

# Eliminar elementos de la lista
lista.remove('🤞') # Elimina el elemento pasado por parametro. Pero solo la primera coincidencia, es decir, si hay 3 elementos iguales solo elimina el primero que encuentra, NO SE PASA EL INDICE. SE PASA EL ELEMENTO
print(lista)

elemento = lista.pop() # Elimina el ultimo elemento de la lista, y ademas lo devuelve
print("Elemento eliminado", elemento)
print(lista)

lista.pop(1) # Elimina el indice pasado por parámetro
print(lista)

del lista[-1] # Esto tambien elimina elemento ubicado en el indice pasado, Acepta negativos para leer la lista a la inversa
print(lista)

lista_ = ['💀','😒','💕','🚓']
del lista_[1:3] # Puede eliminar un rando de elementos (lo interesante)
print(lista_)

lista.clear() # Elimina TODOS los elementos de la lista
print(lista)

# MEtodos para ordenar listas modificandolas
# En caso de numeros los ordena de menor a mayor
numeros= [100, 544, 26 , 66, 44]
numeros.sort() # Este metodo la modifica, pero no devuelve o crea una nueva lista
print(numeros)

# Ordenar listas creando una nueva
numeros= [100, 544, 26 , 66, 44]
numeros_ordenados = sorted(numeros)
print('Nueva lista ordenada', numeros_ordenados)

# Ordenar una lista de cadenas de texto
print('Ordenando cadenas de texto todas minusculas')
frutas = ['pera', 'banana', 'Manzana', 'Kiwi']
frutas_ordenadas = sorted(frutas) # Ordena de menor a mayor, en este caso ordena alfabeticamente, si todas son minusculas.
print(frutas_ordenadas)

print('Ordenando cadenas de texto minusculas y mayusculas mezcladas')
frutas = ['pera', 'banana', 'Manzana', 'Kiwi', 'Durazno', 'aguacate']
frutas.sort(key=str.lower) # Se pasa por parametro la key, que corresponde a la forma de ordenar la lista. En este caso se pasa la funcion str.lower, que convierte todo a minusculas. Si no se pasa nada, lo ordena por el primer caracter de cada cadena.
print(frutas)

# Mas metodos utiles
animals = ['🐩', '🐈', '🐄', '🐩', '🐊']
print(len(animals)) # Devolvemos la longitud de la lista, es decir, la cantidad de elementos que tiene

print(animals.count('🐩')) # Devuelve la cantidad de veces que se repite el elemento pasado por parametro

print('🐈' in animals)
print('🐀' in animals)