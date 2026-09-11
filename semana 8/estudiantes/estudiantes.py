from archivos import leer_estudiantes


def mostrar_estudiantes():

    estudiantes = leer_estudiantes()

    for estudiante in estudiantes:

        print(
            f"{estudiante['id']} - "
            f"{estudiante['nombre']} - "
            f"{estudiante['curso']} - "
            f"{estudiante['nota']}"
        )


def buscar_estudiante(id_buscar):

    estudiantes = leer_estudiantes()

    for estudiante in estudiantes:

        if estudiante["id"] == id_buscar:
            return estudiante

    return None


def promedio_notas():

    estudiantes = leer_estudiantes()

    notas = []

    for estudiante in estudiantes:
        notas.append(float(estudiante["nota"]))

    return sum(notas) / len(notas)