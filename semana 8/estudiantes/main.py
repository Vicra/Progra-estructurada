from archivos import agregar_estudiante
from estudiantes import mostrar_estudiantes
from estudiantes import buscar_estudiante
from estudiantes import promedio_notas


def menu():

    while True:

        print("\n===== ESTUDIANTES =====")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Promedio de notas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            estudiante = {
                "id": input("ID: "),
                "nombre": input("Nombre: "),
                "edad": input("Edad: "),
                "curso": input("Curso: "),
                "nota": input("Nota: ")
            }

            agregar_estudiante(estudiante)

            print("Estudiante agregado.")

        elif opcion == "2":

            mostrar_estudiantes()

        elif opcion == "3":

            id_buscar = input("ID a buscar: ")

            estudiante = buscar_estudiante(id_buscar)

            if estudiante:
                print(estudiante)
            else:
                print("Estudiante no encontrado.")

        elif opcion == "4":

            promedio = promedio_notas()

            print(f"Promedio: {promedio:.2f}")

        elif opcion == "5":

            print("Hasta luego.")
            break

        else:
            print("Opción inválida.")


menu()