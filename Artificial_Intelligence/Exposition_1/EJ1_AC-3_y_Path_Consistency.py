from collections import deque

# ============================================================
# CONTEXTO DEL PROBLEMA
# ============================================================
# Una universidad necesita organizar los horarios de tres materias:
#
#   Matemáticas < Programación < Física
#
# Cada materia inicialmente puede tener los horarios:
#   8, 10 o 12
#
# El objetivo es reducir las posibilidades imposibles utilizando
# técnicas de consistencia de CSP.
# ============================================================


# ============================================================
# VARIABLES Y DOMINIOS
# ============================================================

variables = ["Matematicas", "Programacion", "Fisica"]

domains = {
    "Matematicas": {8, 10, 12},
    "Programacion": {8, 10, 12},
    "Fisica": {8, 10, 12}
}


# ============================================================
# RESTRICCIONES
# ============================================================



constraints = {
    ("Matematicas", "Programacion"): lambda x, y: x < y,
    ("Programacion", "Matematicas"): lambda x, y: x > y,

    ("Programacion", "Fisica"): lambda x, y: x < y,
    ("Fisica", "Programacion"): lambda x, y: x > y
}


# ============================================================
# AC-3
# ============================================================

def revise(x, y):

    revised = False

    # Guardamos los valores que debemos eliminar.
    values_to_remove = set()

    for value_x in domains[x]:

        # Buscamos si existe AL MENOS un valor de Y
        # compatible con value_x.
        has_support = False

        for value_y in domains[y]:

            if constraints[(x, y)](value_x, value_y):
                has_support = True
                break

        # Si no existe ningún valor compatible,
        # value_x nunca podrá formar parte de una solución.
        if not has_support:
            values_to_remove.add(value_x)

    # Eliminamos los valores imposibles.
    for value in values_to_remove:
        domains[x].remove(value)
        revised = True

        print(
            f"AC-3 elimina {value} de {x} "
            f"porque no tiene soporte en {y}"
        )

    return revised


def ac3():

    # La cola contiene todos los arcos que debemos revisar.
    queue = deque(constraints.keys())

    while queue:

        x, y = queue.popleft()

        print(f"\nRevisando arco: {x} -> {y}")

        # Si modificamos el dominio de X...
        if revise(x, y):

            # Si el dominio queda vacío,
            # no existe solución bajo estas restricciones.
            if len(domains[x]) == 0:
                return False

            # Como X cambió, las variables que apuntan hacia X
            # deben revisarse nuevamente.
            for z in variables:

                if z != x and z != y:

                    if (z, x) in constraints:
                        queue.append((z, x))

    return True


# ============================================================
# EJECUTAMOS AC-3
# ============================================================

print("========== DOMINIOS INICIALES ==========")

for variable in variables:
    print(variable, ":", domains[variable])


print("\n========== EJECUTANDO AC-3 ==========")

result = ac3()


print("\n========== DOMINIOS DESPUÉS DE AC-3 ==========")

for variable in variables:
    print(variable, ":", domains[variable])


# ============================================================
# PATH CONSISTENCY
# ============================================================

def path_consistency_example():

    print("\n========== PATH CONSISTENCY ==========")

    A = "Matematicas"
    B = "Programacion"
    C = "Fisica"

    print(
        f"Comprobando la trayectoria: "
        f"{A} -> {B} -> {C}"
    )

    # Comprobamos cada combinación A-C.
    for value_a in domains[A]:

        for value_c in domains[C]:

            # Buscamos un valor intermedio de B
            # que permita cumplir ambas restricciones:
            #
            # A < B
            # B < C
            #
            # Por lo tanto necesitamos:
            #
            # A < B < C
            has_middle_value = False

            for value_b in domains[B]:

                if (
                    value_a < value_b
                    and value_b < value_c
                ):
                    has_middle_value = True
                    break

            if has_middle_value:

                print(
                    f"{value_a} -> {value_c}: compatible"
                )

            else:

                print(
                    f"{value_a} -> {value_c}: "
                    f"NO compatible"
                )


# Ejecutamos el ejemplo.
if result:
    path_consistency_example()
