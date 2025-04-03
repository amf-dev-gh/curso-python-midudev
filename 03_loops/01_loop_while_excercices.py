
# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1: Cuenta atras")
contador = 10
while contador >= 1:
  print(contador)
  contador -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2: Suma de enteros pares del 1 al 20")
contador = 1
resultado = 0;
while contador <= 20:
  if contador % 2 == 0:
    resultado += contador
  contador +=1
print(resultado)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3: Factorial de un numero")
numero = int(input("Introduce un número entero positivo: "))
factorial = 1
contador = 1

while contador <= numero:
  factorial *= contador
  contador += 1

print(f"El factorial de {numero} es: {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4: Validacion de contraseña")
while True:
  password = input("Ingresa una contraseña de 8 caracteres: ")
  if len(password) == 8:
    print('Contraseña correcta!')
    break


# Ejercicio 5: Tabla de multiplicar8
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5: Tabla de multiplicar")
numero = int(input("Introduce un número entero positivo: "))
factor = 1
while factor <= 10:
  print(f'{numero} x {factor} = {numero*factor}')
  factor += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6: Números primos hasta")
n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1
  if es_primo:
    print(numero)

  numero += 1