###
# Range Function
# permite crear una secuencia de números enteros
# No crea un objeto en memoria, sino que crea un objeto iterable sobre la marcha
###

print("range()")
nums = range(10)  # NO CREA UNA LISTA
print(type(nums))
# Crea una secuencia de numeros pero no una llista
print(nums)

# Imprime los numero de 0 a 9
print("Range con 1 parametro")
for num in nums:
  print(num)

# Se le pueden pasar parametros. El primero es desde donde empieza y el segundo hasta donde termina
# El tercer parametro es el incremento
# si solo se pasa uno, empieza desde 0 y termina en el numero pasado y va de 1 en 1
print("Range con 2 parametros")
for num in range(5,10):
  print(num);

# Si se le pasa el tercer parametro, se puede cambiar el incremento
print("Range con 3 parametros")
for num in range(0,100,5):
  print(num);

print("Range con cuenta regresiva")
# Si se le pasa el tercer parametro negativo, se puede hacer una cuenta regresiva
for num in range(10,0,-1):
  print(num);

# Crear una lista a partir de un range()
nums = range(10);
list_nums = list(nums)  # Crea una lista a partir de un range
print(nums)
print(list_nums)

# Una convencion para declarar una variable que no se usa
# Entonces e este caso ejecuta 10 veces una acción sin usar la variable
for _ in range(10):
  print("Hola")