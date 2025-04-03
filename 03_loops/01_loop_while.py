###
# Los loops sierven para repetir un bloque de código mientras una condición sea verdadera.(Automatizar tareas repetitivas)
###

from os import system
if system("clear") != 0: system("cls")

print("Bucle WHILE")
contador= 0
while contador <= 5:
  print(contador)
  contador += 1

print("Bucle WHILE con break")
contador= 0
while True:
  print(contador)
  contador += 1
  if contador == 5:
    print("Fin del bucle")
    break # Como en java, corta el bucle

# Con continue se salta la iteración actual y se pasa a la siguiente
print("Bucles con continue")
contador= 0
while contador < 10:
  contador += 1

  if contador % 2 == 0:
    continue # Si la condicion se cumple saltea la iteración actual y continua con la siguiente. Noimporta el codigo que siga. Se saltea y vuelve a ejecutar el siguiente bucle

print(contador)

# Existe el else en los bucles, se ejecuta cuando el bucle termina normalmente (sin break)
print("Bucle WHILE con else")
contador= 0
while contador < 5:
  contador += 1
  print(contador)
else:
  print("Fin del bucle")

# Pedir un numero al ususario que sea positivo si no lo es, volver a pedirlo
# while True:
#   numero = int(input("Introduce un numero positivo: "))
#   if numero > 0:
#     print(f'El numero {numero} es positivo')
#     break
#   else:
#     print(f'El numero {numero} NO ES positivo')

# PRevenir error con try except, En Java try catch
numero = -1
while numero <= 0:
  try:
    numero = int(input("Introduce un numero positivo: "))
    if numero < 0:
      print("El numero NO es positivo, Intenta de nuevo")
  except:
    print("Lo que introduces debe ser un numero")

print(f'El numero introducido es: {numero}')