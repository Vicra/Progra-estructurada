def mostrar_productos(products):
  print("==== Productos ===")
  for key, value in products.items():
    print("\nId:" , key)
    print("Name:", value["name"])
    print("Price:", value["price"])
    print("Stock:", value["stock"])

def realizar_venta(products):
  nombre_cliente = input("Ingrese el nombre del cliente:")

  lista_de_productos = []
  # valor usado para salirse del ciclo
  CENTINELA = "0"
  while True:
    # proceso
    # mostrarle todos los productos 
    # el usuario selecciona 1
    # el usuario selecciona la cantidad de ese producto
    for key, value in products.items():
      print(f"id:{key}, name:{value["name"]}, price:{value["price"]}, stock:{value["stock"]}")
    print("Ingrese 0 para terminar, si no hay mas productos por agregar")

    producto_seleccionado = input("Ingrese un producto: ")
    if producto_seleccionado == CENTINELA:
      break

    if products[producto_seleccionado]["stock"]  == 0:
      print("El producto seleccionado no tiene stock")
      continue


    cantidad = 0
    # verificar que la cantidad no sea mayor al stock
    while True:
      cantidad = int(input("Ingrese la cantidad que desea de ese producto: "))

      if cantidad <= products[producto_seleccionado]["stock"] and cantidad > 0:
        break

      print(f"La cantidad no puede ser mayor al stock, stock {products[producto_seleccionado]["stock"]}")
    subtotal = cantidad * products[producto_seleccionado]["price"]

    # agregando el producto a la orden de venta
    lista_de_productos.append({
      "id": producto_seleccionado,
      "nombre": products[producto_seleccionado]["name"],
      "precio": products[producto_seleccionado]["price"],
      "cantidad": cantidad,
      "subtotal": subtotal
    })
    print(lista_de_productos[len(lista_de_productos)-1])
    print("Producto agregado...\n")
  # en este punto ya no se agregan mas productos
  # mostrar todos los productos

  # creacion de orden vacia
  nuevaOrden = {
    "nombreCliente": nombre_cliente,
    "detalle": lista_de_productos,
    "total": 0
  }

  return nuevaOrden

def imprimir_ordenes(ordenes):
  print("===== ORDENES ====")
  for key, value in ordenes.items():
    print("Orden:", key)
    print("Nombre Cliente:", value["nombreCliente"])
    print("TOTAL:", value["total"])
    print("---PRODUCTOS--")
    for product in value["detalle"]:
      print(f"Id: {product["id"]} Producto: {product["nombre"]} Precio:{product["precio"]} Subtotal: {product["subtotal"]} Cantidad:{product["cantidad"]}" )
    print("")

def realizar_venta_main(ordenes, productos):
  cantidadLlaves = len(ordenes.keys())
  nuevaLLave = str(cantidadLlaves + 1)
  ordenes[nuevaLLave] = realizar_venta(productos)

  # iniciar el valor de total en 0
  ordenes[nuevaLLave]["total"] = 0

  # iterar(for) sobre los productos de la orden
  for product in ordenes[nuevaLLave]["detalle"]:
      ordenes[nuevaLLave]["total"] = ordenes[nuevaLLave]["total"] + product["subtotal"]
      cantidadAReducir = product["cantidad"]
      # encontrar el producto desde la base de datos (diccionario)
      for productoKey in productos.keys():
          if productoKey == product["id"]:
              nuevoStock = productos[productoKey]["stock"] - cantidadAReducir
              productos[productoKey]["stock"] = nuevoStock

  # ya termine de reducir los stocks
  # mostrar el diccionario de productos
  imprimir_ordenes(ordenes)
  mostrar_productos(productos)