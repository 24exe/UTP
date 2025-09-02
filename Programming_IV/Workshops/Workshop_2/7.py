'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Archivos, clases y objetos.

TALLER 2

7. Inventario de almacén
- Crea una clase `Producto` con atributos: código, nombre, cantidad, precio y categoría.
- Implemente un método que permita guardar el inventario en `almacen.txt`.
- Otro método que lea el archivo y muestre el valor total en stock de cada categoría.
'''
from io import *
import os

class Producto:

    codigo: int = 0
    nombre: str
    cantidad: int
    precio: int
    categoria: str

    def InsertData(self):
        while True:
            try:
                nameAux = str(input("Digite el nombre del Producto: "))
                self.nombre = nameAux
                break
            except ValueError:
                print ("ERROR, TIPO DE DATO INVALIDO \n")

        while True:
            try:
                precioAux = int(input("Digite el precio del producto: "))
                self.precio = precioAux
                break
            except ValueError:
                print ("ERROR, TIPO DE DATO INVALIDO \n")

        while True:
            try:
                cantidadAux = int(input("Digite la cantidad de producto en Stock: "))
                if cantidadAux >= 0:
                    self.cantidad = cantidadAux
                    break
                else:
                    print("TIENE QUE INGRESAR UN NÚMERO ENTERO POSITIVO O 0. \n")
            except ValueError:
                print ("ERROR, TIPO DE DATO INVALIDO \n")
        while True:
            try:
                catAux = str(input("Categoria del producto: "))
                self.categoria = catAux
                break
            except ValueError:
                print ("ERROR, TIPO DE DATO INVALIDO \n")

        Producto.codigo += 1
        self.codigo = Producto.codigo
        print(f"Se le asigno la siguiente ID al producto: {self.codigo}\n")


    @staticmethod
    def guardarInventario(productos: list):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "almacen.txt")
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("Codigo,Nombre,Cantidad,Precio,Categoria\n")
            for prod in productos:
                archivo.write(f"{prod.codigo},{prod.nombre},{prod.cantidad},{prod.precio},{prod.categoria}\n")
            archivo.close()

    @staticmethod
    def mostrarValorporCategoriaEnStock():
        valores = {}
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "almacen.txt")
        with open(ruta_archivo, "r") as archivo:
            next(archivo)  # Saltar encabezado
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) == 5:
                    _, _, cantidad, precio, categoria = partes
                    cantidad = int(cantidad)
                    precio = int(precio)
                    valor = cantidad * precio
                    if categoria in valores:
                        valores[categoria] += valor
                    else:
                        valores[categoria] = valor
        print("Valor total en stock por categoría:")
        for cat, val in valores.items():
            print(f"{cat}: ${val}")


n: int
while True:
    try:    
        num = int(input("¿Cuantos productos desea Ingresar?: "))
        n = num
        break
    except (ValueError, TypeError):
        print("ERROR DE INSERCIÓN EN EL NÚMERO DE PRODUCTOS, SE DARA UN TAMAÑO DE 5 POR DEFECTO. \n")
        n = 5
        break

productos: list[Producto] = []
for i in range(n):
    print(f"Producto {i+1}: \n")
    producto = Producto()
    producto.InsertData()
    productos.append(producto)
    print("\n")

Producto.guardarInventario(productos)
Producto.mostrarValorporCategoriaEnStock()




    