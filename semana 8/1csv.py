# Crear un archivo estudiantes.csv:
# id,nombre,edad,curso,nota

# Crear un programa que:
# Abra el archivo.
# Lea todos los estudiantes.
# Muestre cada estudiante.
# Muestre solamente los estudiantes de Python.
# Muestre los estudiantes con nota mayor a 80. 

# csv.reader, with open()

# CSV = Comma Separated Values

import csv
from pathlib import Path

notas = []

with open(Path(__file__).with_name("datos.csv"), "r", encoding="utf-8") as archivo:
  reader = csv.DictReader(archivo)

  for line in reader:
    if line['curso'] == "Python":
      print("Id:", line['id'])
      print("Nombre:", line['nombre'])
      print("Edad:", line['edad'])
      print("Curso:", line['curso'])
      print("Nota:", line['nota'])
      print("---")