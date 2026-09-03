# EJERCICIO 6: DOS LÍNEAS EN EL MISMO GRÁFICO


from matplotlib import pyplot as plt

# Meses
months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]

# Ventas del producto A
product_a = [100, 120, 150, 140, 180, 200]

# Ventas del producto B
product_b = [80, 100, 130, 160, 170, 190]

product_c = [90, 95, 140, 155, 172, 191]

# Primera línea
plt.plot(
    months,
    product_a,
    marker="o",
    label="Producto A"
)

# Segunda línea
plt.plot(
    months,
    product_b,
    marker="o",
    label="Producto B"
)

plt.plot(
    months,
    product_c,
    marker="o",
    label="Producto C"
)

# Agregar título
plt.title("Comparación de ventas")

# Etiquetas
plt.xlabel("Mes")
plt.ylabel("Ventas")

# Mostrar leyenda
plt.legend()

# Mostrar gráfico
plt.show()