# Solicita al usuario su calificación.
# Reglas:
# •	65 o más → Aprobado
# •	Menor que 65 → Reprobado

calificacion = float(input("Ingrese su calificacion: "))

if calificacion > 100 or calificacion < 0:
  print("Calificacion invalida")
elif calificacion >= 65:
  print("Curso Aprobado")
  print("Exitos en tu proxima clase")
else:
  print("Curso Reprobado")
  print("Suerte a la proxima")