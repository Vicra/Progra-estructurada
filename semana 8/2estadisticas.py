# Utilizando el mismo CSV:

# Calcular el promedio de notas.
# Encontrar la nota más alta.
# Encontrar la nota más baja.
# Contar cuántos estudiantes aprobaron.
# Contar cuántos reprobaron.

import csv
from pathlib import Path

notas = []

CALIFICACION_MINIMA = 65

with open(Path(__file__).with_name("pe-calificaciones.csv"), 
    "r", encoding="utf-8") as archivo:
  reader = csv.DictReader(archivo)

  promedio = 0
  for line in reader:
    notas.append(float(line['nota']))
    promedio += float(line['nota'])

  # dividir para sacar el promedio
  promedio = promedio / len(notas)

  cantidadAprobados = 0
  cantidadReprobados = 0

  for nota in notas:
    if nota >= CALIFICACION_MINIMA:
      cantidadAprobados += 1
    else:
      cantidadReprobados += 1

  print(f"Promedio: {promedio:.2f}")
  print(f"Notas mas alta {max(notas)}")
  print(f"Notas mas baja {min(notas)}")
  print(f"Cantidad de aprobados: {cantidadAprobados}")
  print(f"Cantidad de reprobados: {cantidadReprobados}")
  