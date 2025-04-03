"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

"""

from os import system
if system("clear") != 0: system("cls")

## Opcion rebuscada
# def battle (list_a, list_b):
#   size = len(list_a)-1
#   ganador = {}
#   for index in range(size):
#     if list_a[index] > list_b[index]:
#       diferencia = list_a[index] - list_b[index]
#       list_a[index+1] += diferencia

#     if list_b[index] > list_a[index]:
#       diferencia = list_b[index] - list_a[index]
#       list_b[index+1] += diferencia

#   if (list_a[size] - list_b[size]) > 0:
#     ganador.update({"lista": "a", "puntos":(list_a[size] - list_b[size])})
#   if (list_b[size] - list_a[size]) > 0:
#     ganador.update({"lista": "b", "puntos":(list_b[size] - list_a[size])})
#   if (list_b[size] - list_a[size]) == 0:
#     ganador.update({"lista": "empate", "puntos":0})
#   print("Ganador ", ganador)

## Opcion ideal
def battle(lista_a, lista_b):
    # sum() suma todos los elementos iterables de la lista, si no hay elementos devuelve 0
    puntos_a = sum(lista_a)
    puntos_b = sum(lista_b)

    # esto dice: Retorna 
    # '(diferencia de puntos a-b)A' si la lista a suma mas que la lista b
    # sino retorna '(diferencia de puntos b-a)B' si la lisya b suma mas que la lista a
    # de lo contrario retorna X
    return f"{puntos_a - puntos_b}pts-A" if puntos_a > puntos_b else f"{puntos_b - puntos_a}pts-B" if puntos_b > puntos_a else "X"

#------------------------------------------------------------

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

print(battle(lista_a, lista_b))