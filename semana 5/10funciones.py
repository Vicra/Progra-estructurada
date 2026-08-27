#1. funcion sencilla sin parametros saludar
def saludar():
  print("Hola Primero")

print("\nEJERCICIO 1")
saludar()
saludar()
saludar()

#2. funcion saludar con un parametro
def saludarA(nombre):
  print("Hola, ", nombre)

print("\nEJERCICIO 2")
saludarA("Alba")
saludarA("Paris")
saludarA("Jorge")

#3. funcion sumar (2 parametros)
print("\nEJERCICIO 3")
def sum(a, b):
  c = a + b
  print("Resultado:", c)

sum(6,7)
sum(100, 1)
sum(13, 6)

#3.5 Sumar con valor de retorno
def sumAndReturn(a, b):
  return a + b

n1 = sumAndReturn(10, 15)
# n1 = 25
n2 = sumAndReturn(100, 150)
# n1 = 250

print("\nEJERCICIO 3.5")
print("n1:", n1)
print("n2:", n2)

print("Suma y retorna concatenado:", 
  sumAndReturn(3,3) + sumAndReturn(6,6))

s = sumAndReturn(3,3) + sumAndReturn(6,6)
print("Suma y retorna concatenado:",s)

#4. funcion es mayor de edad
def es_mayor_de_edad(edad):
  if edad >= 18:
    print("Es mayor de edad")
  else:
    print("NO es mayor de edad")

print("\nEJERCICIO 4")
es_mayor_de_edad(17)
es_mayor_de_edad(20)
es_mayor_de_edad(5)

def es_mayor_de_edad_bool(edad):
  if edad >= 18:
    return True
  else:
    return False

print("\nEJERCICIO 4.5")
print(es_mayor_de_edad_bool(17))
print(es_mayor_de_edad_bool(20))
print(es_mayor_de_edad_bool(5))

miEdad = int(input("Ingresa tu edad:"))
if es_mayor_de_edad_bool(miEdad):
  print("Bienvenido")
else:
  print("No se puede registrar al curso")

#5. funcion contar numeros pares
# numbers = [1,3,4,6,7,8,0,10]
def countPairs(numbers):
  pairs = 0
  for i in range(len(numbers)):
    if numbers[i]%2 == 0:
      print("Adding pairs:", 
            pairs, "+ numbers[", i, "]",
             numbers[i])
      pairs = pairs + numbers[i]
  print("Suma de pairs:", pairs)
  return pairs

numbers = [1,3,4,6,7,8,0,10]
sumaDePares = countPairs(numbers)

print("\nSUMA DE PARES: ", sumaDePares)

#6. funcion numero mayor
#7. funcion buscar estudiante y retornar calificacion en diccionario
#8. sistema de operaciones (calculadora)


