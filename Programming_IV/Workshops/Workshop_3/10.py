'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Constructores, Destructores y Métodos


TALLER 3

10. Desarrolle una clase `SistemaNotas` para manejar múltiples estudiantes y sus
calificaciones. Implemente métodos para calcular promedios por materia y guardar los
mejores estudiantes en un archivo.
'''

import os
from io import *


class SistemaNotas:
    estudiantes = []

    @classmethod
    def agregar_estudiante(cls, nombre, calificaciones):
        estudiante = {
            "nombre": nombre,
            "calificaciones": calificaciones
        }
        cls.estudiantes.append(estudiante)

    @classmethod
    def promedio_por_materia(cls, materia):
        """
        Calcula el promedio de una materia para todos los estudiantes.
        """
        notas = [est["calificaciones"].get(materia) for est in cls.estudiantes if materia in est["calificaciones"]]
        if notas:
            return sum(notas) / len(notas)
        return 0

    @classmethod
    def mejores_estudiantes(cls, materia):

        max_nota = -1
        mejores = []
        for est in cls.estudiantes:
            nota = est["calificaciones"].get(materia)
            if nota is not None:
                if nota > max_nota:
                    max_nota = nota
                    mejores = [est]
                elif nota == max_nota:
                    mejores.append(est)
        return mejores

    @classmethod
    def guardar_mejores_estudiantes(cls, materia, archivo):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, f"{archivo}.txt")
        mejores = cls.mejores_estudiantes(materia)
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            for est in mejores:
                f.write(f"Nombre: {est['nombre']}, Nota en {materia}: {est['calificaciones'][materia]}\n")

def ejemplo_de_uso():
    SistemaNotas.agregar_estudiante("Ana", {"Matematicas": 4.5, "Fisica": 4.0})
    SistemaNotas.agregar_estudiante("Luis", {"Matematicas": 4.8, "Fisica": 3.9})
    SistemaNotas.agregar_estudiante("Marta", {"Matematicas": 4.8, "Fisica": 4.7})
    print("Promedio Matematicas:", SistemaNotas.promedio_por_materia("Matematicas"))
    SistemaNotas.guardar_mejores_estudiantes("Matematicas", "mejores_matematicas")

def main():
    ejemplo_de_uso()

main()