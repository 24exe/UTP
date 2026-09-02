import random
import string
import uuid

def generar_id_unico():
    return str(uuid.uuid4())[:8]


class Persona:
    def __init__(self, nombre:str, documento: int, edad: int, genero: str = "No especificado"):
        self._nombre: str = nombre
        self._documento: int = documento
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
    
    @property
    def documento(self) -> int:
        return self._documento
    
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
    
    @documento.setter
    def documento(self, documento: int):
        self._documento = documento
    
    def __str__(self):
                return f"""
========= Información del Usuario =========
Nombre: {self.nombre}
Documento: {self.documento}
ID: {self.id}
Edad: {self.edad}
Género: {self.genero}
===========================================
"""
# Test del módulo

if __name__ == "__main__":
    persona1 = Persona("Ana", 12345678, 28, "Femenino")
    persona2 = Persona("Luis", 87654321, 35)

    print(persona1)
    print(persona2)