from matplotlib import pyplot as plt

yvalues = []

print("VENTAS POR DIA")
print("INGRESE LOS VALORES DE Y")
for i in range(5):
  yvalues.append(
    int(
      input(f"Ingrese el valor de x en indice {i+1}:")
    )
  )
print("VALORES DE X", yvalues)

xvalues = ["Lunes",
           "Martes",
           "Mierc",
           "Jueves",
           "Viernes"]

plt.plot(xvalues, yvalues, linestyle="--" ,marker="*")
plt.show()