import math

# Ciclos (For)
# Solicita un número.

# Muestra su tabla del 1 al 10.

# Ejemplo:

# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50


# 5 ^ 1 = 5
# 5 ^ 2 = 25
# ...
# 5 ^ 10 = 9765625
  
numero = int(input("Ingrese un numero: "))

#  i = i + 1
for i in range(1, 11):
  print(numero, " x " , i , ": ", numero * i)

for i in range(1, 11):
  print(numero, " ^ ", i, ": ", math.pow(numero, i))