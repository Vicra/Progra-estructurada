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

while True:
  # 1. solicitar input de teclado de la contrasena
  inputContrasena = input("Ingrese su contrasena: ")

  # 2. comparar contrasenas
  if inputContrasena == contrasena:
    print ("Contrasena correcta")
    break
  else:
    print("Contrasena incorrecta, intente de nuevo")
  
  # 3. si es correcta, termina el ciclo

  # 4. si es incorrecta, se repite el ciclo