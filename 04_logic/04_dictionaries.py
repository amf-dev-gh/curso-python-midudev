from os import system
if system("clear") != 0: system("cls")

###
# Los diccionarios son coleeciones de pares clave-valor
# Sirven para almacenar datos relacionados
###

# Ejemplo basico
persona = {
  "nombre" : "Andres",
  "edad" : 30,
  "calificaciones" : [5, 8, 9],
  "es_programador": True,
  "redes" : {
    "instagran" : "ig_andrres",
    "facebook" : "fb_andres",
    }
}

## Acceder a los valores
# Se coloca el nombre del diccionario y entre corchetes se le pasa un string con el nombre de la clave del valor buscado
print(persona["nombre"])
print(persona["calificaciones"][1])
print(persona["redes"]["facebook"])

## Cambiar valor al acceder
persona["nombre"] = "Magandi"
print(persona["nombre"])
persona["calificaciones"][2] = 10

## Se puede imprimir el diccionario completo
print(persona)

## Eliminar por completo una propiedad
del persona["edad"]
print(persona)

## Eliminar pero a su vez obtener el valor eliminado
dato_eliminado = persona.pop("es_programador")
print(f"Es programador: {dato_eliminado}")
print(persona)

## Sobreescribir un diccionario con otro
a = {"nombre":"andres", "edad":30}
b = {"nombre":"carmen", "edad":35, "es_logopeda": True}
# --> El valor 'a' es actualizado con los valores de 'b'
a.update(b)
print(a)

## Comprobar si existe una propiedad o 'clave' en un diccionario
print("nombre" in a)
print("name" in a)

## Obtener todas las claves o propiedades
print("\n Claves o Keys")
print(persona.keys())

## Obtener todos los valores del diccionario
print("\n Valores o Values")
print(persona.values())

## Obtener tanto la clave como el valor de todos los items
print("\n items -> clave,valor")
print(persona.items())

# Esto retorna una tupla con su clave y valor, utiles en for
print("\nFor cpn tupla -> clave,valor")
for key, value in persona.items():
  print(f"{key} -> {value}")