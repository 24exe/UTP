class Estudiante:
    def __init__(self,nombre,edad,programa="Ingenieria"): # 'programa' es un parametro con valor por defecto por si no se pasa 
        self.nombre=nombre
        self.edad=edad
        self.programa=programa
    def mostrarDatos(self):
        print(f"nombre: {self.nombre} edad: {self.edad} programa: {self.programa}")

pepito=Estudiante("pepito",100,"Medicina")
pepito.mostrarDatos()