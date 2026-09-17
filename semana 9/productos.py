def mostrar_productos(products):
  for key, value in products.items():
    print("Id:" , key)
    print("Name:", value["name"])
    print("Price;", value["price"])
    print("Stock:", value["stock"])
    print("="*15)
  print("Ingrese 0 para terminar, si no hay mas productos por agregar")

def realizar_venta(products):
  nombre_cliente = input("Ingrese el nombre del cliente:")

  lista_de_productos = []
  # valor usado para salirse del ciclo
  CENTINELA = "0"
  while True:
    # mostrarle todos los productos 
    # el usuario selecciona 1
    # el usuario selecciona la cantidad de ese producto
    for key, value in products.items():
      print(f"id:{key}, name:{value["name"]}, price:{value["price"]}, stock:{value["stock"]}")

    producto_seleccionado = input("Ingrese un producto: ")
    if producto_seleccionado == CENTINELA:
      break

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
      "name": products[producto_seleccionado]["name"],
      "price": products[producto_seleccionado]["price"],
      "quantity": cantidad,
      "subtotal": subtotal
    })
    print(lista_de_productos[len(lista_de_productos)-1])
    print("Producto agregado...\n")
  # en este punto ya no se agregan mas productos
  # mostrar todos los productos
  print(lista_de_productos)

  # reducir el stock
