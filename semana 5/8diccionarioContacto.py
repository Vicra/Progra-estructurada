# ==========================================
# EJERCICIO: AGENDA DE CONTACTOS
# ==========================================

# Crear un diccionario con los datos de una persona.

# 1. Mostrar el nombre
# 2. Mostrar el teléfono
# 3. Cambiar el número de teléfono
# 4. Agregar una nueva clave/llave
# 5. Mostrar todas las claves/llave
# 6. Mostrar las claves y valores

persona = {
  "nombre": "Carlos",
  "telefono": "1234567890",
  "direccion": "Barrio Rio de Piedras",
  # edad, genero, estatura, peso
}

print("Nombre: ", persona["nombre"])
print("Tel: ", persona["telefono"])
persona["telefono"] = 987654321
print("Nuevo telefono: ", persona["telefono"])

persona["edad"] = 50

print("Edad: ", persona["edad"])

print("\n-----KEYS____")
for key in persona.keys():
  print(key)

print("\nLLAVES Y VALORES")
for key, value in persona.items():
  print(key, ":", value)
