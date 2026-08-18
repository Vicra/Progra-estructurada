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
# 1. Ver alumnos
# 2. Agregar alumno
# 3. Eliminar alumno
# 4. Agregar una calificacion
  # Solicitar/Seleccionar el alumno al que se le agregara la nota
  # Solicitar la calificacion
  #
# 5. Ver Promedio de un Alumno
# 0. Salir

# do-while
while True:
  print("")
  print("MENU")
  print("1. Ver alumnos")
  print("2. Agregar alumno")
  print("3. Eliminar alumno")
  print("4. Agregar una calificacion")
  print("5. Mostrar Promedio")
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
    case 4:
      # 1er paso: Mostrar la lista de alumnos para seleccionar uno
      print("")
      print("AGREGAR CALIFICACION - STUDENTS")
      for i in range(len(students)):
        print(
          "Account:",
          students[i].account, 
          students[i].name, 
          students[i].email
        )
      accountInput = input("Ingrese el numero de cuenta del alumno al que le ingresara una calificacion: ")

      # 2do paso: Mostrar e indicar la seccion a asignarle una calificacion
      print("")
      print("SECCIONES")
      for i in range(len(sections)):
        print(sections[i].sectionId, sections[i].className)

      seccionIdInput = int(input("Ingrese el id de la seccion: "))

      # 3er paso: indicar una calificacion
      calificacion = float(input("Ingrese la calificacion: "))

      # 4 paso: Encontrar el nombre de la clase en base al section id
      nombreClase = ""
      for i in range(len(sections)):
        if sections[i].sectionId == seccionIdInput:
          # encontre la clase, actualizar nombre de clase
          nombreClase = sections[i].className

          # no es necesario seguir iterando si ya lo encontre
          break


      # 5 paso: Seleccionar un alumno para ingresarle una nueva calificacion
      for i in range(len(students)):
        if students[i].account == accountInput:
          students[i].grades.append(
            StudentGrade(
              seccionIdInput, nombreClase, calificacion
            )
          )
      # 6 paso: mostrar todas las calificaciones de ese estudiante
      # iterar sobre cada estudiante
      for i in range(len(students)):
        if students[i].account == accountInput:
          # iterar sobre las calificacion de ese estudiante
          print("")
          print("CALIFICACIONES DE: ", students[i].name)
          for j in range(len(students[i].grades)):
            print(
              students[i].grades[j].className, 
              students[i].grades[j].grade
            )
    case 5:
      print("")
      print("MOSTRAR PROMEDIO")

      accountInput = input("Ingrese numero de cuenta del alumno que quiere ver el promedio:")

      for i in range(len(students)):
        if students[i].account == accountInput:
          promedio = 0
          for j in range(len(students[i].grades)):
            promedio = promedio + students[i].grades[j].grade
          promedio = promedio / len(students[i].grades)

      print("")
      print("El promedio de ", students[i].name, "es de", promedio)
    case 0:
      break
    case _:
      print("Opcion invalida")