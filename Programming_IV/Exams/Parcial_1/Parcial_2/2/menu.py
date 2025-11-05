from Habitacion_Simple import Habitacion_Simple
from Habitaciones_Especiales import *
from Habitaciones_Especiales import _ServiciosMixin
from Sistema_Reservas import SistemaReservas

def inicializar_sistema_demo():
    sistema = SistemaReservas()
    sistema.agregar_habitacion(Habitacion_Simple(101, 100.0))
    sistema.agregar_habitacion(Habitacion_Simple(102, 95.0))
    sistema.agregar_habitacion(Habitacion_Doble(201, 180.0))
    sistema.agregar_habitacion(Habitacion_Doble(202, 200.0))
    sistema.agregar_habitacion(Suite(301, 350.0))
    return sistema


def mostrar_menu():
    print("\n=== Sistema de Reservas ===")
    print("1. Listar todas las habitaciones")
    print("2. Mostrar habitaciones disponibles")
    print("3. Reservar habitación (agregar servicios si aplica)")
    print("4. Cancelar reserva")
    print("5. Calcular precio total")
    print("6. Salir")


def pedir_entero(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor ingrese un número válido.")


def pedir_si_no(prompt: str) -> bool:
    while True:
        r = input(prompt + " [s/n]: ").strip().lower()
        if r in ("s", "si"):
            return True
        if r in ("n", "no"):
            return False
        print("Responda 's' o 'n'.")


def preguntar_agregar_servicios(hab: Habitacion_Simple):
    """Pregunta al usuario si desea agregar servicios con precios por defecto."""
    if not isinstance(hab, (Habitacion_Doble, Suite)):
        return

    agregar = pedir_si_no("¿Desea agregar servicios adicionales?")
    if not agregar:
        return

    servicios = list(_ServiciosMixin.SERVICIOS_DISPONIBLES.items())

    while True:
        print("\n--- Servicios disponibles ---")
        for i, (nombre, precio) in enumerate(servicios, start=1):
            print(f"{i}. {nombre} (${precio:.2f})")
        print("0. Finalizar selección")

        opcion = pedir_entero("Seleccione un servicio: ")
        if opcion == 0:
            break
        if 1 <= opcion <= len(servicios):
            nombre = servicios[opcion - 1][0]
            try:
                hab.agregar_servicio(nombre)
                print(f"Servicio '{nombre}' agregado. Total: {hab.calcular_precio_total():.2f}")
            except KeyError:
                print("Servicio no disponible.")
        else:
            print("Opción inválida.")

def mostrar_menu():
    print("\n=== Sistema de Reservas ===")
    print("1. Listar todas las habitaciones")
    print("2. Mostrar habitaciones disponibles")
    print("3. Reservar habitación (agregar servicios si aplica)")
    print("4. Cancelar reserva")
    print("5. Calcular precio total")
    print("6. Salir")


def pedir_entero(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor ingrese un número válido.")


def pedir_si_no(prompt: str) -> bool:
    while True:
        r = input(prompt + " [s/n]: ").strip().lower()
        if r in ("s", "si"):
            return True
        if r in ("n", "no"):
            return False
        print("Responda 's' o 'n'.")


def preguntar_agregar_servicios(hab: Habitacion_Simple):
    """Pregunta al usuario si desea agregar servicios con precios por defecto."""
    if not isinstance(hab, (Habitacion_Doble, Suite)):
        return

    agregar = pedir_si_no("¿Desea agregar servicios adicionales?")
    if not agregar:
        return

    servicios = list(_ServiciosMixin.SERVICIOS_DISPONIBLES.items())

    while True:
        print("\n--- Servicios disponibles ---")
        for i, (nombre, precio) in enumerate(servicios, start=1):
            print(f"{i}. {nombre} (${precio:.2f})")
        print("0. Finalizar selección")

        opcion = pedir_entero("Seleccione un servicio: ")
        if opcion == 0:
            break
        if 1 <= opcion <= len(servicios):
            nombre = servicios[opcion - 1][0]
            try:
                hab.agregar_servicio(nombre)
                print(f"Servicio '{nombre}' agregado. Total: {hab.calcular_precio_total():.2f}")
            except KeyError:
                print("Servicio no disponible.")
        else:
            print("Opción inválida.")


# ------------------------
# MENÚ PRINCIPAL
# ------------------------
def main():
    sistema = inicializar_sistema_demo()

    while True:
        mostrar_menu()
        opcion = pedir_entero("Seleccione una opción: ")

        if opcion == 1:
            print("\n--- Todas las habitaciones ---")
            for desc in sistema.listar_todas():
                print(desc)

        elif opcion == 2:
            print("\n--- Habitaciones disponibles ---")
            disponibles = sistema.mostrar_disponibles()
            if not disponibles:
                print("No hay habitaciones disponibles.")
            else:
                for desc in disponibles:
                    print(desc)

        elif opcion == 3:
            num = pedir_entero("Número de habitación a reservar: ")
            hab = sistema.obtener_habitacion(num)
            if hab is None:
                print("No existe esa habitación.")
                continue
            if hab.reservado:
                print("La habitación ya está reservada.")
                continue

            preguntar_agregar_servicios(hab)
            hab.reservar()
            print(f"Habitación {num} reservada exitosamente. Total a pagar: {hab.calcular_precio_total():.2f}")

        elif opcion == 4:
            num = pedir_entero("Número de habitación para cancelar: ")
            if sistema.cancelar_reserva(num):
                print("Reserva cancelada correctamente.")
            else:
                print("La habitación no estaba reservada o no existe.")

        elif opcion == 5:
            num = pedir_entero("Número de habitación: ")
            try:
                total = sistema.calcular_precio_total(num)
                print(f"Precio total de la habitación {num}: ${total:.2f}")
            except KeyError:
                print("No existe esa habitación.")

        elif opcion == 6:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()