# ============================================================
# EJERCICIO 1: GRÁFICO DE LÍNEAS
# ============================================================

# Matplotlib es una librería para crear gráficos en Python.
from matplotlib import pyplot as plt

# puntos en x
# puntos en y

xvalues = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SAB", "DOM"] # dias de la semana
yvalues = [10.5, 13.2, 13.1, 17.7, 14.3, 12.3, 15] # ventas por dia (en dolares)

plt.plot(xvalues, yvalues, linestyle="--", marker="*", color="#BA07F0")

plt.bar(xvalues, yvalues, color="pink")
# plt.bar(xvalues, yvalues)

# configurar los label
plt.xlabel("DIAS DE LA SEMANA", color="blue")

plt.ylabel("VENTAS EN DOLARES")

plt.title("VENTAS SEMANALES DE EMPLEADO: Dr. Doom", color="orange", fontweight="bold", fontstyle="oblique")

# la ultima instruccion siempre
plt.show()


# ------------------------------------------------------------
# EJERCICIO
# ------------------------------------------------------------
# 1. Cambia los valores de x_values.
# 2. Cambia los valores de y_values.
# 3. Cambia el título.
# 4. Agrega más puntos.
# 5. Prueba diferentes estilos de línea:
#
# plt.plot(x_values, y_values, linestyle="--")  USAR ESTE
# plt.plot(x_values, y_values, linestyle=":")
#
# 6. Agrega marcadores:
#
# plt.plot(x_values, y_values, marker="o")
#
# Prueba otros marcadores:
# "s" = cuadrado
# "^" = triángulo
# "*" = estrella  USAR ESTE
# ============================================================