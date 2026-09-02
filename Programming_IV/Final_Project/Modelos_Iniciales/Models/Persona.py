'''
Modulo 1.1: Final_Project.Clinica.Models.Persona
Descripción: Este módulo define la clase Base Persona
'''

import random
import string


def generar_id_unico(longitud: int = 8) -> str:
    """Genera un ID único compuesto por letras mayúsculas y dígitos."""
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choices(caracteres, k=longitud))
    return codigo


class Persona:
    def __init__(self, nombre: str, edad: int, genero: str = "No especificado"):
        self._nombre: str = nombre
        self._id: str = generar_id_unico()
        self._edad: int = edad
        self._genero: str = genero

    # Getters
    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def id(self) -> str:
        return self._id

    @property
    def edad(self) -> int:
        return self._edad

    @property
    def genero(self) -> str:
        return self._genero
    
    # Setters

    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre 
    
    @edad.setter
    def edad(self, edad: int):
        self._edad = edad
    
    @genero.setter
    def genero(self, genero: str):
        self._genero = genero
    
    def __str__(self):
        return f"==========Información de la Persona==========\nNombre: {self.nombre}\nID: {self.id}\nEdad: {self.edad}\nGénero: {self.genero}\n"
        
# Test del módulo

if __name__ == "__main__":
    persona1 = Persona("Ana", 28, "Femenino")
    persona2 = Persona("Luis", 35)
        
    print(persona1)
    print(persona2)   