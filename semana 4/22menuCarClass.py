# Desarrollar un 'sistema de gestion de carros'
# Los carros tienen marca, modelo, año; guardar la informacion en un arreglo/lista
# Mostrar menu con opciones de 
# 1. Ver lista de carros
# 2. Agregar carro (solicita el marca, modelo, año del carro, lo agrega al final)
# 3. Eliminar carro (solicita el indice del carro a borrar, no muestra indices en 0)
# 0. Salir

class Car:
  # constructor: funcion que se ejecuta cuando se crea la instancia
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

carros = [
  Car("Ford", "Escape", 2012),
  Car("Toyota", "RAV4", 2026)
]

OPCION_SALIDA = 0
# inicializarlo
opcion = -1

# estrategia de while convencional
while opcion != OPCION_SALIDA:
  print("")
  print("-----MENU-----")
  print("1. Ver lista de carros")
  print("2. Agregar un carro")
  print("3. Eliminar un carro")
  print("0. Salir")
  opcion = int(input("Ingrese una opcion: "))

  # switch statement
  match opcion:
    case 1:
      print("")
      print("LISTA DE CARROS")

      if len(carros) == 0:
        print("No hay carros en este momento")
      else:
        for i in range(len(carros)):
          print(i + 1, carros[i].brand, carros[i].model, carros[i].year)
    case 2:
      print("")
      print("AGREGAR UN CARRO")
      nombre = input("Ingrese el nombre del nuevo carro: ")

      # agregar el nombre a la lista de carros
      carros.append(nombre)

    case 3:
      print("")
      print("ELIMINAR UN CARRO")

      for i in range(len(carros)):
        print(i + 1, carros[i])

      inputABorrar = int(input("Ingrese el numero del carro a borrrar: "))

      print("Carro eliminado: ", carros.pop(inputABorrar - 1))

    case 0:
      print("Salir")
    case _:
      print("Opcion invalida")
