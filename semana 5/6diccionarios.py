# DICCIONARIOS en py
# Diccionarios son estructuras de datos que almacenan datos a traves de una llave/clave y un valor

# 1. Crear diccionario
country = {
  "continent": "Europe",
  "language": "French",
  "name": "Belgium",
  "capital": "Brusselss",
  "name": "Belgium",
  "area": 30689 #km2
}

# 2. Mostrar el valor (valores) de una llave del diccionario

# 3. Modificar un valor de una llave del diccionario
print(country["capital"])
country["capital"] = "Bruselas"
print(country["capital"])

# 4. Agregar una nueva clave
country["population"] = 11867634
print(country["population"])

# 5. Mostrar todas las claves/llaves -> .keys()
print("")
print("----KEYS----")
for item in country.keys():
  print(item)

# 6. Mostrar todas los valores -> .values()
print("----VALUES----")
for item in country.values():
  print(item)

# 7. Mostrar todos las llaves y valores -> a,b in items
print("----ITEMS----")
for key, value in country.items():
  print(key, ":", value)
