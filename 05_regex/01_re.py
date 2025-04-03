###
# Expresiones regulares reg ex
# Sirven para buscar y manipular patrones, validar datos, etc
###

'''
Por que aprender regex?
- Busqueda avanzada. Encontrar patrones especificos en textos
- Validacion de datos, dominos, ips, contraseñas, emails....
- Manipulacion de texto: extraer, manipular, editar...
'''
# 1) IMportar el modulo re
import re

# 2) Crear un patron que descriobe lo que quiero encontrar
pattern = "Hola"

# 3) El texto donde queremos buscar
text = 'Hola mundo'

# 4) Utilizar la funcion de busqueda de 're'
result = re.search(pattern, text)

if result:
  print("Valor encontrado en el texto")
else:
  print("Valor no encontrado en el texto")

# .group() devuelve la cadena que conincide con el patron
print(result.group())

# .start() posicion inicial de la coincidencia
print(result.start())

# .end() posicion final de la coincidencia
print(result.end())

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
pattern = "IA"
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"

resultado = re.search(pattern, text)

if resultado:
  print(f'El resultado fue encontrado y comienda en la pposicion {resultado.start()} y termina en la posicion {resultado.end()}')
else:
  print("Valor no encontrado en el texto")

### ------------------------------------------

## Enncontrar todas las coincidencias de un patron
# .finall() devuelve una lista con todas las coincidencias
text = "Me gusta Python. Pyfhon es lo máximo. Aunque Pylhon no es tan difícil, ojo con Python"
pattern = "Python"
# Si se coloca un punto '.' significa que puede ser cualquier caracter
pattern = "Py.hon"
matches = re.findall(pattern, text)
print("valores encontrados: ",matches)
# Al ser una lista el resultado tiene los metodos de una lista
print("cantidad de coincidencias: ", len(matches))

### ------------------------------------------

## .finditer() devuelve un iterador que contiene todos los resultados de la busqueda
text = "Me gusta Python. Pyfhon es lo máximo. Aunque Pylhon no es tan difícil, ojo con Python"
pattern = "Py.hon"
matches = re.finditer(pattern, text)

for match in matches:
  print(match.group(), match.start(), match.end())

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
patron = 'midu'
resultado = re.findall(patron, text)
if resultado:
  print(f'Se encontraron {len(resultado)} coincidencias')
  for r in re.finditer(patron, text):
    print(f'{r.group()} inicia en posicion {r.start()} y acaba en {r.end()}')
else:
  print("Valor no encontrado en el texto")

### ------------------------------------------

### Modificadores

# Son opcione sque se puede agregar a un patron para cambiar su comportamiento
# re.IGNORECASE
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"
# Como 3 argumento se le pasa el modificador (en este caso ignora mayusculas o minusculas)
found = re.findall(pattern, text, re.IGNORECASE)

if found: print(found)

### Reemplazar el texto
# .sub() reemplaza las coincidencias
texto = "Hola, mundo! Hola de nuevo. Hola otra vez."
patron = "hola"
reemplazo = "Adiós"

# primer argumento el patron, luego el texto a reemplazar y luego el texto a modificar
# se puede pasar flags que son los modificadores
# se pueden pasar count que indica la cantidad de coincidencias que se reemplazaran. Por efecto cambia todas las coincidencias
nuevo_texto = re.sub(patron, reemplazo, texto, flags=re.IGNORECASE, count=2)
print(nuevo_texto)