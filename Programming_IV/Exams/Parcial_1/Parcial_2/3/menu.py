from Productos import *
from Sistema_Pedidos import * 

def inicializar_demo() -> SistemaPedidos:
    sp = SistemaPedidos()
    sp.agregar_producto(Electronico(1, "Smartphone X", 1200.0, 10, garantia_meses=24))
    sp.agregar_producto(Electronico(2, "Auriculares BT", 150.0, 20, garantia_meses=12))
    sp.agregar_producto(Ropa(3, "Camiseta deportiva", 25.0, 50, talla="M"))
    sp.agregar_producto(Ropa(4, "Pantalón jeans", 45.0, 30, talla="L"))
    sp.agregar_producto(Alimento(5, "Café molido 250g", 8.0, 100, fecha_caducidad="2026-06-30"))
    sp.agregar_producto(Alimento(6, "Galletas pack", 3.5, 40, fecha_caducidad="2025-12-31"))
    # Si existe JSON en carpeta, cargarlo para sobrescribir demo (útil para persistencia)
    if os.path.exists(JSON_FILENAME):
        try:
            sp.cargar_json(JSON_FILENAME)
            print(f"Productos cargados desde {JSON_FILENAME}.")
        except Exception:
            # si falla la carga, mantener demo y sobrescribir después si el usuario guarda
            pass
    return sp


def mostrar_menu():
    print("\n=== Sistema de Gestión de Pedidos ===")
    print("1. Listar todos los productos")
    print("2. Listar productos disponibles")
    print("3. Realizar pedido")
    print("4. Agregar producto manualmente")
    print("5. Guardar productos a JSON (productos.json en carpeta actual)")
    print("6. Cargar productos desde JSON (productos.json en carpeta actual, sobrescribe actual)")
    print("7. Salir")


def pedir_entero(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ingresa un número entero válido.")


def pedir_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ingresa un número válido (ej. 12.5).")


def pedir_si_no(prompt: str) -> bool:
    while True:
        r = input(prompt + " [s/n]: ").strip().lower()
        if r in ("s", "si"):
            return True
        if r in ("n", "no"):
            return False
        print("Responde 's' o 'n'.")


def agregar_producto_interactivo(sistema: SistemaPedidos):
    pid = pedir_entero("ID numérico del producto: ")
    if sistema.obtener_producto(pid) is not None:
        print("Ya existe un producto con ese ID.")
        return
    nombre = input("Nombre del producto: ").strip()
    # prevenir nombres duplicados exactos
    existentes = sistema.obtener_producto_por_nombre(nombre)
    if any(p.nombre.strip().lower() == nombre.strip().lower() for p in existentes):
        print("Ya existe un producto con ese nombre exacto. Elija otro nombre.")
        return
    precio = pedir_float("Precio unitario: ")
    cantidad = pedir_entero("Cantidad en stock: ")

    print("Tipos:")
    print("1. Electrónico")
    print("2. Ropa")
    print("3. Alimento")
    tipo = pedir_entero("Selecciona tipo: ")
    if tipo == 1:
        garantia = pedir_entero("Garantía (meses): ")
        p = Electronico(pid, nombre, precio, cantidad, garantia)
    elif tipo == 2:
        talla = input("Talla (ej. S, M, L): ").strip()
        p = Ropa(pid, nombre, precio, cantidad, talla)
    elif tipo == 3:
        fecha = input("Fecha de caducidad (YYYY-MM-DD): ").strip()
        # validación simple:
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except Exception:
            print("Formato de fecha inválido. Se usará cadena sin validar.")
        p = Alimento(pid, nombre, precio, cantidad, fecha)
    else:
        print("Tipo inválido. Producto no creado.")
        return

    sistema.agregar_producto(p)
    print("Producto agregado correctamente.")

def realizar_pedido_interactivo(sistema: SistemaPedidos):
    """
    Ahora el usuario ingresa el nombre del producto (no ID) y la cantidad deseada.
    Se permite agregar múltiples líneas por nombre.
    """
    print("\nIngrese las líneas del pedido por NOMBRE del producto. Para finalizar, ingresa nombre vacío.")
    lineas: list[tuple[int, int]] = []
    while True:
        nombre = input("Nombre del producto (ENTER para terminar): ").strip()
        if nombre == "":
            break
        coincidencias = sistema.obtener_producto_por_nombre(nombre)
        if not coincidencias:
            print("No se encontró ningún producto con ese nombre (o coincidencia parcial). Intenta de nuevo.")
            continue

        # Si hay varias coincidencias mostramos y pedimos elegir por id (solo en caso de ambigüedad)
        if len(coincidencias) > 1:
            print("Se encontraron varias coincidencias:")
            for p in coincidencias:
                print(p.descripcion())
            print("Por favor escribe el ID del producto que deseas comprar (se muestra aquí como ayuda).")
            pid = pedir_entero("ID del producto elegido: ")
            producto = sistema.obtener_producto(pid)
            if producto is None or producto not in coincidencias:
                print("Selección inválida. Línea omitida.")
                continue
        else:
            producto = coincidencias[0]

        print(producto.descripcion())
        cantidad = pedir_entero("Cantidad a comprar: ")
        lineas.append((producto.id, cantidad))

    if not lineas:
        print("Pedido vacío. Abortando.")
        return

    exito, total, mensajes = sistema.realizar_pedido(lineas)
    for m in mensajes:
        print(m)
    if exito:
        # Guardar cambios inmediatamente en JSON en la misma carpeta
        try:
            sistema.guardar_json(JSON_FILENAME)
            print(f"Stock actualizado y guardado en {JSON_FILENAME}.")
        except Exception as e:
            print("Pedido realizado, pero error al guardar JSON:", e)
        print(f"Pedido realizado correctamente. Total: ${total:.2f}")
    else:
        print("Pedido no realizado. Corrige errores e intenta de nuevo.")


def main():
    sistema = inicializar_demo()
    while True:
        mostrar_menu()
        opcion = pedir_entero("Selecciona una opción: ")
        try:
            if opcion == 1:
                print("\n--- Todos los productos ---")
                for desc in sistema.listar_todos():
                    print(desc)

            elif opcion == 2:
                print("\n--- Productos disponibles ---")
                for desc in sistema.listar_disponibles():
                    print(desc)

            elif opcion == 3:
                realizar_pedido_interactivo(sistema)

            elif opcion == 4:
                agregar_producto_interactivo(sistema)

            elif opcion == 5:
                try:
                    sistema.guardar_json(JSON_FILENAME)
                    print(f"Productos guardados en {JSON_FILENAME}.")
                except Exception as e:
                    print("Error al guardar JSON:", e)

            elif opcion == 6:
                try:
                    sistema.cargar_json(JSON_FILENAME)
                    print(f"Productos cargados desde {JSON_FILENAME}.")
                except Exception as e:
                    print("Error al cargar JSON:", e)

            elif opcion == 7:
                print("Saliendo. ¡Hasta luego!")
                break

            else:
                print("Opción no válida.")

        except Exception as e:
            print("Ocurrió un error:", e)


if __name__ == "__main__":
    main()
