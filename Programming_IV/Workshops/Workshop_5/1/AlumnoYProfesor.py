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
MODULO 2
'''


from Base import *


# Clase Profesor ------------------------------------------------------------------------------------------------------------------------------

class Profesor(Personal_Universitario):
    def __init__(self, nombre: str, edad: int, genero: str, documento: str, direccion: str, telefono: str, fecha_ingreso: date | str,
                 tipo: str | None, horas_trabajadas: int | None, salario_por_hora: float | None):
        super().__init__(nombre, edad, genero, documento, direccion, telefono, fecha_ingreso)
        self.tipo: str | None = tipo
        if horas_trabajadas is None:
            self.horas_trabajadas: int | None = 0
        else:
            self.horas_trabajadas: int | None = horas_trabajadas
        if horas_trabajadas is None:
            self.salario_por_hora: float | None = 0.0
        else:
            self.salario_por_hora: float | None = salario_por_hora

    def calcular_sueldo(self) -> str:
        '''
        Calcula el sueldo mensual del profesor.
        '''
        sueldo_base = self.horas_trabajadas * self.salario_por_hora
        if self.tipo == "Titular":
            return f"El sueldo del profesor titular {self.nombre} es: {sueldo_base}"
        elif self.tipo == "Adjunto":
            return f"El sueldo del profesor adjunto {self.nombre} es: {sueldo_base * 0.8}"
        elif self.tipo == "Auxiliar":
            return f"El sueldo del profesor auxiliar {self.nombre} es: {sueldo_base * 0.6}"
        return "Tipo de profesor no válido."

    def mostrar_materias(self):
        '''
        Muestra las materias que imparte el profesor.
        '''
        if self.tipo == "Titular":
            return f"Materias impartidas por {self.nombre}: Matemáticas, Física, Química"
        elif self.tipo == "Adjunto":
            return f"Materias impartidas por {self.nombre}: Programación, Bases de Datos"
        elif self.tipo == "Auxiliar":
            return f"Materias impartidas por {self.nombre}: Introducción a la Programación"
        return "No se encontraron materias."
    
    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}, Horas Trabajadas: {self.horas_trabajadas}, Salario por Hora: {self.salario_por_hora}"


class Estudiante(Personal_Universitario):
    def __init__(self, nombre: str, edad: int, genero: str, documento: str, direccion: str, telefono: str, fecha_ingreso: date | str,
                 carrera: str | None, semestre: int | None, promedio: float | None, materias: list[str] | None, estado: str | None):
        super().__init__(nombre, edad, genero, documento, direccion, telefono, fecha_ingreso)
        self.carrera: str | None = carrera
        self.semestre: int | None = semestre
        self.promedio: float | None = promedio
        self.materias: list[str] | None = materias
        if estado is None:
            self.estado: str | None = "Activo"
    pass

    def inscribir_materia(self, materia: str):
        '''
        Inscribe una materia para el estudiante.
        '''
        materia = materia.strip().lower()
        if self.materias is None:
            self.materias = []
        elif self.materias is not None and materia in self.materias:
            return f"El estudiante {self.nombre} ya está inscrito en la materia {materia}."
        else:
            self.materias.append(materia)
            return f"Materia {materia} inscrita para {self.nombre}."
    
    def mostrar_materias(self):
        '''
        Muestra las materias inscritas del estudiante.
        '''
        if self.materias:
            return f"Materias inscritas por {self.nombre}: {', '.join(self.materias)}"
        return f"{self.nombre} no tiene materias inscritas."
    
    def cancelar_materia(self, materia: str):
        '''
        Cancela una materia inscrita del estudiante.
        '''
        if self.materias and materia in self.materias:
            self.materias.remove(materia)
            return f"Materia {materia} cancelada para {self.nombre}."
        return f"El estudiante {self.nombre} no está inscrito en la materia {materia}."
    def __str__(self):
        return super().__str__() + f", Carrera: {self.carrera}, Semestre: {self.semestre}, Promedio: {self.promedio}, Estado: {self.estado}"
# Test
if __name__ == "__main__":
    profesor1 = Profesor(
        nombre="Ana Gómez",
        edad=45,
        genero="Femenino",
        documento="987654321",
        direccion="Calle 456, Ciudad",
        telefono="3216549870",
        fecha_ingreso="2015-03-20",
        tipo="Titular",
        horas_trabajadas=40,
        salario_por_hora=30.0
    )

    print(profesor1.calcular_sueldo())
    print(profesor1.mostrar_materias())
    print(profesor1.calcular_antiguedad())

    estudiante1 = Estudiante(
        nombre="Luis Pérez",
        edad=20,
        genero="Masculino",
        documento="123123123",
        direccion="Calle 789, Ciudad",
        telefono="4564564560",
        fecha_ingreso="2022-01-15",
        carrera="Ingeniería de Sistemas",
        semestre=4,
        promedio=4.5,
        materias=None,
        estado="Activo"
    )

    print(estudiante1.calcular_antiguedad())
    print(estudiante1.mostrar_materias())
    print(estudiante1.inscribir_materia("Programación IV"))
    print(estudiante1.mostrar_materias())

    print