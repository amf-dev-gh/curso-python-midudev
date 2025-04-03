###
# Las clases son plantillas para crear objetos
####

# Ejemplo basico
class Coche:
  # Atributo de la clase. cada instacia del objeto tendra este atributo
  tipo = "Vehiculo de 4 ruedas"

  # Metodo que contruye al objeto o __init__
  def __init__(self, marca, modelo, color):
    self.marca = marca
    self.modelo = modelo
    self.color = color

  # Metodos de todos los objetos instanciados
  def arrancar(self):
    print(f'El coche {self.marca} {self.modelo} {self.color} arrancó')

###------------------------------------

coche_1 = Coche("Toyota","Corolla","Rojo")
coche_1.arrancar()
print(coche_1)

coche_2 = Coche("Ford","Fiesta","Azul")
coche_2.arrancar()