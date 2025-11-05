from Habitacion_Simple import Habitacion_Simple


# ------------------------
# MIXIN DE SERVICIOS (METODOS PROTEGIDO)
# ------------------------
class _ServiciosMixin:
    """Permite agregar y listar servicios adicionales con precios predefinidos."""
    SERVICIOS_DISPONIBLES = {
        "Servicio a la habitación": 30.0,
        "Servicio de lavandería": 25.0,
        "Servicio de transporte": 40.0,
        "Desayuno incluido": 20.0,
        "Acceso al spa": 60.0
    }

    def __init__(self):
        self.__servicios: dict[str, float] = {}

    # METODOS PROTEGIDOS

    def _agregar_servicio(self, nombre: str):
        if nombre not in self.SERVICIOS_DISPONIBLES:
            raise KeyError(f"Servicio '{nombre}' no disponible.")
        self.__servicios[nombre] = self.SERVICIOS_DISPONIBLES[nombre]

    def _quitar_servicio(self, nombre: str):
        if nombre in self.__servicios:
            del self.__servicios[nombre]
        else:
            raise KeyError(f"Servicio '{nombre}' no encontrado.")

    def _listar_servicios(self) -> list[str]:
        return [f"{n} (${p:.2f})" for n, p in self.__servicios.items()]

    def _total_servicios(self) -> float:
        return sum(self.__servicios.values())

    def _obtener_servicios_dict(self) -> dict[str, float]:
        return dict(self.__servicios)


# ------------------------
# CLASES DERIVADAS
# ------------------------
class Habitacion_Doble(Habitacion_Simple, _ServiciosMixin):
    def __init__(self, numero: int, precio: float):
        Habitacion_Simple.__init__(self, numero, precio)
        _ServiciosMixin.__init__(self)

    def agregar_servicio(self, nombre: str):
        self._agregar_servicio(nombre)

    def quitar_servicio(self, nombre: str):
        self._quitar_servicio(nombre)

    def listar_servicios(self) -> list[str]:
        return self._listar_servicios()

    def calcular_precio_total(self) -> float:
        return self.precio + self._total_servicios()

    def descripcion(self) -> str:
        base = super().descripcion()
        servicios = ", ".join(self.listar_servicios()) if self.listar_servicios() else "Sin servicios"
        return f"{base} - Servicios: {servicios} - Total: {self.calcular_precio_total():.2f}"


class Suite(Habitacion_Simple, _ServiciosMixin):
    def __init__(self, numero: int, precio: float):
        Habitacion_Simple.__init__(self, numero, precio)
        _ServiciosMixin.__init__(self)

    def agregar_servicio(self, nombre: str):
        self._agregar_servicio(nombre)

    def quitar_servicio(self, nombre: str):
        self._quitar_servicio(nombre)

    def listar_servicios(self) -> list[str]:
        return self._listar_servicios()

    def calcular_precio_total(self) -> float:
        return self.precio + self._total_servicios()

    def descripcion(self) -> str:
        base = super().descripcion()
        servicios = ", ".join(self.listar_servicios()) if self.listar_servicios() else "Sin servicios"
        return f"{base} - Servicios: {servicios} - Total: {self.calcular_precio_total():.2f}"