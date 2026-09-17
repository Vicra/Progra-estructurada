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

from productos import mostrar_productos
from productos import realizar_venta
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

  option = int(input("Ingrese una opcion:"))

  match option:
    case 1:
      mostrar_productos(productos)
    case 3:
      realizar_venta(productos)