# ejercicio en base a ejercicio 14
contrasena = "admin2026"
inputContrasena = "" 

MAXIMO_INTENTOS_PERMITIDOS = 3
intentosRealizados = 0

alumnos = [
  "Jorge Bonilla","Jorge Paz","Alba Mena","Adrian Aviles","Victor Ramirez","Paris Rodas"
]

while True:
  print("")
  print("INICIAR SESION")
  inputContrasena = input("Ingrese su contrasena: ")

  if inputContrasena == contrasena:
    while True:
      print("") # '\n' new line
      print("MENU")
      print("1. Ver alumnos")
      print("0. Salir")

      opcion = int(input("Ingrese una opcion: "))

      match opcion:
        case 1:
          for i in range(len(alumnos)):
            print(i+1, alumnos[i])
        case 0:
          break
        case _:
          print("Opcion invalida")
  else:
    # incrementar la cantidad de intentorRealizados (+1)
    intentosRealizados = intentosRealizados + 1

    if intentosRealizados == MAXIMO_INTENTOS_PERMITIDOS:
      print("Usuario bloqueado")
      break

    # informar al usuario cuantos intentos le quedan
    intentosRestantes = MAXIMO_INTENTOS_PERMITIDOS - intentosRealizados
    print("Contrasena incorrecta, Intentos restantes:", intentosRestantes)

