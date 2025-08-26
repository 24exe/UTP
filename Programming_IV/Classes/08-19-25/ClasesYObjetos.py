# Ejemplo Clase


class Automovil:
    marca = " "
    color = " "
    modelo = 0
    placa = " "

    def print_datos(self):
        return (f"Marca {self.marca} \n Color: {self.color} \n  Modelo: {self.modelo} \n Placa: {self.placa} ")

    def modificar_datos(self):


# Ejemplo Objeto de la Clase:

march = Automovil()
march.color = "Gris"
march.marca = "Nissan"
march.modelo = 2025
march.placa = "QWE123"

march.print_datos()