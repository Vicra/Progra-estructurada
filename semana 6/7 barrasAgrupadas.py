# EJERCICIO 7: GRÁFICO DE BARRAS AGRUPADAS


from matplotlib import pyplot as plt

# Categorías
months = ["Ene", "Feb", "Mar", "Abr"]

# Ventas de 2025
sales_2025 = [100, 120, 150, 130]

# Ventas de 2026
sales_2026 = [120, 140, 160, 180]

# Posiciones de las barras
x = [0, 1, 2, 3]

# Ancho de las barras
width = 0.35

# Barras del año 2025
plt.bar(
    [value - width / 2 for value in x],
    sales_2025,
    width=width,
    label="2025"
)

# Barras del año 2026
plt.bar(
    [value + width / 2 for value in x],
    sales_2026,
    width=width,
    label="2026"
)

# Colocar nombres de los meses
plt.xticks(x, months)

# Título
plt.title("Ventas 2025 vs 2026")

# Etiquetas
plt.xlabel("Mes")
plt.ylabel("Ventas")

# Leyenda
plt.legend()

# Mostrar gráfico
plt.show()