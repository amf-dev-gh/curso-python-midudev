###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("EJERCICIO 1 - Determinar el mayor numero de dos")
num1, num2 = input("Ingresa dos numeros separados para saber si son iguales o cual es mayor\n").split()
if int(num1) == int(num2):
  print(f"Los numeros {num1} y {num2} son iguales")
elif num1 > num2:
  print(f"El numero {num1} es mayor que {num2}")
else:
  print(f"El numero {num2} es mayor que {num1}")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("EJERCICIO 2: Calculadora simple")
num1, num2, calculo = input("Ingresa dos numeros por separado y luego ingresa +, -, *, / para indicar la operación\n").split()
if calculo == "-":
  print(f"El resultado de la resta es: ", int(num1)-int(num2))
elif calculo == "+":
  print(f"El resultado de la suma es: ", int(num1)+int(num2))
elif calculo == "*":
  print(f"El resultado de la multiplicación es: ", int(num1)*int(num2))
elif calculo == "/":
  if int(num2):
    print(f"El resultado de la division es: ", int(num1)/int(num2))
  else:
    print("No se puede divivir por 0")
else:
  print("ERROR: Operación no válida")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("EJERCICIO 3: Determina si el año ingresado es bisiesto")
anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("EJERCICIO : Categorizando edades")
edad = input("Ingresa una edad: ")
respuesta = "Segun la tabla es un: "

if int(edad) <= 2:
  respuesta += "Bebé"
elif int(edad) <= 12:
  respuesta += "Niño"
elif int(edad) <= 17:
  respuesta += "Adolescente"
elif int(edad) <= 64:
  respuesta += "Adulto"
else:
  respuesta += "Adulto mayor"

print(respuesta)