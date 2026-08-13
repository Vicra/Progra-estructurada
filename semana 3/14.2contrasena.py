# Define una contraseña:
# 1234
# Solicita al usuario que la ingrese.

# Mientras sea incorrecta:
# Contraseña incorrecta.

# Cuando sea correcta:
# Bienvenido.

contrasena = "1234"

# while <condicion de entrada>

inputContrasena = "" # empty string o cadena vacia

# == es igual?
# != es distinto? es diferente

while inputContrasena != contrasena:
  inputContrasena = input("Ingrese su contrasena: ")

print ("Contrasena correcta. Bienvenido")