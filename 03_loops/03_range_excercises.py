###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1: Imprimir números del 1 al 10")
for n in range(1,11):
  print(n)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2: Imprimir números impares del 1 al 20")
for n in range(1, 21, 2):
  print(n)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3: Imprimir múltiplos de 5")
for n in range(5, 51, 5):
  print(n)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4: Imprimir números en orden inverso")
for n in range(10, 0, -1):
  print(n)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5: Suma de números en un rango")
total = 0;
for n in range(1,101):
  total += n
print("La suma total es: ", total)

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6: Tabla de multiplicar")
numero_ingresado = int(input("Ingresa un numero: "))
for m in range(1,11):
  print(f'{numero_ingresado} x {m} = {numero_ingresado*m}')

print("\nEjercicio EXTRA: todas las tablas")
contador = 1
while contador <= 10:
  print('Tabla del ', contador)
  for factor in range(1,11):
    print(f'{contador} X {factor} =  {contador*factor}')
  contador +=1
  print('\n')