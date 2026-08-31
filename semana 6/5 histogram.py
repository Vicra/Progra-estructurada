# ============================================================
# EJERCICIO 5: HISTOGRAMA
# Nivel: Intermedio
# Objetivo: Aprender a visualizar la distribución de datos
# ============================================================

from matplotlib import pyplot as plt

# Edades de un grupo de personas
ages = [
    18, 19, 20, 21, 22,
    22, 23, 24, 24, 25,
    25, 26, 27, 28, 30,
    31, 32, 35, 36, 40
]

# Crear histograma
plt.hist(ages)

# Título
plt.title("Distribución de edades")

# Eje X
plt.xlabel("Edad")

# Eje Y
plt.ylabel("Cantidad de personas")

# Mostrar gráfico
plt.show()


# ------------------------------------------------------------
# EJERCICIO
# ------------------------------------------------------------
# 1. Cambia las edades.
# 2. Agrega más personas.
# 3. Investiga qué hace:
#
# bins
#
# Prueba:
#
# plt.hist(ages, bins=5)
#
# y después:
#
# plt.hist(ages, bins=10)
#
# 4. Compara cómo cambia el gráfico.
# ============================================================