###
# Conversion de typos de un valor a otro
###

print("Conversion de tipos")
print(type(int("100")))
# print("100" + 2) ---> no se puede

print(int("111") + 2)
print(float("1.25589"))

# El unico valor que se trata como falso es el 0 o cadenas vacias, el resto son verdaderos
print(bool(3))
print(bool(0))
print(bool(-10))
print(bool(""))
print(bool("Hola"))

# Redondeo (redondea al entero par si es justo la mitad mas cercano)
print(round(1.5))
print(round(1.6))

