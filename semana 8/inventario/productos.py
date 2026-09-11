from archivos import leer_productos
from archivos import guardar_productos

def mostrar_productos(productos):
  for line in productos:
    mostrar_producto(line)

def mostrar_producto(producto):
  print("Id:", producto["id"])
  print("Product name:", producto["producto"])
  print("Product Stock", producto["stock"])
  print("Product Price:", producto["precio"])
  print("="*38)

def ingresar_producto():
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

  return product

def buscar_productos_id(products):
  idBusqueda = input("Ingrese el id a buscar:")

  # foreach
  for product in products:
    if product["id"] == idBusqueda:
      return product
  # deberia de haber un valor de retorno
  # si llega aca es porque no hay productos que matcheen con la busqueda
  return None

def buscar_productos_categoria(products):
  inputCategory = input("Ingrese la categoria a buscar:")
  resultados = []
  for product in products:
    if product["categoria"] == inputCategory:
      resultados.append(product)
  return resultados

def modificar_producto():
  idBuscar = input("Ingrese el id del producto a modificar:")

  products = leer_productos()

  for product in products:
    # encontrar el producto
    if product["id"] == idBuscar:
      # presentarle el producto como está
      mostrar_producto(product)

      # pedirle los nuevos valores
      product["producto"] = input("Ingrese el nuevo nombre:")
      product["categoria"] = input("Ingrese la nueva categoria:")
      product["stock"] = input("Ingrese el nuevo stock:")
      product["precio"] = input("Ingrese el nuevo precio:")

      break

  guardar_productos(products)

