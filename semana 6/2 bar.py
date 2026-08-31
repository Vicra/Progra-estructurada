# ============================================================
# EJERCICIO 2: GRÁFICO DE BARRAS
# Nivel: Básico
# Objetivo: Aprender a representar cantidades con barras
# ============================================================

from matplotlib import pyplot as plt

# Categorías
products = ["Laptop", "Mouse", "Teclado", "Monitor"]

# Cantidad vendida de cada producto
sales = [15, 30, 22, 10]

# Crear gráfico de barras
plt.bar(products, sales)

# Título
plt.title("Ventas de productos")

# Etiqueta del eje X
plt.xlabel("Producto")

# Etiqueta del eje Y
plt.ylabel("Cantidad vendida")

# Mostrar gráfico
plt.show()


# ------------------------------------------------------------
# EJERCICIO
# ------------------------------------------------------------
# 1. Agrega dos productos más.
# 2. Modifica las cantidades.
# 3. Cambia el título.
# 4. Investiga y prueba:
#
# plt.bar(..., width=0.5)
#
# 5. Prueba barras horizontales:
#
# plt.barh(products, sales)
#
# 6. Agrega una segunda lista de productos y cantidades
#    para intentar comparar dos grupos de ventas.
# ============================================================