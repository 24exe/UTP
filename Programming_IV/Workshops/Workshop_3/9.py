'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Constructores, Destructores y Métodos


TALLER 3

9. Diseñe una clase `Empresa` que maneje empleados, sus salarios, bonificaciones y
descuentos. Incluya métodos para generar reportes en archivos separados por
departamentos.
'''
import os
from io import *


class Empresa:
    empleados = []

    def ingresar_datos(self, nombre, departamento, salario, bonificacion=0, descuento=0):
        self.nombre = nombre
        self.departamento = departamento
        self.salario = salario
        self.bonificacion = bonificacion
        self.descuento = descuento
        empleado = {
            "nombre": self.nombre,
            "departamento": self.departamento,
            "salario": self.salario,
            "bonificacion": self.bonificacion,
            "descuento": self.descuento
        }
        Empresa.empleados.append(empleado)

    @classmethod
    def calcular_salario_final(cls, empleado):
        return empleado["salario"] + empleado["bonificacion"] - empleado["descuento"]

    @classmethod
    def generar_reportes_por_departamento(cls):
        departamentos = {}
        for emp in cls.empleados:
            depto = emp["departamento"]
            if depto not in departamentos:
                departamentos[depto] = []
            departamentos[depto].append(emp)
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        for depto, empleados in departamentos.items():
            ruta_archivo = os.path.join(ruta_actual, f"reporte_{depto}.txt")
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                for emp in empleados:
                    salario_final = cls.calcular_salario_final(emp)
                    f.write(f"Nombre: {emp['nombre']}, Salario Base: {emp['salario']}, Bonificación: {emp['bonificacion']}, Descuento: {emp['descuento']}, Salario Final: {salario_final}\n")

def ejemplo_de_uso():
    empleado1 = Empresa()
    empleado1.ingresar_datos("Ana", "Ventas", 2000, 200, 50)
    empleado2 = Empresa()
    empleado2.ingresar_datos("Luis", "Ventas", 1800, 150, 30)
    empleado3 = Empresa()
    empleado3.ingresar_datos("Marta", "TI", 2500, 300, 100)
    Empresa.generar_reportes_por_departamento()

def main():
    ejemplo_de_uso()

main()
