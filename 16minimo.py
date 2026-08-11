numeros = [10, 40, 2, 75, 1, 8, -1]

minimo = numeros[0]
for i in range(len(numeros)):
  print("Comparando... min:", minimo, "contra elemento en la posicion[", i, "]:", numeros[i])
  if numeros[i] < minimo:
    minimo = numeros[i]

print("El minimo es: ", minimo)