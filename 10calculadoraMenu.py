# Solicita:

# Primer número
# Segundo número

# Muestra un menú:

# A. Sumar
# B. Restar
# C. Multiplicar
# D. Dividir

# Según la opción elegida realiza la operación utilizando switch.

# Si el usuario selecciona una opción inválida, mostrar:

# Opción no válida.


a = float(input("Ingrese el valor de Primer numero: "))
b = float(input("Ingrese el valor de Segundo numero: "))

# switch
# if -> elif -> elif -> elif -> else

print("MENU")
print("A. Addition")
print("B. Substraction")
print("C. Dividir")
print("D. Multiplicar")

opcion = input("Ingrese el valor: ")

# Switch statement
match opcion:
  case "A":
    print("Suma:", a+b)
  case "B":
    print("Resta:", a-b)
  case "C":
    print("Div:", a/b)
  case "D":
    print("Mult:", a*b)
  case _:
    print("Input invalido")


# "b" == "B"?