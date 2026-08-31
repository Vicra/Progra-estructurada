# ============================================================
# EJERCICIO 4: SCATTER PLOT
# Nivel: Intermedio
# Objetivo: Aprender a visualizar relaciones entre dos variables
# ============================================================

from matplotlib import pyplot as plt

# Horas de estudio
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]

# Calificaciones obtenidas
grades = [50, 55, 60, 65, 70, 75, 82, 90]

# Crear gráfico de dispersión
plt.scatter(study_hours, grades)

# Título
plt.title("Horas de estudio vs Calificación")

# Eje X
plt.xlabel("Horas de estudio")

# Eje Y
plt.ylabel("Calificación")

# Mostrar gráfico
plt.show()


# ------------------------------------------------------------
# EJERCICIO
# ------------------------------------------------------------
# 1. Agrega más estudiantes.
# 2. Cambia las horas de estudio.
# 3. Cambia las calificaciones.
# 4. Investiga cómo modificar el tamaño de los puntos:
#
# plt.scatter(
#     study_hours,
#     grades,
#     s=100
# )
#
# 5. Investiga cómo modificar la transparencia:
#
# alpha=0.5
#
# 6. Intenta crear dos grupos de estudiantes
#    utilizando dos llamadas diferentes a scatter().
# ============================================================