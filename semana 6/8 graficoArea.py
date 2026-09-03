# EJERCICIO 8: GRÁFICO DE ÁREA


from matplotlib import pyplot as plt

# Meses
months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]

# Visitantes de un sitio web
visitors = [100, 150, 180, 250, 300, 400]

# Crear gráfico de área
plt.fill_between(
    months,
    visitors,
    alpha=0.5
)

# También podemos dibujar la línea
plt.plot(
    months,
    visitors,
    marker="o"
)

# Título
plt.title("Visitas al sitio web")

# Etiquetas
plt.xlabel("Mes")
plt.ylabel("Visitantes")

# Mostrar gráfico
plt.show()
