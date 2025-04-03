###
#Bloque de codigo reutilizable y parametrizable para ejecutar tareas especificas
###

""" Definicion de una funcion

def nombre_de_la_funcion(paratemtro1, parametro2, ...):
  docstring
  cuerpo de la funcion
  return valor_de_retorno #Opcional

"""

#Ejemplo de una funcion
def saludar():
  print("HOLA MUNDO!")

saludar()


# Eemplo de una funcion con parametros
def saludarA(nombre):
  print("Hola " + nombre + "!")

saludarA("Juan")
saludarA("Andres")
saludarA("Carmen")

# Funciones con varios parametros
def sumar(a, b):
  return a + b

print(sumar(5, 10))

# Documentar dunciones con docstring
def restar(a, b):
  """Resta dos numeros enteros y devuelve el resultado"""
  return a - b

print(restar(10, 5))
help(restar) # Muestra la documentacion de la funcion

# Parametros por defecto
def multiplicar(a:str, b=1):
  """Multiplica dos numeros enteros y devuelve el resultado"""
  return a * b

print(multiplicar(5)) # Como al segundo parametro se le asigna un valor cuando se delcara la funcion. Si no se lo pasa como argumento, se le asigna el valor por defecto
print(multiplicar(5, 10)) # Si se le pasa el segundo argumento, se usa el valor pasado como argumento

# Parametros son posicionales
def describirPersona(nombre, edad, sexo):
  print(f"Soy {nombre} tengo {edad} años y me identifico como {sexo}")

describirPersona("Andres", 30, "Masculino")
describirPersona("Hombre ", 'Andres' , 30) #MAL

# Argumentos por clave
# Parametros nombrados
describirPersona(sexo='hombre', nombre='Andres', edad=30) # Utilizando el nombre del parametro, no hace falta seguir el mismo orden de como esta declarada la funcion

# Argumentos de longitud de variables
# se declara como parametro *args (que es un iterable)
# Se le pueden pasar la cantida de elementos que desee
def sumarNumeros(*args):
  result = 0
  for num in args:
    result += num
  return result

print(sumarNumeros(1,2,3,5,4,8,6,9,10,255))

# Argumentos de clave-valor variable **kwargs (key words arguments)
def mostrar_informacion_de(**kwargs):
  # Itera todos los items de los argumentos kwargs
  for key, value in kwargs.items():
    print(f'{key}: {value}')

mostrar_informacion_de(nombre='Andres', sexo='masculino', edad=30)
mostrar_informacion_de(nombre='Carmen', sexo='femenino', nacionalidad='España')