import math
# Solicita:

# Cantidad de calificaciones/periodos.

# Después solicita cada calificación utilizando un ciclo.

# Al final muestra:

# Promedio
# Si aprobó (65 o más)
# Si reprobó

# -------------------
notas = [60, 70, 80, 90, 100]
# indice: 0     notas[en la posicion 0] = 60
# indice: 1     notas[en la posicion 1] = 70

print("Notas en el indice: 1", notas[1])
# -------------------

periodos = int(input("Ingrese la cantidad de periodos: "))

calificaciones = [] # arreglo vacio

for i in range(1, periodos+1):
  print ("Periodo ", i)
  calificaciones.append(float(input("Ingrese la calificacion: ")))

acumulador = 0
for i in range(0, periodos):
  acumulador = acumulador + calificaciones[i]

promedio = acumulador / periodos

print("El promedio es: ", promedio)

# promedio 64.5
if promedio >= 64.5 and promedio < 65:
  promedio = math.ceil(promedio)
  print("Nuevo promedio con math.ceil: ", promedio)

if promedio >= 65:
  print("Excelente Felicidades Aprobo")
else:
  print("Reprobo, Pruebe en otra universidad")