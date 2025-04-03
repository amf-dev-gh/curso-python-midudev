###
#Los inputs son datos que se piden y se guardan en una variable.
### 

print("¿Cuál es tu nombre?")
my_name = input() # input() devuelve un string, no es necesario convertirlo a string
print("Hola " + my_name + " ¿Cuántos años tienes?")

age = input("Cuantos años tiene? \n")

print(f"dentro de 20 años tendrás {int(age) + 20} años") # input() devuelve un string, por lo que hay que convertirlo a int para hacer operaciones matemáticas

country, city = input("En que pais y ciudad vives? \n").split()

print(f"Vives en {city} en el pais {country}")