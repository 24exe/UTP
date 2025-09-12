'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Nombre: Rafael Urrea Gaviria
Codigo: 1004737606


Parcial 1

2. Sistema de Gestión de Empleados
Crea una aplicación de gestión de empleados. Debes crear las siguientes clases:
'''
# LIBRERIAS
from io import *
import os
import random
'''
Clase Empleado:

• Atributos:
    o Nombre (cadena de texto)
    o ID (entero)
    o Salario Base (flotante)
    o Años de Experiencia (entero)

• Métodos:
    o Constructor para inicializar todos los atributos. 
    o Un método calcular_salario() que retorne el salario total del empleado. El salario total se calcula sumando un bono al salario 
      base que depende de los años de experiencia:
        ▪ Entre 0 y 2 años: bono de 5% del salario base.
        ▪ Entre 3 y 5 años: bono de 10% del salario base.
        ▪ Más de 5 años: bono de 15% del salario base.
    o Un método para representar al empleado en formato de texto.
'''
class Empleado:
    def __init__(self, nombre: str, id: int, salario_base: float, experiencia: int):
        self.nombre: str = nombre
        self.id: int = id
        self.salario_base: float = salario_base
        self.experiencia: int = experiencia

    def calcular_salario(self):
        if 0 <= self.experiencia <= 2:
            return self.salario_base * 1.05
        elif 3 <= self.experiencia <= 5:
            return self.salario_base * 1.10
        elif self.experiencia > 5:
            return self.salario_base * 1.15
        else:
            print("ERROR\n")
            return self.salario_base
        
    def __str__(self)-> str:
         return f"ID: {self.id}, Nombre: {self.nombre}, Años de experiencia: {self.experiencia}, Salario: ${self.calcular_salario():.2f}" # Dos decimales despues del punto


'''
Clase GestorEmpleados:

• Atributos:
    o Una lista de empleados.

• Métodos:
    o agregar_empleado(empleado: Empleado): Agrega un empleado a la lista.
    o eliminar_empleado(id: int): Elimina un empleado de la lista según su ID.
    o buscar_empleado(id: int): Busca y devuelve un empleado por su ID.
    o editar_empleado(id: int): Busca un empleado y deja editar la informacion que se quiera del empleado, luego se debe actualizar
    el archivo donde esta guardada la información.
    o mostrar_empleados(): Muestra todos los empleados de la lista junto con sus salarios totales.
    o guardar_empleados(archivo: str): Guarda la lista de empleados en un archivo.
    o cargar_empleados(archivo: str): Carga la lista de empleados desde un archivo.

