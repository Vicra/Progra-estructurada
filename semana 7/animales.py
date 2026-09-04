# Programacion Orientada a Objetos POO

# Ejercicio de Gestion de Granja
import random

class Animal:
  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed

  # polimorfismo
  def makeSound(self):
    print("Hacer sonido")

  def sleep(self):
    print(self.name + " sleeping...")

# Herencia
class Dog(Animal):
  def makeSound(self):
    print(self.name + " dice: Woof")

class Cat(Animal):
  def makeSound(self):
    if self.name == "Garfield":
      print(self.name + " dice: bye")
    else:
      print(self.name + " dice: Miau!")

class Cow(Animal):
  def makeSound(self):
    print(self.name+" dice: Muuu!")

class Chicken(Animal):
  def layEggs(self, amount):
    print(self.name + " layed " + amount + " eggs")

animales = [
  Dog("Tinky", 12, "Avocado"),
  Dog("Raider", 7, "German Shepard"),
  Cat("Enrique", 6, "Egipcio"),
  Cat("Garfield", 3, "Naranja"),
  Cow("Alejo", 4, "Savana"),
  Chicken("Maria", 2, "Blanca"),
  Chicken("Chunga", 1, "India"),
  Chicken("Terca", 3, "Peluda")
]

def mostrar_animales():
  print("")
  for animal in animales:
    print(
      "Nombre:", animal.name, "Edad:", animal.age, "Raza:", animal.breed)

def dia_animales():
  for animal in animales:
    animal.makeSound()

  print("\nAL FINAL DEL DIA")
  for animal in animales:
    animal.sleep()

  for animal in animales:
    if isinstance(animal, Chicken):
      animal.layEggs(str(random.randint(0, 5)))

dia_animales()