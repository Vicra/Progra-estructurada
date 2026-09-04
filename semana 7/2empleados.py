# Utilizando herencia y polimorfismo, crear una clase Empleado y EmpleadoVentas que permita
# Calcular un salario con comisiones (EmpleadoVentas)
# Calcular un salario con bonificacion (Gerente)
# Calcular un salario con horas extras (Tecnico)

# Que cosas comparten?
# salario, nombre

# 1. Crear clase Base/Padre (Empleado)
class Empleado:
  # constructor
  def __init__(self, salarioBase, nombre):
    self.salarioBase = salarioBase
    self.nombre = nombre

  # Regresa el salario final con bonificacion, hrs extras o comisiones
  def calcular_salario(self):
    return self.salarioBase

# (Empleado) permite heredar todos los atributos de Empleado
# Empleado es mi padre, super() significa acceder a mi padre
class EmpleadoVentas(Empleado):
  # redefinir la function de calcular_salario
  # este empleado percibe comisiones

  # nuevo constructor
  def __init__(self, salarioBase, nombre, ventasTotales, indicadorComision):
    super().__init__(salarioBase, nombre)
    self.ventasTotales = ventasTotales 
    self.indicadorComision = indicadorComision

  # salarioTotal = salarioBase + comisiones
  def calcular_salario(self):
    return self.salarioBase + (self.ventasTotales * (self.indicadorComision/100))

# clase Empleado Tecnico salarioBase + hrs extra
class EmpleadoTecnico(Empleado):
  def __init__(self, salarioBase, nombre, cantidadHrsExtra, salarioPorHraExtra):
    super().__init__(salarioBase, nombre)
    self.cantidadHrsExtra = cantidadHrsExtra
    self.salarioPorHraExtra = salarioPorHraExtra

  def calcular_salario(self):
    return (self.cantidadHrsExtra * self.salarioPorHraExtra) + self.salarioBase

class EmpleadoGerente(Empleado):
  # el gerente tiene una bonificacion estatica
  def __init__(self, salarioBase, nombre, bonificacion):
      super().__init__(salarioBase, nombre)
      self.bonificacion = bonificacion

  def calcular_salario(self):
    return self.salarioBase + self.bonificacion

# ----- EMPLEADOS DE VENTAS -----------
empleado1 = EmpleadoVentas(13000, "Victor", 20000, 10)
empleado2 = EmpleadoVentas(12500, "Ricardo", 15000, 10)
# print("Salario Total de " 
#   + empleado1.nombre 
#   + " es :" 
#   + str(empleado1.calcular_salario())
# )
# print("Salario Total de " 
#   + empleado2.nombre 
#   + " es :" 
#   + str(empleado2.calcular_salario())
# )

# ----- EMPLEADOS TECNICOS -----------
empleado3 = EmpleadoTecnico(11000, "Jose", 12, 80)
# print("Salario Total de " 
#   + empleado3.nombre 
#   + " es :" 
#   + str(empleado3.calcular_salario())
# )

empleado4 = EmpleadoTecnico(12250, "Juan", 13, 85)
# print("Salario Total de " 
#   + empleado4.nombre 
#   + " es :" 
#   + str(empleado4.calcular_salario())
# )

# ----- EMPLEADOS GERENTE -----------
empleado5 = EmpleadoGerente(20000, "Josue", 5000)
# print("Salario Total de " 
#   + empleado5.nombre 
#   + " es :" 
#   + str(empleado5.calcular_salario())
# )


# LISTA DE EMPLEADOS
empleados = [
  empleado1, 
  empleado2,
  empleado3,
  empleado4,
  empleado5,
]

for empleado in empleados:
  print("Empleado:" + empleado.nombre)
  print("Salario Total: L." + str(empleado.calcular_salario()))
  print("-----------------")