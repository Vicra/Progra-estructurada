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
        "id","product","category","stock","price", 
      ])

      writer.writerow(product)

def guardar_productos(products):
   with open(Path(__file__).with_name("inventario.csv"), 
    "w", encoding="utf-8", newline="") as archivo:
      writer = csv.DictWriter(
         archivo,
         fieldnames=[
            "id", "producto", "categoria", "stock", "precio"
         ]
      )

      writer.writeheader()
      writer.writerows(products)