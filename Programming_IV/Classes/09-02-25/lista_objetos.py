#crear una lista de objetos y luego imprimir los objetos

class Estudiante:
    def __init__(self,nombre,edad,telefono):
        self.nombre=nombre
        self.edad=edad
        self.telefono=telefono
    def __str__(self):
        return f"nombre:{self.nombre}"
    def __len__(self):
        return len(self.nombre)+len(self.edad)+len(self.telefono)


def ingreso_lista(): 
    lista_estudiante=[]     
    while True:
        nombre=input("ingrese el nombre: ")
        edad=int(input("ingrese la edad: "))
        telefono=int(input("ingrese el telefono:"))
        estudiante=Estudiante(nombre,edad,telefono)
        lista_estudiante.append(estudiante)
        pregunta=input("¿desea ingresar mas estudiantes?(s/n): ")
        if pregunta=='s':
            pass
        else:
            return lista_estudiante
            
def imprimir_objetos(lista):
    for i in lista:
        print(i)

#imprimir_objetos(ingreso_lista())
pepito=Estudiante("pepito","85","8452")
print(len(pepito))