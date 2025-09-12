'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Constructores, Destructores y Métodos


TALLER 3

7. Diseñe una clase `AgendaContactos` con atributos como nombre, teléfono, correo y
dirección. Agregue métodos para buscar contactos, eliminar contactos y actualizar
información desde y hacia un archivo.
'''
import os
from io import *

# Noto el cambio de nombres de variables, metodos y funciones en todo el taller desde un par de ejercicios para acá? jajaj simplemente queria
# uniformizar todo, estaba cansado de tener nombres en inglés y otros en español, ademas usted da los nombres en español de los atributos o
# clases entonces marca la pauta (para los ejercicios obvio), en fin solo queria que todo se viera mas uniforme y ordenado.



# Se que si se encapsula la lista de agenda se pueden crear multiples agendas pero decidí seguir la pequeña descripción exacta para hacerlo así
class AgendaContactos:
    agenda = []
    pass
    def __init__(self, nombre: str, telefono: str, correo: str, direccion: str):
        self.nombre: str = nombre
        self.telefono: str = telefono
        self.correo: str = correo
        self.correo: str = correo
        self.direccion: str = direccion
        contacto ={"nombre" : self.nombre, "telefono": self.telefono, "correo": self.correo, "direccion": self.direccion}
        AgendaContactos.agenda.append(contacto)
        pass
    @classmethod
    def buscar_contacto(cls, contacto_a_buscar: str):
        coincidencias = [contacto for contacto in cls.agenda if contacto["nombre"] == contacto_a_buscar]
        return coincidencias
    
    @classmethod
    def eliminar_contacto(cls, contacto_a_borrar: str):
        contacto_a_borrar = contacto_a_borrar.lower().strip()
        cls.agenda = [contacto for contacto in cls.agenda if contacto["nombre"].lower().strip() != contacto_a_borrar]
        # Para actualizar la agenda
        AgendaContactos.guardar_en_archivo()

    @classmethod
    def actualizar_contacto(cls, contacto_a_actualizar: str, telefono=None, correo=None, direccion=None):
        contacto_a_actualizar_lower = contacto_a_actualizar.lower().strip()
        for contacto in cls.agenda:
            if contacto["nombre"].lower().strip() == contacto_a_actualizar_lower:
                # Verificación de que atributos se van a cambiar (cuales son none y cuales no)
                if telefono: contacto["telefono"] = telefono
                if correo: contacto["correo"] = correo
                if direccion: contacto["direccion"] = direccion
                break
        # Para actualizar la agenda
        AgendaContactos.guardar_en_archivo()
    
    @classmethod
    def guardar_en_archivo(cls):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "agenda.txt")
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"Nombre|Telefono|Correo|Direccion\n")
            for contacto in cls.agenda:
                 archivo.write(f"{contacto['nombre']}|{contacto['telefono']}|{contacto['correo']}|{contacto['direccion']}\n")


def ejemplo_de_uso():
    contacto1 = AgendaContactos("Carlos", "12345", "carlos@mail.com", "Calle 17")
    contacto2 = AgendaContactos("Ana", "67890", "ana@mail.com", "Calle 24")
    AgendaContactos.guardar_en_archivo()
    contacto = "Carlos"
    lista_retornada = AgendaContactos.buscar_contacto(contacto)
    print(f"Buscar a {contacto}:")
    for atributo_encontrado in lista_retornada:
        print(f"Contacto: {atributo_encontrado['nombre']}|Telefono: {atributo_encontrado['telefono']}|Correo: {atributo_encontrado['correo']}|Direccion: {atributo_encontrado['direccion']}\n")
    AgendaContactos.actualizar_contacto("Carlos", "31378")
    AgendaContactos.eliminar_contacto("Ana")

def main():
    ejemplo_de_uso()

main()