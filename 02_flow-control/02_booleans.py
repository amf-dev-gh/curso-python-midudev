###
# Booleanos
# Los booleanos son un tipo de dato que solo puede tener dos valores: True o False.

print("Valores booleanos basicos")
print(True) # True es un valor booleano
print(False) # False es un valor booleano
print(type(True)) # El tipo de dato es bool
print(type(False)) # El tipo de dato es bool

#Operadores de comparacion
print("Operadores de comparacion")
print(5 > 3) # True
print(5 < 3) # False
print(5 >= 3) # True
print(5 <= 3) # False
print(5 == 3) # False
print(5 != 3) # True

print("Comparacion de cadenas")
print("Hola es igual que Hola","Hola" == "Hola") # True
# Esto comprara por letras, pero tiene en cuenta el orden alfabetico
# NO COMPARA POR LONGITUD DE CADENA
print("Manzana es mas grande que pera","Manzana" >= "Pera") # True
# Tiene en cuenta mayusculas y minusculas
print("Manzana igual que manzana","Manzana" == "manzana") # False

print("Operadores logicos")
print(True and True) # True
print(True or False) # False
print("Not True",not True) # False"

# Tablas de verdad (para referencia):
print("\nTablas de verdad:")
print("\nand:")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

print("\n or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

print("\n not:") 
print("A     not A")
print("True ", not True)
print("False", not False)

#--------------------------------------------

print("Condicion ternaria")
# Condicion ternaria: if else en una sola linea
# [codigo si es verdadero] if [condicion] else [codigo si es falso] RARO!
# En Java se hace con ? y :
edad = 17
# Se hace asi porque python es ma verboso y se entiende que primero conoce la condicion
# "Eres mayor de edad si tu edad es mayor o igual a 18, si no eres menor de edad"
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)
print("Eres mayor de edad" if edad >= 18 else "Eres menor de edad")