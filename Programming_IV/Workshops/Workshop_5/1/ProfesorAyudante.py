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
MODULO 3
'''

from AlumnoYProfesor import *



# Clase Profesor Ayudante ------------------------------------------------------------------------------------------------------------------------------

class Profesor_Ayudante(Estudiante, Profesor):
    def __init__(self, nombre: str, edad: int, genero: str, documento: str, direccion: str, telefono: str, fecha_ingreso: date | str,
                 tipo: str | None, horas_trabajadas: int | None, salario_por_hora: float | None,
                 carrera: str | None, semestre_actual: int | None, promedio_acumulado: float | None):
        Estudiante.__init__(self, nombre, edad, genero, documento, direccion, telefono, fecha_ingreso,
                            carrera, semestre_actual, promedio_acumulado)
        Profesor.__init__(self, nombre, edad, genero, documento, direccion, telefono, fecha_ingreso,
                         tipo, 20, 15.0)
        
    def materias_de_ayuda(self):
        '''
        Muestra las materias que puede ayudar el profesor ayudante según su tipo.
        '''
        if self.tipo == "Ayudante":
            materias = ["Programación I", "Introducción a la Informática", "Matemáticas Básicas"]
        elif self.tipo == "Asistente":
            materias = ["Estructuras de Datos", "Programación II ", "Gramáticas y Lenguajes Formales"]
        else:
            materias = []
        print(f"El profesor ayudante {self.nombre} puede ayudar en las siguientes materias: {', '.join(materias)}")
