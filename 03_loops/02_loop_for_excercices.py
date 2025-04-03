# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
print("Ejercicio 1: Imprimir numeros pares")
for num in range(2,21,2):
  print(num)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2: Calcular la media de una lista")
numeros = [10, 20, 30, 40, 50]
total= 0
for n in numeros:
  total += n

print(f'La media es {total/len(numeros)}')

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3: Buscar el máximo de una lista")
numeros = [15, 5, 25, 10, 20]
max = 0
for n in numeros:
  if n > max: max = n

print(f'El numero mayor es el {max}')


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4: Filtrar cadenas por longitud")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabras_largas = []
for p in palabras:
  if len(p) >= 5: palabras_largas.append(p)

print(palabras_largas)

# palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
# print(palabras_largas)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5: Contar palabras que empiezan con una letra")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce una letra: ")
contador = 0
for p in palabras:
  if p.lower().startswith(letra):
    contador += 1

print(f'Existen {contador} palabras que comienzan con {letra}')