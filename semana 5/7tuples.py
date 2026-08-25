numeros = [
  "Alba", 
  18,
  "Honduran",
  "F"
]
print(numeros)
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])

# paciente[0] = name
# paciente[1] = age
# paciente[2] = nationality
# paciente[3] = gender

# 1. crear una tupla
paciente = ("Alba", 18, "Honduran", "F")

# 2. mostrar un valor de la tupla
print(paciente[0])
print(paciente[1])
print(paciente[2])
print(paciente[3])

# 3. Crear una lista de tuplas

pacientes = [
  ("Alba", 18, "Honduran", "F"),
  ("Jorge", 19, "Honduran", "M"),
  ("Paris", 20, "Griego", "M")
]
print("")
print("TUPLAS LISTA")

for item in pacientes:
  print("\nName:", item[0])
  print("\\Age:",item[1])
  print("Nationality:",item[2])
  print("Sex:",item[3])