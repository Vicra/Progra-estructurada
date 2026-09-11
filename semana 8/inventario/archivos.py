from pathlib import Path
import csv

def leer_productos():
  productos = []
  with open(Path(__file__).with_name("inventario.csv"), 
    "r", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)

    for line in reader:
      productos.append(
        line
      )

  return productos


def escribir_producto(product):
  with open(Path(__file__).with_name("inventario.csv"), 
      "a", encoding="utf-8", newline="") as archivo:

      writer = csv.DictWriter(archivo, fieldnames=[
        "id","product","stock","price"
      ])

      writer.writerow(product)