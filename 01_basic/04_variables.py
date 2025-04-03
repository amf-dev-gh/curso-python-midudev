###
# Las variables sirven para guardar datos en memoria y poder usarlos después.
###

my_name="Andres"
age=32

print("Hola " + my_name + " tienes " + str(age) + " años")

age=30 #Son variables mutables, se pueden cambiar

print("Hola " + my_name + " tienes " + str(age) + " años REALMENTE")

# El tipo de dato se determina en tiempo de ejecución, no es necesario declararlo antes.
print(type(my_name))
my_name=65
print(type(my_name))

# Tipado fuerte: no se puede sumar un string con un int
# print(my_name + age) # Esto no se puede hacer, da error
my_name="Andres"

# f-strings: Formateo literal de cadenas
print(f"Hola {my_name} tienes {age+4} años")

# no recomendable forma de asignar variables
name, age2, city = "Andres", 32, "Madrid"

# convencion de nombre de variables
# snake_case: nombre_de_variable
nombre_de_mi_variables="Hola Andres"

MI_CONSTANTE = 3.11 # Constantes en mayusculas (no son realmente constantes, pero es una convención)
# camelCase: nombreDeVariable = "Hola"

# Palabras reservadas en Python:
# and, as, assert, async, await, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return

is_userlogged:bool = True # booleano, pero no inmutable. (Se puede configurar en el editor para que de avisos, pero python lo ignora)
print(type(is_userlogged))
is_userlogged = 42
print(type(is_userlogged))