def sum(a, b):
  return a + b

# Methods = Functions (Actions)

# def <nombreDeLaFuncion> (lista de params separados por coma):
  # codigo
  # return <variable>

# Nombre de Funcion: debe de tener la prima palabra verbo en infinitivo

print("La suma de 10 y 15 es:", sum(10, 15))


class Dog:
  # method/function constructor
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  # make sound
  def makeSound(self):
    print(self.name, "dice: Woof")

  def showInfo(self):
    print("")
    print("Name: ", self.name)
    print("Breed: ", self.breed)
    print("Age: ", self.age)

coco = Dog(
  "Coco",
  "Terrier",
  14
)

coco.makeSound()

tinky = Dog(
  "Tinky",
  "Mixed",
  10
)

tinky.makeSound()

coco.showInfo()
tinky.showInfo()
