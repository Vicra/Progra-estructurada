productos = {
    "P001": {
        "name": "Laptop",
        "price": 850.00,
        "stock": 5
    },
    "P002": {
        "name": "Mouse",
        "price": 25.00,
        "stock": 20
    },
    "P003": {
        "name": "Teclado",
        "price": 45.00,
        "stock": 10
    }
}

ordenes = {
    "1": {
      "nombreCliente": "Juan Perez",
      "detalle": [
            {
                "id": "P001",
                "nombre": "Laptop",
                "cantidad": 1,
                "precio": 850.00,
                "subtotal": 850.00
            },
            {
                "id": "P002",
                "nombre": "Mouse",
                "cantidad": 2,
                "precio": 25.00,
                "subtotal": 50.00
            }
        ],
        "total": 900.00
    },
    "2": {
        "nombreCliente": "Juan Perez",
        "detalle": [
            {
                "id": "P001",
                "nombre": "Laptop",
                "cantidad": 2,
                "precio": 850.00,
                "subtotal": 850.00
            },
            {
                "id": "P002",
                "nombre": "Mouse",
                "cantidad": 3,
                "precio": 25.00,
                "subtotal": 50.00
            }
        ],
        "total": 900.00
    },
}

from productos import mostrar_productos
from productos import realizar_venta_main
from ordenes import mostrar_resumen
# ========= TIENDA =========
# 1. Mostrar productos
# 2. Buscar producto
# 3. Realizar venta
# 4. Mostrar resumen de ventas (Total Ventas:10, Total en Efectivo:L 13,235.4 )
# 5. Mostrar producto más vendido (cantidad)
# 6. Salir

# Seleccione una opción:

# Instrucciones: Utilizando paquetes y diccionarios crear un programa de inventario para ACOSA

while True:
  print("=====TIENDA=====")
  print("1. Mostrar producto")
  print("3. Realizar venta")
  print("4. Mostrar Resumen de Ventas")
  print("5. Mostrar producto más vendido")

  option = int(input("Ingrese una opcion:"))

  match option:
    case 1:
        mostrar_productos(productos)
    case 3:
        realizar_venta_main(ordenes, productos)
    case 4:
        mostrar_resumen(ordenes)
    case 5:
        productosVendidos = {}
        for orden in ordenes.keys():
           print(f"orden: {orden}")
           for product in ordenes[orden]["detalle"]:
            #   print(f"Producto: {product["nombre"]} {product["cantidad"]}")

            # print(f"Processing... {product["id"]}")
            # print(productosVendidos.get(product["id"]))

            # si no existe en el diccionario, lo agrego
            if productosVendidos.get(product["id"]) == None:
               productosVendidos[product["id"]] = product["cantidad"]
            else:
               print(f"id {product["id"]}")
               print(f"value {productosVendidos[product["id"]]}")
               print(f"cantidad {product["cantidad"]}")
               # ya existe un item en la lista de vendidos
               # productosVendidos[product["id"]] = productosVendidos[product["id"]] + product["cantidad"]
               productosVendidos[product["id"]] += product["cantidad"]
            
        print(productosVendidos)