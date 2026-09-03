# EJERCICIO 9: BOXPLOT


from matplotlib import pyplot as plt

# Salarios de diferentes departamentos
development = [
    2500, 2700, 2800, 3000,
    3100, 3200, 3500, 4000
]

marketing = [
    1800, 2000, 2100, 2200,
    2400, 2500, 2700, 3000
]

design = [
    2000, 2200, 2300, 2500,
    2600, 2800, 2900, 3200
]

# Crear Boxplot
plt.boxplot(
    [development, marketing, design],
    label=["Development", "Marketing", "Design"]
)

# Título
plt.title("Distribución de salarios")

# Etiqueta del eje Y
plt.ylabel("Salario")

# Mostrar gráfico
plt.show()


# 1. Agrega otro departamento.
# 2. Agrega más salarios.
# 3. Cambia los valores.
# 4. Observa dónde aparecen los valores extremos.