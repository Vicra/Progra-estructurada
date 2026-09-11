import csv
from pathlib import Path

ARCHIVO = "estudiantes.csv"

def leer_estudiantes():

    with open(Path(__file__).with_name(ARCHIVO), 
    "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        estudiantes = []

        for estudiante in lector:
            estudiantes.append(estudiante)

    return estudiantes


def agregar_estudiante(estudiante):

    campos = [
        "id",
        "nombre",
        "edad",
        "curso",
        "nota"
    ]

    with open(Path(__file__).with_name(ARCHIVO), 
        "a", newline="", enqcoding="utf-8") as archivo:

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        escritor.writerow(estudiante)