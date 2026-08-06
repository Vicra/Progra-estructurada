# Solicita un número del 1 al 7.

# Muestra:

# 1 → Lunes
# 2 → Martes
# 3 → Miércoles
# 4 → Jueves
# 5 → Viernes
# 6 → Sábado
# 7 → Domingo

# Si escribe otro número:

# Día inválido.
while True:
  print("1 → Lunes")
  print("2 → Martes")
  print("3 → Miércoles")
  print("4 → Jueves")
  print("5 → Viernes")
  print("6 → Sábado")
  print("7 → Domingo")
  print("8 → Salir del Sistema")

  opcion = input("Ingrese el numero del dia: ")

  # switch statement
  match opcion:
    case 1:
      print ("Lunes")
    case 2:
      print ("Martes")
    case 3:
      print ("Miercoles")
    case 4:
      print ("Jueves")
    case 5:
      print ("Viernes")
    case 6:
      print ("Sabado")
    case 7:
      print ("Domingo")
    case 8:
      break
    case _:
      print("Numero invalido")
  