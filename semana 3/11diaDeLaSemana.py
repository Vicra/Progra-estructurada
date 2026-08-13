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

  opcion = int(input("Ingrese el numero del dia: "))

  if opcion == 1:
    print("Lunes")
  elif opcion == 2:
    print("Martes")
  elif opcion == 3:
    print("Miercoles")
  elif opcion == 4:
    print("Jueves")
  elif opcion == 5:
    print("Viernes")
  elif opcion == 6:
    print("Sabado")
  elif opcion == 7:
    print("Domingo")
  elif opcion == 8:
    break;
  else:
    print("Dia invalid")
  