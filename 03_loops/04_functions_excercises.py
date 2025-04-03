# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6: Tabla de multiplicar")
def obtener_tabla_multiblicar(numero):
  for m in range(1,11):
    print(f'{numero} x {m} = {numero*m}')

obtener_tabla_multiblicar(7)
obtener_tabla_multiblicar(4)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3: Factorial de un numero")
def obtener_factorial(num):
  factorial = 1
  contador = 1
  while contador <= num:
    factorial *= contador
    contador += 1
  print(f"El factorial de {num} es: {factorial}")

obtener_factorial(5)
obtener_factorial(7)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2: Imprimir números impares del 1 al 20")
def implrimir_numeros_impares(hasta, desde=0):
  """
  Recibe parametros desde hasta e imprime los numeros impares comprendidos en ese rango
  
  Si no se le pasa desde, comienza contando del 0
  """
  for n in range(desde, hasta+1):
    if n % 2 != 0:
      print(n)

implrimir_numeros_impares(20)
print('----------')
implrimir_numeros_impares(desde=9,hasta=30)
  


