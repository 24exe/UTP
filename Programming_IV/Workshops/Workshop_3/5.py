'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Constructores, Destructores y Métodos


TALLER 3

5. Cree una clase `Encuesta` que almacene respuestas de usuarios (edad, género,
ciudad, opinión). Guarde cada respuesta en un archivo distinto por ciudad. Muestre
estadísticas por género.
'''
import os

class Encuesta:
    def __init__(self):
        self.respuestas = []  # aquí se guardan todas las respuestas temporalmente

    def agregar_respuesta(self, edad, genero, ciudad, opinion):
        respuesta = {"edad": edad, "genero": genero, "ciudad": ciudad, "opinion": opinion}
        self.respuestas.append(respuesta)
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, f"{ciudad}.txt")

        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"{edad}|{genero}|{ciudad}|{opinion}\n")

    def mostrar_estadisticas_genero(self):
        estadisticas = {"Masculino": 0, "Femenino": 0, "Otro": 0}

        for respuesta in self.respuestas:
            genero = respuesta["genero"].strip().capitalize()
            if genero in estadisticas:
                estadisticas[genero] += 1
            else:
                estadisticas["Otro"] += 1

        print("Estadísticas por género:")
        for g, c in estadisticas.items():
            print(f"{g}: {c} respuestas")



# No quice alargarlo mas como en los anteriores
def example():
    encuesta = Encuesta()
    # Agregar respuestas
    encuesta.agregar_respuesta(25, "Masculino", "Bogota", "Muy buena experiencia")
    encuesta.agregar_respuesta(30, "Femenino", "Medellin", "Podría mejorar")
    encuesta.agregar_respuesta(22, "Otro", "Bogota", "Me gustó bastante")
    encuesta.agregar_respuesta(18, "Femenino", "Medellin", "No me gusto nada")

    # Mostrar estadísticas
    encuesta.mostrar_estadisticas_genero()

# FUN. PRINCIPAL
def main():
    example()

main()

