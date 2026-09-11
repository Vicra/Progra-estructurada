from archivos import leer_productos
from archivos import escribir_producto
from productos import mostrar_productos
from productos import mostrar_producto
from productos import ingresar_producto
from productos import buscar_productos_id
from productos import buscar_productos_categoria
from productos import modificar_producto

# declaracion de la funcion
def mostrar_menu():
  while True:
    print("="*38)
    print("         MENU")
    print("="*38)
    print("1. Listar productos")
    print("2. Agregar productos")
    print("3. Buscar productos por id")
    print("4. Buscar productos por categoria")
    print("5. Modificar un producto")
    print("0. SALIR")

    opcion = int(input("Ingrese una opcion:"))

    match opcion:
      case 1:
        products = leer_productos()
        # llamado de la funcion 
        mostrar_productos(products)
      case 2:
        product = ingresar_producto()
        escribir_producto(product)
      case 3:
        products = leer_productos()
        productoExiste = buscar_productos_id(products)

        if productoExiste:
          mostrar_producto(productoExiste)
        else:
          print("No existe un producto con ese id")
      case 4:
        products = leer_productos()
        productosFiltrados = buscar_productos_categoria(products)
        if productosFiltrados == []:
          print("No hay resultados")
        else:
          mostrar_productos(productosFiltrados)
      case 5:
        modificar_producto()
      case 0:
        break
      case _:
        print("Opcion invalida")

# llamada de la funcion
mostrar_menu()