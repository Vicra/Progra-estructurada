# Sistema de Cursos/talleres

# Tener una lista preexistente de cursos

# 1. Mostrar cursos existentes
# 2. Agregar participantes al curso
      # Ingresar: nombre del participante, email, curso, horario
# 3. Ver Detalle de Participantes por Curso

# Un curso tiene la siguiente informacion: nombre, modalidad(prensencial o virtual), participantes[], cupo

# Validaciones (Al momento de agregar)
# 1. Una persona no se puede inscribir 2 veces en el mismo curso (validacion por email)
# 2. No se puede pasar de la cantidad de incripciones que tiene asignado el curso a traves del cupo (slots)

class Participant:
  def __init__(self, name, schedule,  email):
    self.name = name
    self.email = email
    self.schedule = schedule

class Course:
  def __init__(self, name, type, slots):
    self.name = name
    self.type = type
    self.slots = slots
    self.participants = []


courses = [
  Course("Taller de Python", "Presencial", 5),
  Course("Taller de PSeInt", "Virtual", -1),
]

numeros = [1, 2, 3, 4]

option = -1

while option:
  print("")
  print("MENU")
  print("1. Ver lista de cursos")
  print("2. Agregar participante al curso")
  print("3. Ver detalles de participantes por curso")

  option = int(input("Ingrese una opcion: "))

  match option:
    case 1:
      for i in range(len(courses)):
        print(courses[i].name, courses[i].type, courses[i].slots)
        print ("PARTICIPANTES")
        for j in range(len(courses[i].participants)):
          print("---", courses[i].participants[j].name)

    case 2:
      print("")
      print("AGREGAR PARTICIPANTE")

      nombre = input("Ingrese el nombre del participante: ")
      email = input("Ingrese el email del participante:")

      print("")
      print("CURSOS")
      for i in range(len(courses)):
        print(i+1, courses[i].name, courses[i].type, courses[i].slots)

      curso = int(input("Ingrese el numero de curso:"))
      curso = curso - 1

      horario = input("Ingrese el horario (M o T):")

      courses[curso].participants.append(
        Participant(
          nombre, horario, email
        )
      )



