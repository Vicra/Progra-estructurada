# EJERCICIO 10: SUBPLOTS


from matplotlib import pyplot as plt

# Datos
months = ["Ene", "Feb", "Mar", "Abr"]

sales = [100, 150, 130, 180]

expenses = [80, 90, 100, 120]

products = ["A", "B", "C", "D"]

stock = [20, 35, 15, 40]

# Crear una figura con 2 filas y 2 columnas
fig, axes = plt.subplots(2, 2)

# ------------------------------------------------------------
# GRÁFICO 1: LÍNEA
# ------------------------------------------------------------

axes[0, 0].plot(months, sales)

axes[0, 0].set_title("Ventas")

axes[0, 0].set_xlabel("Mes")

axes[0, 0].set_ylabel("Ventas")


# ------------------------------------------------------------
# GRÁFICO 2: BARRAS
# ------------------------------------------------------------

axes[0, 1].bar(months, expenses)

axes[0, 1].set_title("Gastos")

axes[0, 1].set_xlabel("Mes")

axes[0, 1].set_ylabel("Gastos")


# ------------------------------------------------------------
# GRÁFICO 3: SCATTER
# ------------------------------------------------------------

axes[1, 0].scatter(sales, expenses)

axes[1, 0].set_title("Ventas vs Gastos")

axes[1, 0].set_xlabel("Ventas")

axes[1, 0].set_ylabel("Gastos")


# ------------------------------------------------------------
# GRÁFICO 4: PIE
# ------------------------------------------------------------

axes[1, 1].pie(
    stock,
    labels=products,
    autopct="%1.1f%%"
)

axes[1, 1].set_title("Stock")


# Ajustar automáticamente los espacios
plt.tight_layout()

# Mostrar todos los gráficos

plt.savefig("test")

plt.show()



# 1. Cambia los datos.
# 2. Cambia los títulos.
# 3. Cambia uno de los gráficos.
# 4. Intenta agregar un quinto gráfico.
# 5. Prueba:
#
# plt.subplots(3, 2)
#
# 6. Diferencia entre
# plt.title()
# y:
# axes[0, 0].set_title()