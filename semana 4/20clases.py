class Fruit:
  # constructor
  # name and color are parameters
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def rot():
    print("rotting...")

apple = Fruit("manzana gala", "red")
greenApple = Fruit("manzana verde", "verde")
f1 = Fruit("sandia", "verde")
f2 = Fruit("mango", "verde")
f3 = Fruit("mango", "camulean")
f4 = Fruit("mango", "jade")

fruits = [f1, f2, f3, f4]

for i in range(len(fruits)):
  print(fruits[i].name, fruits[i].color)
