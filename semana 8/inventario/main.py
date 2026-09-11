from archivos import leer_productos
from archivos import escribir_producto

while True:
  print("MENU")
  print("1. Listar productos")
  print("2. Agregar productos")
  print("0. SALIR")

  opcion = int(input("Ingrese una opcion"))

  match opcion:
    case 1:
      productos = leer_productos()
      for line in productos:
        print("Id:", line["id"])
        print("Product name:", line["producto"])
        print("Product Stock", line["stock"])
        print("Product Price:", line["precio"])
        print("="*38)

    case 2:
      id = int(input("Ingrese el Id:"))
      productName = input("Ingrese el nombre del producto:")
      stock = int(input("Ingrese el stock del producto:"))
      price = float(input("Ingrese el precio del producto:"))

      product = {
        "id": id, 
        "product": productName, 
        "stock": stock, 
        "price": price
      }

      escribir_producto(product) 
      # escribir_producto(id, productName, stock, price) 