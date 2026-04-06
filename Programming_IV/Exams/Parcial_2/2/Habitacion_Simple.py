class Habitacion_Simple:
    def __init__(self, numero: int, precio: float):
        self.__numero: int = int(numero)
        self.__precio: float = float(precio)
        self.__reservado: bool = False

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, nuevo: float):
        if nuevo < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = float(nuevo)

    @property
    def reservado(self) -> bool:
        return self.__reservado

    def reservar(self) -> bool:
        '''
        Este método intenta reservar la habitación. Si ya está reservada, retorna False.
        Si está disponible, la marca como reservada y retorna True para confirmar la operación exitosa.
        '''
        if self.__reservado:
            return False
        self.__reservado = True
        return True

    def cancelar_reserva(self) -> bool:
        '''
        Este método intenta cancelar la reserva de la habitación. Si no está reservada, retorna False.
        Si está reservada, la marca como disponible y retorna True para confirmar la operación exitosa
        '''
        if not self.__reservado:
            return False
        self.__reservado = False
        return True

    def calcular_precio_total(self) -> float:
        '''
        Este método calcula el precio total de la habitación.
        En una habitación simple, el precio total es simplemente el precio base.
        '''
        return self.__precio

    def descripcion(self) -> str:
        '''
        Este método retorna una descripción de la habitación, incluyendo su número, tipo (simple),
        precio base y estado (disponible o reservado).
        '''
        estado = "Reservado" if self.__reservado else "Disponible"
        tipo_habitacion = self.__class__.__name__.replace("_", " ")
        return f"Habitación {self.__numero} - {tipo_habitacion} - Precio base: {self.__precio:.2f} - {estado}"