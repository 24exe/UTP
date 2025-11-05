from Habitacion_Simple import Habitacion_Simple

class SistemaReservas:
    def __init__(self):
        self.__habitaciones: dict[int, Habitacion_Simple] = {}

    def agregar_habitacion(self, habitacion: Habitacion_Simple):
        if habitacion.numero in self.__habitaciones:
            raise KeyError(f"La habitación {habitacion.numero} ya existe.")
        self.__habitaciones[habitacion.numero] = habitacion


    #  Optional[Habitacion] es el equivalente con la librería typing de Habitacion | None
    def obtener_habitacion(self, numero: int) -> Habitacion_Simple | None:
        return self.__habitaciones.get(numero)

    def mostrar_disponibles(self) -> list[str]:
        return [h.descripcion() for h in self.__habitaciones.values() if not h.reservado]

    def listar_todas(self) -> list[str]:
        return [h.descripcion() for h in self.__habitaciones.values()]

    def reservar_habitacion(self, numero: int) -> bool:
        h = self.obtener_habitacion(numero)
        if h is None:
            raise KeyError(f"No existe la habitación número {numero}.")
        return h.reservar()

    def cancelar_reserva(self, numero: int) -> bool:
        h = self.obtener_habitacion(numero)
        if h is None:
            raise KeyError(f"No existe la habitación número {numero}.")
        return h.cancelar_reserva()

    def calcular_precio_total(self, numero: int) -> float:
        h = self.obtener_habitacion(numero)
        if h is None:
            raise KeyError(f"No existe la habitación número {numero}.")
        return h.calcular_precio_total()
