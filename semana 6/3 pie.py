# ============================================================
# EJERCICIO 3: GRÁFICO DE PIE / CIRCULAR
# Nivel: Básico - Intermedio
# Objetivo: Aprender a representar porcentajes
# ============================================================

from matplotlib import pyplot as plt

# Categorías
languages = ["Python", "JavaScript", "Java", "C++"]

# Cantidad de estudiantes que eligieron cada lenguaje
students = [40, 30, 20, 10]

# Crear gráfico circular
plt.pie(
    students,
    labels=languages,
    autopct="%1.1f%%"
)

# Agregar título
plt.title("Lenguajes de programación favoritos")

# Mostrar gráfico
plt.show()

# ------------------------------------------------------------
# EJERCICIO
# ------------------------------------------------------------
# 1. Agrega más lenguajes.
# 2. Cambia los porcentajes.
# 3. Investiga qué hace:
#
# autopct="%1.1f%%"
#
# 4. Investiga cómo separar una sección del gráfico:
#
# explode
#
# Ejemplo:
#
# explode = [0.1, 0, 0, 0]
#
# plt.pie(
#     students,
#     labels=languages,
#     autopct="%1.1f%%",
#     explode=explode
# )
#
# 5. Investiga cómo agregar una sombra:
#
# shadow=True
# ============================================================