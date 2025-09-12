'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Nombre: Rafael Urrea Gaviria
Codigo: 1004737606


Parcial 1

3. Sistema de Ventas de Productos con Inventario
Crea un sistema de ventas que gestione productos y clientes. El sistema
debe llevar control de los productos en inventario y de las ventas
realizadas, Para ello, crea las siguientes clases:


Nota importante: para este ejercicio debe implementar archivos XML, la
documentación quedará adjunta en la actividad de “parcial I”.
'''
# LIBRERIAS
from io import *
import os
import random
import xml.etree.ElementTree as ET
'''
Clase Producto:

• Atributos:
    o Nombre (cadena de texto)
    o ID (entero)
     Precio (flotante)
    o Cantidad en inventario (entero)

• Métodos:
    o Constructor para inicializar todos los atributos.
    o disminuir_inventario(cantidad: int): Disminuye la cantidad del inventario al realizar una venta.
    o aumentar_inventario(cantidad: int): Aumenta la cantidad del inventario al reponer stock.
    o mostrar_informacion(): Muestra la información del producto en formato legible.

'''

class Producto():
    def __init__(self, nombre: str, id: int, precio: float, cantidad: int):
        self.nombre: str = nombre
        self.id: int = id
        self.precio: float = precio
        self.cantidad: int = cantidad

    def disminuir_inventario(self, disminucion: int):
        '''
        if self.cantidad == 0:
            print("NO HAY STOCK DEL PRODUCTO\n")
        elif self.cantidad - disminucion < 0:
            print(f"CANTIDAD DE PRODUCTO INSUFICIENTE, STOCK ACTUAL: {self.cantidad}")
        else:
            self.cantidad -= disminucion
        '''
        self.cantidad -= disminucion
    
    def aumentar_inventario(self, aumento: int):
        self.cantidad = self.cantidad + aumento
    def __str__(self):
        return f"ID: {self.id}, Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}\n"
    

'''
Clase Cliente:

• Atributos:
    o Nombre (cadena de texto)
    o ID (entero)
    o Saldo (flotante)

• Métodos:
    o Constructor para inicializar los atributos.
    o realizar_compra(producto: Producto, cantidad: int): Reduce el saldo del cliente y reduce la cantidad en inventario del producto,
      siempre que el saldo y el stock lo permitan.
    o mostrar_informacion(): Muestra la información del cliente en
    formato legible.
'''


class Cliente():
    def __init__(self, nombre: str, id: int, saldo: float):
        self.nombre: str = nombre
        self.id: int = id
        self.saldo: float = saldo
        
    def realizar_compra(self, producto: Producto, cantidad_a_comprar: int):
        if producto.cantidad == 0:
            print("NO HAY STOCK DEL PRODUCTO\n")
        elif producto.cantidad < cantidad_a_comprar:
            print(f"CANTIDAD DE PRODUCTO INSUFICIENTE, STOCK ACTUAL: {self.cantidad}")
        else:
            costo = producto.precio * cantidad_a_comprar
            if self.saldo >=  costo and producto.cantidad >= cantidad_a_comprar:
                self.saldo -= costo
                producto.disminuir_inventario(cantidad_a_comprar)
                print(f"Compra realizada: {producto.nombre} x{cantidad_a_comprar}")
            else:
                print("SALDO INSUFICIENTE PARA REALIZAR LA COMPRA.\n")
    
    def mostrar_informacion(self):
        print(f"ID: {self.id}, Cliente: {self.nombre}, Saldo: {self.saldo}\n")

'''
Clase Tienda:

• Atributos:
    o Una lista de productos disponibles.
    o Una lista de clientes registrados.

