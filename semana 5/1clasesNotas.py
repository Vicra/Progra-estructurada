# Sistema de Calificaciones
# Gestionar Alumnos (Ver, Crear, Eliminar)
# Agregar calificaciones por clase por alumnos
# Ver el promedio (de graduacion) del alumno
  # no incluye secciones reprobadas

class Section:
  def __init__(self, sectionId, className):
    self.sectionId = sectionId
    self.className = className

class StudentGrade:
  def __init__(self, sectionId, className, grade):
    self.sectionId = sectionId
    self.className = className
    self.grade = grade

class Student :
  def __init__(self, account, name, email):
    self.account = account
    self.name = name
    self.email = email
    self.grades = []

# accountInput = 125
students = [
  Student("123", "Jorge Paz", "jorge.paz@unitec.edu"),
  Student("124", "Paris Rodas", "paris.rodas@unitec.edu"),
  Student("125", "Alba Mena", "alba.mena@unitec.edu")
]

sections = [
  Section(1, "Programacion Estructurada"),
  Section(2, "Programacion Estructurada"),
  Section(3, "Intro al Algebra"),
  Section(4, "Comunicacion Oral y Escrita")
]

# MENU
# 1. ver alumnos
# 2. agregar alumno
# 3. eliminar alumno
# 4. agregar una calificacion
# 0. Salir

# do-while
while True:
  print("")
  print("MENU")
  print("1. Ver alumnos")
  print("2. Agregar alumno")
  print("3. Eliminar alumno")
  print("4. Agregar una calificacion")
  print("0. Salir")

  opcion = int(input("Ingrese una opcion: "))

  match opcion:
    case 1:
      print("")
      print("ESTUDIANTES")
      for i in range(len(students)):
        print(i+1, 
          students[i].name, 
          students[i].account, 
          students[i].email
        )
    case 2:
      print("")
      print("AGREGAR UN ALUMNO")
      name = input("Ingrese el nombre: ")
      account = input("Ingrese el numero de cuenta: ")
      email = input("Ingrese el numero de email: ")

      # validations
      # 1. Email is unique (DONE)
      # 2. Account number is unique (PENDING)

      isEmailFound = False
      for i in range(len(students)):
        if students[i].email == email:
          isEmailFound = True

      if isEmailFound == True:
        print ("User email already exists, did not add user")
      else:
        students.append(Student(account, name, email))
        print("User added...")

    case 3:
      print("")
      print("ELIMINAR UN ALUMNO")
      for i in range(len(students)):
        print(
          "Account:",
          students[i].account, 
          students[i].name, 
          students[i].email
        )
      accountInput = input("Ingrese el numero de cuenta del alumno a eliminar: ")

      indiceABorrar = -1
      for i in range(len(students)):
        if students[i].account == accountInput:
          # reasignar el indice del que quiero borrar
          indiceABorrar = i
          break

      if indiceABorrar != -1:
        students.pop(indiceABorrar)

    case 0:
      break
    case _:
      print("Opcion invalida")