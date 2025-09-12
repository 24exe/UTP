'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Constructores, Destructores y Métodos


TALLER 3

3. Cree una clase `InventarioProducto` que gestione un listado de productos (nombre,
precio, cantidad). Agregue métodos para añadir productos, calcular el valor total del
inventario y guardar todo en un archivo.
'''
from io import *
import os

class InventarioProducto:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre: str, precio: float, cantidad: int):
        """Agrega un producto al inventario"""
        # Por conveniencia cada producto sera un diccionario.
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        self.productos.append(producto)

    def valor_total(self) -> float:
        total = sum(producto["precio"] * producto["cantidad"] for producto in self.productos)
        return total

    def guardar_en_archivo(self):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "inventario.txt")
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("Nombre|Precio|Cantidad\n")
            for producto in self.productos:
                archivo.write(f"{producto['nombre']}|{producto['precio']}|{producto['cantidad']}\n")

Inventario = InventarioProducto()

def insert_Data():
    while True:
        try:
            nombre = str(input("Nombre: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            precio = float(input("Precio: ")) 
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    Inventario.agregar_producto(nombre, precio, cantidad)

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Crear Producto")
        print("2. Calcular Valor Total del Inventario")
        print("3. Guardar en Archivo")
        print("4. Salir")

        opcion = int(input("Ingrese una opción [1-4]: "))
        match opcion:
            case 1:
                insert_Data()
                print("--PRODUCTO CREADO--\n")
            case 2:
                print("Valor total del inventario:", Inventario.valor_total())
            case 3:
                Inventario.guardar_en_archivo()
                print("--REVISAR 'inventario.txt'--\n")
            case 4:
                print("QUE TENGA BUEN DIA")
                break
            case _:
                print("OPCION NO VALIDA")

# FUN. PRINCIPAL
def main():
    menu()

main()




