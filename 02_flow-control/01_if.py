###
# Sentencias condicionales
# if, elif, else
# Permiten ejecutar codigo dependiendo de si se cumple una condicion o no.
###

print("Sentencia simple condicional")

edad = 30

if edad >= 18: # No utiliza llaves, si no tabulaciones.
    print("Eres mayor de edad")
    print("Felicidades")

#--------------------------------------------

print("Sentencia con else")
edad = 15

if edad >= 18:
        print("Eres mayor de edad")
else:
        print("Eres menor de edad")

#--------------------------------------------

print("sentencia con elif")

nota = 7
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Notable")
else:
    print("Suspendido!!")

#--------------------------------------------

print("Condiciones multiples")
# Operadores logicos: and, or, not
# En Java se utilizan && y || respectivamente
edad = 25
tiene_licencia = False
if edad >= 18 and tiene_licencia:
# if edad >= 18 or tiene_licencia:
    print("Puedes conducir")
else:
    print("No puedes conducir!!! 🚓")

# En Java para negar una condicion se utiliza !, en python se utiliza not
es_fin_de_semana = True
if not es_fin_de_semana: # Si no es fin de semana
    print("A trabajar!!!")
else:
    print("A descansar!!!")

#--------------------------------------------

print("Condiciones anidadas")
edad = 20
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes salir a bailar")
    else:
        print("No tienes dinero")
else:
    print("No puedes entrar a la discoteca")