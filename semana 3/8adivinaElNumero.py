# Define un número secreto.
# numero_secreto = 7

# Pide al usuario que lo adivine.
# Si acierta:
#   ¡Correcto!
#   Programa termina
# En caso contrario:
#   Inténtalo de nuevo.

# sintaxis
# while <condicion de salida>
# while cont = 10

numero = 10

while True:
  intento = float(input("Adivina el numero entre [1-10]: "))
  if intento == numero:
    print("Correcto")
    break
  else:
    print("Intente de nuevo")