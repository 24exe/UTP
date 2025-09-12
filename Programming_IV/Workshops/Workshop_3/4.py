'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Constructores, Destructores y Métodos


TALLER 3

4. Diseñe una clase `Vehículo` que guarde marca, modelo, año, tipo y placa. Incluya un
método para guardar en archivo solo los vehículos del año actual y otro para leerlos.
'''
import datetime
import os
from io import *

class Vehiculo:
    # Atributos de instancia
    vehiculos = []
    def __init__(self, marca: str, modelo: str, year: int, tipo: str, placa: str):
        self.marca: str = marca
        self.modelo: str = modelo
        self.year: int = year
        self.tipo: str = tipo
        self.placa: str = placa

        Vehiculo.vehiculos.append(self)
    
    @classmethod
    def save_Actuals(cls):
        actual_year = datetime.datetime.now().year
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "vehiculos.txt")
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("Marca|Modelo|Tipo|Placa|Año\n")
            for vehiculo in cls.vehiculos:
                if vehiculo.year == actual_year:
                    archivo.write(f"{vehiculo.marca}|{vehiculo.modelo}|{vehiculo.tipo}|{vehiculo.placa}|{vehiculo.year}\n")
    
    def read_Archive():
        # Quice hacerlo de otra manera
        # Lista de Diccionarios
        vehiculos_leidos = []
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "vehiculos.txt")
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            next(archivo)  # Saltar encabezado
            for linea in archivo:
                partes = linea.strip().split("|")
                if len(partes) == 5:
                    marca, modelo, tipo, placa, año = partes
                    vehiculos_leidos.append({"marca": marca, "modelo": modelo, "tipo": tipo, "placa": placa, "año": int(año)})
                else:
                    print(f"Línea con formato incorrecto: {linea.strip()}")
        return vehiculos_leidos


placas_usadas = set()
def insert_Data():
    while True:
        try:
            marca = str(input("Marca: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            modelo = str(input("Modelo: ")) 
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            year = int(input("Año: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            tipo = str(input("Tipo: ")) 
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            placa = str(input("Placa: "))
    
            if len(placa) == 6:
                if placa in placas_usadas:
                    print("ERROR, PLACA YA USADO\n")
                else:
                    placas_usadas.add(placa)
                break
            else:
                print("RECUERDE QUE LAS PLACAS SON DE 6 DIGITOS")
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    x = Vehiculo(marca, modelo, year, tipo, placa)

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Crear Vehiculo")
        print("2. Guardar en Archivo")
        print("3. Leer Archivo")
        print("4. Salir")

        opcion = int(input("Ingrese una opción [1-4]: "))
        match opcion:
            case 1:
                insert_Data()
                print("--Vehiculo CREADO--\n")
            case 2:
                Vehiculo.save_Actuals()
                print("--REVISAR 'vehiculos.txt'--\n")
            case 3:
                vehiculos_actuales = Vehiculo.read_Archive()
                for vehiculo in vehiculos_actuales:
                    print(f"Marca: {vehiculo['marca']}, Modelo: {vehiculo['modelo']}, Año: {vehiculo['año']}, Tipo: {vehiculo['tipo']}, Placa: {vehiculo['placa']}")
            case 4:
                print("QUE TENGA BUEN DIA")
                break
            case _:
                print("OPCION NO VALIDA")


# FUN. PRINCIPAL
def main():
    menu()

main()