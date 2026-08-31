def obtenerOperadores():
  operadorA = float(input("Ingrese el 1er operador:"))
  operadorB = float(input("Ingrese el 2do operador:"))
  return operadorA, operadorB

def imprimirResultado(resultado):
  print("El resultado es: ", f"{resultado:.2f}")

def sumar():
  print("\nSUMAR")
  operadorA, operadorB = obtenerOperadores()
  imprimirResultado(operadorA + operadorB)

def restar():
  print("\nRESTA")
  operadorA, operadorB = obtenerOperadores()
  imprimirResultado(operadorA - operadorB)

def multiplicar():
  print("\nMULTIPLICACION")
  operadorA, operadorB = obtenerOperadores()
  imprimirResultado(operadorA * operadorB)

def sumarNOperandos():
  print("\nSUMAR CON N OPERANDOS")
  amount = int(input("Ingrese cuantos operandos va a sumar: "))
  total = 0
  for i in range(amount):
    operando = float(input(f"Ingrese el operando {i + 1}: "))
    total = total + operando
  print("El resultado total es:", total)

def sumarHastaCentinela():
  print("\nSUMAR INFINITO")
  # este valor sirve como señal para terminar el ciclo
  valorCentinela = -999

  total = 0
  while True:
    operando = float(input("Ingrese el operando: "))

    if operando == valorCentinela:
      break
    else:
      # estas dos lineas son exactamente lo mismo
      # total = total + operando
      total += operando
  print("El valor total es:", total)

def potencia():
  print("\nPOTENCIAS")
  base = float(input("Ingrese la base:"))
  exp = float(input("Ingrese el exponente:"))

  imprimirResultado(pow(base, exp))

while True:
  print("\nCALCULADORA MENU")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Sumar con n operandos")
  print("5. Sumar infinito hasta -999")
  # print("5. Dividir")
  print("6. Potencia")
  option = int(input("Ingrese una opcion del menu:"))

  match option:
    case 1:
      sumar()
    case 2:
      restar()
    case 3:
      multiplicar()
    case 4:
      sumarNOperandos()
    case 5:
      sumarHastaCentinela()
    case 6:
      potencia()
    case 0:
      break
    case _:
      print("Opcion no valida")