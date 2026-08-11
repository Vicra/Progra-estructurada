numeros = [15, 34, 2, 189, 267, 31, 89, 1234]
# max = 267

maximo = numeros[0] # maximo es 15
for i in range(0, len(numeros)): # i < n ?   es 7 < 7?
  if numeros[i] > maximo:
    maximo = numeros[i]

print("El maximo es: ", maximo)