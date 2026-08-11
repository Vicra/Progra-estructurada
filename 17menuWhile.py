opcion = -1

OPCION_SALIDA = 4

while opcion != OPCION_SALIDA:
  print("MENU")
  print("1. Opcion A")
  print("2. Opcion B")
  print("3. Opcion C")
  print("4. Salir")

  opcion = int(input("Ingrese una opcion: "))

  match opcion:
    case 1:
      print("Opcion A")
    case 2:
      print("Opcion B")
    case 3:
      print("Opcion C")
    case 4:
      print("Adios")
    case _:
      print("Opcion invalida, ingrese valor dentro del rango")