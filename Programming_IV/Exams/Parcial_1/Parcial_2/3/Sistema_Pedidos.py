from Productos import *
import json
import os
# ------------------------
# CONFIGURACIÓN DEL SISTEMA
# ------------------------
DISCOUNT_THRESHOLD = 5        # umbral de unidades para aplicar descuento
DISCOUNT_RATE = 0.10          # 10% de descuento si se compran > DISCOUNT_THRESHOLD unidades
JSON_FILENAME = "productos.json"  # archivo JSON en la misma carpeta del script


class SistemaPedidos:
    def __init__(self):
        # productos: id -> Producto
        self.__productos: dict[int, Producto] = {}

    # ----- Gestión de productos -----
    def agregar_producto(self, producto: Producto):
        if producto.id in self.__productos:
            raise KeyError(f"El producto con id {producto.id} ya existe.")
        self.__productos[producto.id] = producto

    def actualizar_producto(self, producto: Producto):
        if producto.id not in self.__productos:
            raise KeyError(f"No existe el producto id {producto.id}.")
        self.__productos[producto.id] = producto

    def eliminar_producto(self, producto_id: int):
        if producto_id in self.__productos:
            del self.__productos[producto_id]
        else:
            raise KeyError(f"No existe el producto id {producto_id}.")

    def obtener_producto(self, producto_id: int) -> Producto | None:
        return self.__productos.get(producto_id)

    def listar_disponibles(self) -> list[str]:
        return [p.descripcion() for p in sorted(self.__productos.values(), key=lambda x: x.id) if p.cantidad > 0]

    def listar_todos(self) -> list[str]:
        return [p.descripcion() for p in sorted(self.__productos.values(), key=lambda x: x.id)]

    def obtener_producto_por_nombre(self, nombre_busqueda: str) -> list[Producto]:
        """
        Búsqueda case-insensitive por nombre. Retorna lista de coincidencias (posiblemente vacía).
        """
        nb = nombre_busqueda.strip().lower()
        resultados: list[Producto] = []
        for p in self.__productos.values():
            if p.nombre.strip().lower() == nb:
                # coincidencia exacta (prioritaria)
                resultados = [p]
                return resultados
        # si no hay exactas, buscar por inclusión
        for p in self.__productos.values():
            if nb in p.nombre.strip().lower():
                resultados.append(p)
        return resultados

    # ----- Pedido -----
    def realizar_pedido(self, lineas: list[tuple[int, int]]) -> tuple[bool, float, list[str]]:
        """
        lineas: lista de tuplas (producto_id, cantidad_solicitada)
        Devuelve (exito_global, total_a_pagar, mensajes)
        - Si alguna linea no tiene stock suficiente NO realiza ninguna modificación y retorna False.
        - Si todo ok, reduce stock y devuelve total con descuentos aplicados por producto.
        """
        mensajes: list[str] = []
        # Validar existencias primero
        for producto_id, cantidad in lineas:
            p = self.obtener_producto(producto_id)
            if p is None:
                mensajes.append(f"Producto id {producto_id} no existe.")
                return False, 0.0, mensajes
            if cantidad <= 0:
                mensajes.append(f"Cantidad invalida para producto {producto_id}.")
                return False, 0.0, mensajes
            if cantidad > p.cantidad:
                mensajes.append(f"Stock insuficiente para {p.nombre} (id {producto_id}). Disponible: {p.cantidad}, solicitado: {cantidad}.")
                return False, 0.0, mensajes

        # Si pasa validaciones, calcular total y reducir stock
        total = 0.0
        for producto_id, cantidad in lineas:
            p = self.obtener_producto(producto_id)
            assert p is not None  # ya validado
            subtotal = p.precio * cantidad
            descuento = 0.0
            if cantidad > DISCOUNT_THRESHOLD:
                descuento = subtotal * DISCOUNT_RATE
                mensajes.append(f"Aplique {int(DISCOUNT_RATE*100)}% descuento en {p.nombre} por comprar {cantidad} unidades: -${descuento:.2f}")
            total += (subtotal - descuento)

        # Aplicar reducción de stock (ya todo validado)
        for producto_id, cantidad in lineas:
            p = self.obtener_producto(producto_id)
            assert p is not None
            p.reducir_stock(cantidad)

        mensajes.append(f"Total a pagar: ${total:.2f}")
        return True, total, mensajes

    # ----- Persistencia JSON (archivo fijo en la misma carpeta) -----
    def guardar_json(self, filename: str = JSON_FILENAME):
        arr = [p.to_dict() for p in sorted(self.__productos.values(), key=lambda x: x.id)]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(arr, f, indent=2, ensure_ascii=False)

    def cargar_json(self, filename: str = JSON_FILENAME):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Archivo {filename} no existe.")
        with open(filename, "r", encoding="utf-8") as f:
            arr = json.load(f)
        self.__productos = {}
        for item in arr:
            p = Producto.from_dict(item)
            self.__productos[p.id] = p
