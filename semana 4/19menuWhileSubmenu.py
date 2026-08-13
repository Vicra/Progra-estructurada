
OPCION_SALIDA_MENU = 0
OPCION_SALIDA_SUBMENU = -1
opcion = -1

while opcion != OPCION_SALIDA_MENU:
  print("")
  print("MENU")
  print("1. Opcion A")
  print("2. Opcion B")
  print("3. Opcion C")
  print("4. Opcion D")
  print("0. Salir")

  opcion = int(input("Ingrese una opcion: "))

  match opcion:
    case 0:
      print("Adios")
    case 1:
      while opcion != OPCION_SALIDA_SUBMENU:
        print("")
        print("Sub MENU")
        print("1. Opcion 1.1")
        print("2. Opcion 1.2")
        print("3. Opcion 1.3")
        print("4. Opcion 1.4")
        print("-1. Salir del submenu")

        opcion = int(input("Ingrese una opcion: "))

        match opcion:
          case 0:
            print("Adios")
          case 1:
            print("1.1 Opcion")
          case 2:
            print("1.2 Opcion")
          case 3:
            print("1.3 Opcion")
          case 4:
            print("1.4 Opcion")
          case _:
            print("Opcion invalida")
    case 2:
      print("Opcion B")
    case 3:
      print("Opcion C")
    case 4:
      print("Opcion D")
    case _:
      print("Opcion invalida, ingrese valor dentro del rango")


print("Fuera del ciclo")