• Métodos:
    o agregar_producto(producto: Producto): Agrega un nuevo producto a la lista de productos.
    o agregar_cliente(cliente: Cliente): Agrega un cliente a la lista de clientes.
    o realizar_venta(id_cliente: int, id_producto: int, cantidad: int): Realiza una venta de un producto a un cliente si se cumplen las
    condiciones de stock y saldo.
    o mostrar_productos(): Muestra todos los productos disponibles.
    o mostrar_clientes(): Muestra todos los clientes registrados.
    o guardar_datos(archivo: str): Guarda los productos y clientes en un archivo.
o cargar_datos(archivo: str): Carga los productos y clientes desde
un archivo.
'''

class Tienda:
    def __init__(self):
        self.productos_disponibles: list[Producto] = []
        self.clientes_registrados: list[Cliente] = []
    
    def agregar_producto(self, producto: Producto):
        self.productos_disponibles.append(producto)
        self.productos_disponibles.sort(key = lambda producto: producto.id)

    def agregar_cliente(self, cliente: Cliente):
        self.clientes_registrados.append(cliente)
        self.clientes_registrados.sort(key = lambda cliente: cliente.id)
    
    def buscar_cliente(self, id: int) -> Cliente:
        for cliente in self.clientes_registrados:
            if id == cliente.id:
                return cliente

    def buscar_producto(self, id: int) -> Producto:
        for producto in self.productos_disponibles:
            if id == producto.id:
                return producto

    def realizar_venta(self, id_cliente: int, id_producto: int, cantidad: int):
        cliente_comprador = self.buscar_cliente(id_cliente)
        producto_a_comprar = self.buscar_producto(id_producto)
        if cliente_comprador and producto_a_comprar:
            if producto_a_comprar.cantidad >= cantidad:
                cliente_comprador.realizar_compra(producto_a_comprar, cantidad)
                print ("VENTA REALIZADA\n")
            else:
                print("STOCK INSUFICIENTE\n")
        else:
            if not cliente_comprador:
                print("CLIENTE NO ENCONTRADO\n")
            if not producto_a_comprar:
                print("PRODUCTO NO ENCONTRADO\n")

    def mostrar_productos(self):
        for producto in self.productos_disponibles:
            print(producto)

    def mostrar_clientes(self):
        for cliente in self.clientes_registrados:
            cliente.mostrar_informacion()


    def guardar_datos(self, archivo: str):
        root = ET.Element("Tienda")
        productos_elem = ET.SubElement(root, "Productos")
        for producto in self.productos_disponibles:
            prod_elem = ET.SubElement(productos_elem, "Producto")
            ET.SubElement(prod_elem, "ID").text = str(producto.id)
            ET.SubElement(prod_elem, "Nombre").text = producto.nombre
            ET.SubElement(prod_elem, "Precio").text = str(producto.precio)
            ET.SubElement(prod_elem, "Cantidad").text = str(producto.cantidad)

        clientes_elem = ET.SubElement(root, "Clientes")
        for cliente in self.clientes_registrados:
            cli_elem = ET.SubElement(clientes_elem, "Cliente")
            ET.SubElement(cli_elem, "ID").text = str(cliente.id)
            ET.SubElement(cli_elem, "Nombre").text = cliente.nombre
            ET.SubElement(cli_elem, "Saldo").text = str(cliente.saldo)

        tree = ET.ElementTree(root)
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, archivo)
        tree.write(ruta_archivo, encoding="utf-8", xml_declaration=True)

    def cargar_datos(self, archivo: str):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, archivo)
        if not os.path.exists(ruta_archivo):
            print("Archivo no encontrado.")
            return

        tree = ET.parse(ruta_archivo)
        root = tree.getroot()

        self.productos_disponibles.clear()
        self.clientes_registrados.clear()

        productos_elem = root.find("Productos")
        if productos_elem is not None:
            for prod_elem in productos_elem.findall("Producto"):
                id_ = int(prod_elem.find("ID").text)
                nombre = prod_elem.find("Nombre").text
                precio = float(prod_elem.find("Precio").text)
                cantidad = int(prod_elem.find("Cantidad").text)
                producto = Producto(nombre, id_, precio, cantidad)
                self.productos_disponibles.append(producto)
                ids_productos.add(id_)

        clientes_elem = root.find("Clientes")
        if clientes_elem is not None:
            for cli_elem in clientes_elem.findall("Cliente"):
                id_ = int(cli_elem.find("ID").text)
                nombre = cli_elem.find("Nombre").text
                saldo = float(cli_elem.find("Saldo").text)
                cliente = Cliente(nombre, id_, saldo)
                self.clientes_registrados.append(cliente)
                ids_usuarios.add(id_)

# VARIABLES GLOBALES
ids_usuarios = set()
ids_productos = set()



def insertar_data_producto()-> Producto:
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
            if id not in ids_productos:
                ids_productos.add(id)
                print(f"Se le asigno la siguiente ID: {id}")
                break
            else:
                print("FALLO EN EL LARGO DEL ID GENERADO")
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
            cantidad = int(input("Cantidad en Stock: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    x = Producto(nombre, id, precio, cantidad)
    return x

def insertar_data_cliente()-> Cliente:
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
            if id not in ids_usuarios:
                ids_usuarios.add(id)
                print(f"Se le asigno la siguiente ID: {id}")
                break
            else:
                print("FALLO EN EL LARGO DEL ID GENERADO")
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")

    while True:
        try:
            saldo = float(input("Saldo: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    x = Cliente(nombre, id, saldo)
    return x

def venta(tienda: Tienda):
    print("\n --- PROCESO DE VENTA ---\n")
    while True:
        try:
            id_cliente = int(input("ID de Cliente: "))
            if not any(cliente.id == id_cliente for cliente in tienda.clientes_registrados):
                print("ID de cliente no encontrado. Intente de nuevo.")
                continue
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            id_producto = int(input("ID del Producto: "))
            if not any(producto.id == id_producto for producto in tienda.productos_disponibles):
                print("ID de producto no encontrado. Intente de nuevo.")
                continue
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            cantidad = int(input("Cantidad a comprar: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    tienda.realizar_venta(id_cliente, id_producto, cantidad)


def menu(tienda: Tienda):
    while True:
        print("\n--- Menu de la Tienda ---")
        print("1. Agregar producto")
        print("2. Agregar cliente")
        print("3. Realizar venta")
        print("4. Mostrar productos")
        print("5. Mostrar clientes")
        print("6. Mostrar ambos")
        print("7. Guardar datos")
        print("8. Cargar datos")
        print("9. Salir")
        try:
            opcion = int(input("Ingrese una opción [1-9]: "))
        except ValueError:
            print("ERROR, TIPO DE DATO INVALIDO")
            continue
        match opcion:
            case 1:
                prod = insertar_data_producto()
                tienda.agregar_producto(prod)
            case 2:
                cliente = insertar_data_cliente()
                tienda.agregar_cliente(cliente)
            case 3:
                venta(tienda)
            case 4:
                print("\n--- PRODUCTOS EN STOCK ---\n")
                tienda.mostrar_productos()
            case 5:
                print("\n--- CLIENTES REGISTRADOS ---\n")
                tienda.mostrar_clientes()
            case 6:
                print("\n--- CLIENTES REGISTRADOS ---\n")
                tienda.mostrar_clientes()
                print("\n--- PRODUCTOS EN STOCK ---\n")
                tienda.mostrar_productos()
            case 7:
                tienda.guardar_datos("tienda_info")
                print("\n---DATOS GUARDADOS---\n")
            case 8:
                tienda.cargar_datos("tienda_info")
                print("\n---DATOS CARGADOS---\n")
            case 9:
                print("\n---QUE TENGA BUEN DÍA---\n")
                break
            case _:
                print("\n--- OPCIÓN NO VALIDA ---\n")
                

# FUNCIÓN PRINCIPAL
def main():
    tienda = Tienda()
    menu(tienda)

main()