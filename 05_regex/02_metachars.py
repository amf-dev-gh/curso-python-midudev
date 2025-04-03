###
# Meta caracteres
# Son simbolos especiales con significados especificos en las reg ex.
###

import re

# 1) el punto '.'
# significado: coincidir con cualquier caracter excepto que sea una nueva linea
texto= 'Hola mundo, H0la de nuevo, H$la otra vez'
patron = r'H.la' # donde esta el punto puede haber cualquier caracter
# el patron debe comenzar con r para indicar que es una expresion regluar

found = re.findall(patron, texto)

if found:
  print(found)
else:
  print('No se ha encontrado el patron')

text = "casa caasa cosa cisa cesa causa"
pattern = r"c.sa"

matches = re.findall(pattern, text)
print(matches)

# --------------------

## Barra invertida para anular el significado especial de un simbolo
text = "Mi casa es blanca. Y el coche es negro."
# Al colocar R, indica que es una expresion regular
# y con la \ (barra invertida) indicamos que ignore el significado especial del carater y lo tome como tal ( el punto es punto)
pattern = r'\.'
matches= re.findall(pattern, text)
print(matches)

## \d: coincide con cualquier digito numerico (0-9)
text = "El numero de teléfono es 123456789"
found = re.findall(r'\d{9}', text)
print(found)

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34
text = "Mi número de teléfono es +34 688999999 apúntalo vale?"
patron = r'\+34 \d{9}'
found = re.search(patron, text)
if found: print(f"Encontre el número de teléfono {found.group()}")

# \w: Cualquier caracter alfanumerico hace coincidencia (a-z, A-Z, 0-9, _)
text = "el_rubi@us_69@"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s: coincide con espacio en blanco, tabulacion o salto de linea
text = "Hola mundo\n Como estas?\t"
pattern = r'\s'
matches = re.findall(pattern, text)
print(matches)

# ^: Coincide con el principio de una cadena
username = "@423_name%22"
pattern = r'^\w' # Valida que el nombre de usuario comience con caracter
valid = re.search(pattern, username)
if valid: print("El nombre de usuario es válido")
else: print("El nombre de usuario no es válido")

phone = "+34 688999999"
pattern = r"^\+\d{1,3} "

valid = re.search(pattern, phone)

if valid: print("El número de teléfono es válido")
else: print("El número de teléfono no es válido")

# $: Coincide con el final de una cadena
text = "Hola mundo."
pattern = r"mundo$"

valid = re.search(pattern, text)

if valid: print("La cadena es válida")
else: print("La cadena no es válida")

# EJERCICIO
# Valida que un correo sea de gmail
text = "miduga@hotmail.com"
pattern = r"@gmail.com$"
valid = re.search(pattern, text)
if valid: print("El correo es válido")
else: print("El correo es inválido")

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r'\w{1,10}\.txt'
found = re.findall(pattern, files)
for f in found:
  print(f)

# \b: Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"
found = re.findall(pattern, text)
print(found)

# |: Coincidr con una opción u otra
fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, piña, aguacate"
pattern = r"palta|aguacate|p..a|\w{7}"
found = re.findall(pattern, fruits)
print(found)