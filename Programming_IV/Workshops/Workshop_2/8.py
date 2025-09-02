'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Archivos, clases y objetos.

TALLER 2

8. Agenda de eventos
- Crea una clase `Evento` con atributos: título, fecha, hora, lugar y responsable.
- Permita registrar varios eventos y guardarlos en `agenda.txt`.
- Implemente un método que lea el archivo y muestre solo los eventos programados
para la próxima semana.
'''
from io import *
import os
from datetime import datetime, timedelta

class Evento:
    titulo: str
    fecha: str
    hora: str
    lugar: str
    responsable: str

    def InsertData(self):
        self.titulo = input("Título: ")
        self.fecha = input("Fecha (YYYY-MM-DD): ")
        self.hora = input("Hora (HH:MM): ")
        self.lugar = input("Lugar: ")
        self.responsable = input("Responsable: ")
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "agenda.txt")
        with open(ruta_archivo, "a", encoding="utf-8") as f:
            f.write(f"{self.titulo}|{self.fecha}|{self.hora}|{self.lugar}|{self.responsable}\n")

    @staticmethod
    def mostrarEventosProximaSemana():
        hoy = datetime.now().date()
        proxima_semana = hoy + timedelta(days=7)
        if not os.path.exists("agenda.txt"):
            print("No hay eventos registrados.")
            return
        with open("agenda.txt", "r", encoding="utf-8") as archivo:
            print("Eventos para la próxima semana:")
            for linea in archivo:
                partes = linea.strip().split("|")
                if len(partes) == 5:
                    fecha_evento = datetime.strptime(partes[1], "%Y-%m-%d").date()
                    if hoy < fecha_evento <= proxima_semana:
                        print(f"Título: {partes[0]}, Fecha: {partes[1]}, Hora: {partes[2]}, Lugar: {partes[3]}, Responsable: {partes[4]}")


# Crear y registrar varios eventos
eventos = []
for i in range(3):
    print(f"\nEvento {i+1}:")
    evento = Evento()
    evento.InsertData()
    eventos.append(evento)

# Mostrar los eventos programados para la próxima semana
Evento.mostrarEventosProximaSemana()