'''

class GestorEmpleados:

    def __init__(self):
        self.empleados: list[Empleado] = []
    
    def agregar_empleado(self, empleado: Empleado):
        self.empleados.append(empleado)
        # Ordenar la lista en orden ascendente a partir del ID de cada empleado
        # Recordar: lambda crea funciones anonimas (sin  nombre), sirve para def
        # funciones rapidas y cortas una linea
        self.empleados.sort(key = lambda empleado: empleado.id)
    
    def eliminar_empleado(self, id: int):
        for empleado in self.empleados:
            if id == empleado.id:
                self.empleados.remove(empleado)
                ids_usados.discard(id)
                return "EMPLEADO BORRADO \n"
        return "EMPLEADO NO ENCONTRADO \n"
            
    def buscar_empleado(self, id: int)-> Empleado:
        for empleado in self.empleados:
            if id == empleado.id:
                return empleado
    
    def editar_empleado(self, id_a_editar: int, nuevo_nombre: str = None, nuevo_salario_base: float = None, nueva_experiencia: int = None):
        for empleado in self.empleados:
            if id_a_editar == empleado.id:
                if nuevo_nombre is not None:
                    empleado.nombre = nuevo_nombre
                if nuevo_salario_base is not None:
                    empleado.salario_base = nuevo_salario_base
                if nueva_experiencia is not None:
                    empleado.experiencia = nueva_experiencia
                return "EMPLEADO EDITADO\n"
        return "EMPLEADO NO ENCONTRADO\n"

    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(empleado)
    
    def guardar_empleados(self, archivo: str):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, f"{archivo}.txt")
        with open(ruta_archivo, "w", encoding = "utf-8") as archivo_a_escribir:
            archivo_a_escribir.write("ID|Nombre|Salario Base|Años de Experiencia|Salario Total\n")
            for empleado in self.empleados:
                archivo_a_escribir.write(f"{empleado.id}|{empleado.nombre}|{empleado.salario_base}|{empleado.experiencia}|{empleado.calcular_salario():.2f}\n")
        print("EMPLEADOS GUARDADOS \n")

    def cargar_empleados(self, archivo: str):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, f"{archivo}.txt")
        if not os.path.exists(ruta_archivo):
            return "ERROR (ARCHIVO NO ENCONTRADO, NO EXISTENTE U OTRO)\n"
        with open(ruta_archivo, "r", encoding="utf-8") as archivo_a_recorrer:
            next(archivo_a_recorrer)  # Para saltar el encabezado
            for linea in archivo_a_recorrer:
                partes = linea.strip().split("|")
                # Verificando que si se realizará correctamente la partición
                if len(partes) >= 4:
                    id = int(partes[0])
                    nombre = partes[1]
                    salario_base = float(partes[2])
                    experiencia = int(partes[3])
                    empleado = Empleado(nombre, id, salario_base, experiencia)
                    self.agregar_empleado(empleado)
                else:
                    print("LÍNEA CON FORMATO INCORRECTO")
        print("ARCHIVO CARGADO \n") 
'''
Requerimiento adicional: Implementa un sistema de menús que permita al usuario interactuar con la clase GestorEmpleados, agregar empleados,
eliminarlos, buscar por ID y ver la lista de empleados y sus salarios, para este ejercicio puede implementar archivos de texto plano.
'''

# VARIABLES GLOBALES
ids_usados = set()



def insertar_datos()-> Empleado:
    print("\n")
    while True:
        try:
            nombre = str(input("Nombre: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            id: int  = random.randint(1000, 9999)
            if id not in ids_usados:
                ids_usados.add(id)
                print(f"Se le asigno la siguiente ID: {id}")
                break
            else:
                print("FALLO EN EL LARGO DEL ID GENERADO")
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")

    while True:
        try:
            salario_base = float(input("Salario Base: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            experiencia = int(input("Años de experiencia: "))
            break
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    x = Empleado(nombre, id, salario_base, experiencia)
    return x



def buscar_datos()-> int:
    while True:
        try:
            id = int(input("Digite la ID: "))
            return id
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")



def editar_datos(Empresa: GestorEmpleados, id: int):
    print("--- EDITAR EMPLEADO ---\n")
    while True:
        respuesta = str(input("EDITAR NOMBRE?(S/N)")).lower().strip()
        if respuesta == "s":
            try:
                nombre_nuevo = str(input("Nombre: "))
                break        
            except ValueError:
                print("ERROR EN EL TIPO DE DATO")
        elif respuesta == "n":
            nombre_nuevo = None
            break
        else:
            print("SOLO PUEDE RESPONDER CON S/s o N/n")

    while True:
        respuesta = str(input("EDITAR SALARIO BASE?(S/N)")).lower().strip()
        if respuesta == "s":
            try:
                salario_base_nuevo = float(input("Salario Base: "))
                break        
            except ValueError:
                print("ERROR EN EL TIPO DE DATO")
        elif respuesta == "n":
            salario_base_nuevo = None
            break
        else:
            print("SOLO PUEDE RESPONDER CON S/s o N/n")

    while True:
        respuesta = str(input("EDITAR AÑOS DE EXPERIENCIA?(S/N)")).lower().strip()
        if respuesta == "s":
            try:
                experiencia_nueva = int(input("Años de experiencia: "))
                break
            except ValueError:
                print("ERROR EN EL TIPO DE DATO")
        elif respuesta == "n":
            experiencia_nueva = None
            break
        else:
            print("SOLO PUEDE RESPONDER CON S/s o N/n")
    Empresa.editar_empleado(id, nombre_nuevo, salario_base_nuevo, experiencia_nueva)


def menu(Empresa: GestorEmpleados):
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar empleado")
        print("2. Eliminar empleado")
        print("3. Buscar empleado")
        print("4. Editar empleado")
        print("5. Mostrar empleados")
        print("6. Guardar empleados en archivo")
        print("7. Cargar empleados desde archivo")
        print("8. Salir")
        try:
            opcion = int(input("Ingrese una opción [1-8]: "))
        except ValueError:
            print("ERROR, TIPO DE DATO INVALIDO")
            continue  # Para saltar al siguiente bucle
        match opcion:
            case 1:
                emp = insertar_datos()
                Empresa.agregar_empleado(emp)
            case 2:
                print("\n--- BORRADO DE EMPLEADO ---\n")
                id_a_eliminar = buscar_datos()
                Empresa.eliminar_empleado(id_a_eliminar)

            case 3:
                print("\n--- BUSCANDO EMPLEADO ---\n")
                id_a_buscar = buscar_datos()
                empleado_encontrado = Empresa.buscar_empleado(id_a_buscar)
                if empleado_encontrado:
                    print(empleado_encontrado)
                else:
                    print("\n--- EMPLEADO NO ENCONTRADO ---\n")
            case 4:
                id_a_buscar = buscar_datos()
                empleado_encontrado = Empresa.buscar_empleado(id_a_buscar)
                if empleado_encontrado:
                    editar_datos(Empresa, id_a_buscar)
                else:
                    print("\n--- EMPLEADO NO ENCONTRADO ---\n")
            case 5:
                print("LISTA DE EMPLEADOS\n")
                Empresa.mostrar_empleados()
            case 6:
                Empresa.guardar_empleados("lista_empleados")
            case 7:
                Empresa.cargar_empleados("lista_empleados")
            case 8:
                print("\n--- QUE TENGA BUEN DÍA ---\n")
                break
            case _:
                print("\n--- OPCIÓN NO VALIDA ---\n")


# FUN. PRINCIPAL
def main():
    Empresa = GestorEmpleados()
    menu(Empresa)

main()