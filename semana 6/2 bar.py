# ============================================================
# EJERCICIO 2: GRÁFICO DE BARRAS
# Nivel: Básico
# Objetivo: Aprender a representar cantidades con barras
# ============================================================

from matplotlib import pyplot as plt
import random

colors = [
  "red", "green", "blue", "yellow", "darkblue", "cyan", "pink",
  "purple", "black", "orange"
]
colorIndex = random.randint(0,9)

xValues = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
yValues = []
for i in range(len(xValues)):
  yValues.append(random.randint(1, 100))

barType = random.randint(0,1)
if barType == 0:
  plt.bar(xValues, yValues, color=colors[colorIndex], width=0.6)
  plt.text("Febrero", yValues[2], "Indicador")
else:
  plt.barh(xValues, yValues, color=colors[colorIndex])
  plt.annotate("Annotate", (3, 4))

plt.title("Ventas por Mes")
plt.xlabel("Meses")
plt.ylabel("Ventas")

plt.grid(True)

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