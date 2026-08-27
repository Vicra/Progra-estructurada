def ver_lista():
  print("\nLISTA")

def agregar_item():
  print("\nAGREGAR ITEM")

def editar():
  print("editar")

def borrar():
  print("borrar")

while True:
  print("\nMENU")
  print("1. Lista")
  print("2. Agregar item")
  print("3. Editar item")
  print("4. Borrar item")
  print("5. Reporte")
  print("0. Salir")

  option = int(input("Ingrese una opcion:"))

  match option:
    case 1:
      ver_lista()
    case 2:
      agregar_item()
    case 3:
      editar()
    case 4:
      borrar()
    case 0:
      break
    case _:
      print("Opcion invalida")

