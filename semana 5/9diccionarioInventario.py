# ==========================================
# EJERCICIO: INVENTARIO
# ==========================================

# Inventario es un diccionario que contiene varios productos
# Los productos son diccionarios

# productos: precio, cantidad, categoria

# 1. Mostrar informacion de un producto
# 2. Modificar informacion de un producto
# 3. Agregar un producto
# 4. Recorrer el inventario

producto = {
  "sku": "1234567890123",
  "name": "Leche Entera",
  "precio": 30,
  "cantidad": "10",
  "categoria": "Lacteos"
}

inventario = {
  "Leche Entera" : {
    "sku": "1234567890123",
    "precio": 30,
    "cantidad": "10",
    "categoria": "Lacteos"
  },
  "Leche Descremada" : {
    "sku": "1234567890124",
    "name": "Leche Descremada",
    "precio": 30,
    "cantidad": "10",
    "categoria": "Lacteos"
  }
}

print("SKU:", inventario["Leche Entera"]["sku"])
print("Precio: ",inventario["Leche Entera"]["precio"])
# print(inventario["Leche Descremada"])


inventario2 = {
  "1234567890123" : {
    "name": "Leche Entera",
    "precio": 30,
    "cantidad": 10,
    "marca": "Leyde",
    "lote": 123,
    "fechaExpiracion": "09/15/2026"
  },
  "1234567890124" : {
    "name": "Leche Entera",
    "precio": 31,
    "cantidad": 15,
    "categoria": "Lacteos",
    "marca": "Sula",
    "lote": 343,
    "fechaExpiracion": "09/15/2026"
  }
}

# 1er Manera de Hacer el Print
# for sku, product in inventario2.items():
#   print("\nProducto:", sku)
#   print("Nombre: ", product["name"])
#   print("Precio: ", product["precio"])
#   print("Stock: ", product["cantidad"])
#   print("Categoria: ", product["categoria"])
#   print("Marca: ", product["marca"])

# 2da Manera de Hacer el Print
print ("\nSEGUNDA MANERA DE IMPRIMIR")
for key, value in inventario2.items():
  print("\nSKU:", key)
  for key2, value2 in inventario2[key].items():
    print(key2, ":", value2)