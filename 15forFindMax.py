numeros = [15, 34, 2, 189, 267, 31, 6]

maximo = numeros[0]
for i in range(len(numeros)):
  if numeros[i] > maximo:
    maximo = numeros[i]

print("El maximo es: ", maximo)