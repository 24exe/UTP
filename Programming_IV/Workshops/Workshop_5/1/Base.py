'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Herencia múltiple.


TALLER 5

Para el siguiente grafico diseñe un algoritmo implementando herencia
múltiple:
    a. Para cada clase debe diseñar al menos 6 atributos.
    b. Para las clases profesor debe realizar un método en donde se pueda
    calcular el sueldo mensual dependiendo de las horas que trabaja y del
    tipo de profesor que sea
    c. Debe de crear un método para calcular la antigüedad de todas las
    entidades en el diseño.
    d. Dependiendo de cada tipo de profesor debe diseñar al menos tres
    materias acordes con el rango de cada uno y se deben visualizar en
    pantalla por medio de un método.
    e. Guarde la información que crea necesaria en un archivo para este
    programa.
'''





'''
MODULO 1
'''

from datetime import *


# Clase Base ------------------------------------------------------------------------------------------------------------------------------
class Personal_Universitario:
    def __init__(self, nombre: str, edad: int, genero: str, documento: str, direccion: str, telefono: str, fecha_ingreso: date | str):
        self.nombre: str = nombre
        self.edad: int = edad
        self.genero: str = genero
        self.documento: str = documento
        self.direccion: str = direccion
        self.telefono: str = telefono
        self.fecha_ingreso: date = self.convertir_a_fecha(fecha_ingreso)

    def convertir_a_fecha(self, fecha: date | str) -> date:
        '''
        Convierte una cadena en formato "YYYY-MM-DD" a un objeto date.
        Si ya es un objeto date, lo retorna tal cual.
        '''
        if isinstance(fecha, str):
            return datetime.strptime(fecha.strip(), "%Y-%m-%d").date()
        return fecha
    
    def calcular_antiguedad(self) -> int:
        '''
        Calcula la antigüedad en años del personal universitario.
        '''
        fecha_actual = date.today()
        antiguedad = fecha_actual.year - self.fecha_ingreso.year - ((fecha_actual.month, fecha_actual.day) < (self.fecha_ingreso.month, self.fecha_ingreso.day))
        return f"Antigüedad: {antiguedad} años"
    

    def __str__(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Documento: {self.documento}, "
                f"Dirección: {self.direccion}, Teléfono: {self.telefono}, Fecha de Ingreso: {self.fecha_ingreso}")