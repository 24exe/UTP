from typing import Any
from datetime import datetime


class Producto:
    """Clase base con encapsulamiento: id, nombre, precio y cantidad disponible."""
    def __init__(self, producto_id: int, nombre: str, precio: float, cantidad: int):
        self.__id: int = int(producto_id)
        self.__nombre: str = str(nombre)
        self.__precio: float = float(precio)
        self.__cantidad: int = int(cantidad)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo: str):
        self.__nombre = str(nuevo)

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, nuevo: float):
        if nuevo < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = float(nuevo)

    @property
    def cantidad(self) -> int:
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nuevo: int):
        if nuevo < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.__cantidad = int(nuevo)

    def reducir_stock(self, unidades: int) -> bool:
        """Intenta reducir stock. Devuelve True si se pudo, False si no hay suficiente stock."""
        if unidades <= 0:
            raise ValueError("Las unidades a pedir deben ser positivas.")
        if unidades > self.__cantidad:
            return False
        self.__cantidad -= unidades
        return True

    def aumentar_stock(self, unidades: int):
        if unidades <= 0:
            raise ValueError("Las unidades a añadir deben ser positivas.")
        self.__cantidad += unidades

    def descripcion(self) -> str:
        return f"[{self.__id}] {self.__nombre} - ${self.__precio:.2f} - Stock: {self.__cantidad}"

    def tipo(self) -> str:
        return "Producto"

    def to_dict(self) -> dict[str, Any]:
        """Serialización para JSON (subclases extienden)."""
        return {
            "tipo": self.tipo(),
            "id": self.__id,
            "nombre": self.__nombre,
            "precio": self.__precio,
            "cantidad": self.__cantidad
        }

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Producto":
        """Fábrica para reconstruir el objeto apropiado desde dict (usa 'tipo')."""
        tipo = data.get("tipo", "Producto")
        if tipo == "Electronico":
            return Electronico(
                producto_id=data["id"],
                nombre=data["nombre"],
                precio=data["precio"],
                cantidad=data["cantidad"],
                garantia_meses=data.get("garantia_meses", 0)
            )
        if tipo == "Ropa":
            return Ropa(
                producto_id=data["id"],
                nombre=data["nombre"],
                precio=data["precio"],
                cantidad=data["cantidad"],
                talla=data.get("talla", "")
            )
        if tipo == "Alimento":
            return Alimento(
                producto_id=data["id"],
                nombre=data["nombre"],
                precio=data["precio"],
                cantidad=data["cantidad"],
                fecha_caducidad=data.get("fecha_caducidad", "")
            )
        # fallback a Producto base
        return Producto(
            producto_id=data["id"],
            nombre=data["nombre"],
            precio=data["precio"],
            cantidad=data["cantidad"]
        )

class Electronico(Producto):
    def __init__(self, producto_id: int, nombre: str, precio: float, cantidad: int, garantia_meses: int):
        super().__init__(producto_id, nombre, precio, cantidad)
        self.__garantia_meses: int = int(garantia_meses)

    @property
    def garantia_meses(self) -> int:
        return self.__garantia_meses

    @garantia_meses.setter
    def garantia_meses(self, nuevo: int):
        if nuevo < 0:
            raise ValueError("La garantía no puede ser negativa.")
        self.__garantia_meses = int(nuevo)

    def tipo(self) -> str:
        return "Electronico"

    def descripcion(self) -> str:
        base = super().descripcion()
        return f"{base} - Garantía: {self.__garantia_meses} meses"

    def to_dict(self) -> dict[str, Any]:
        d = super().to_dict()
        d.update({"garantia_meses": self.__garantia_meses})
        return d


class Ropa(Producto):
    def __init__(self, producto_id: int, nombre: str, precio: float, cantidad: int, talla: str):
        super().__init__(producto_id, nombre, precio, cantidad)
        self.__talla: str = str(talla)

    @property
    def talla(self) -> str:
        return self.__talla

    @talla.setter
    def talla(self, nuevo: str):
        self.__talla = str(nuevo)

    def tipo(self) -> str:
        return "Ropa"

    def descripcion(self) -> str:
        base = super().descripcion()
        return f"{base} - Talla: {self.__talla}"

    def to_dict(self) -> dict[str, Any]:
        d = super().to_dict()
        d.update({"talla": self.__talla})
        return d


class Alimento(Producto):
    def __init__(self, producto_id: int, nombre: str, precio: float, cantidad: int, fecha_caducidad: str):
        super().__init__(producto_id, nombre, precio, cantidad)
        # se acepta cadena ISO 'YYYY-MM-DD'; no se parsea aquí para simplicidad
        self.__fecha_caducidad: str = str(fecha_caducidad)

    @property
    def fecha_caducidad(self) -> str:
        return self.__fecha_caducidad

    @fecha_caducidad.setter
    def fecha_caducidad(self, nueva: str):
        # validación simple de formato YYYY-MM-DD
        try:
            datetime.strptime(nueva, "%Y-%m-%d")
        except Exception:
            raise ValueError("Formato de fecha debe ser YYYY-MM-DD.")
        self.__fecha_caducidad = nueva

    def tipo(self) -> str:
        return "Alimento"

    def descripcion(self) -> str:
        base = super().descripcion()
        return f"{base} - Caduca: {self.__fecha_caducidad}"

    def to_dict(self) -> dict[str, Any]:
        d = super().to_dict()
        d.update({"fecha_caducidad": self.__fecha_caducidad})
        return d