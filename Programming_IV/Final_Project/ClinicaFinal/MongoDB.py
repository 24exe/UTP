from pymongo import MongoClient
from URL import url

cliente = MongoClient(url)
db = cliente["Clinica"]

db["Pacientes"].create_index("documento", unique=True)
db["Citas"].create_index(
    [("Doctor_codigo", 1), ("Fecha", 1), ("Hora", 1)],
    unique=True
)


# ======================================
# INSERTAR DOCUMENTO GENÉRICO
# ======================================
def ingresar_dato(nombre_coleccion: str, documento: dict):
    coleccion = db[nombre_coleccion]
    try:
        coleccion.insert_one(documento)
        print("Documento guardado:", documento)
    except Exception as e:
        print("Error al guardar:", e)

# ==============================================
# OBTENER TODOS LOS DOCUMENTOS DE UNA COLECCIÓN
# ==============================================

def obtener_todos(nombre_coleccion: str) -> list:
    """
    Obtiene todos los documentos de una colección usando
    la conexión fija definida arriba.

    Parameters:
        nombre_coleccion (str): Nombre de la colección

    Returns:
        list: Lista con todos los documentos de esa colección
    """
    coleccion = db[nombre_coleccion]
    documentos = list(coleccion.find())
    return documentos

# ======================================
# ACTUALIZAR DOCUMENTO
# ======================================

def actualizar(nombre_coleccion: str, filtro: dict, nuevos_valores: dict):
    coleccion = db[nombre_coleccion]
    update_query = {"$set": nuevos_valores}

    resultado = coleccion.update_one(filtro, update_query)

    if resultado.matched_count > 0:
        print("Documento actualizado correctamente")
    else:
        print("No se encontró ningún documento que coincida con el filtro")

# ======================================
# AGREGAR CITA (Validaciones completas)
# ======================================

def agregar_cita(documento: dict):
    """
    Documento esperado:
    {
        "Paciente_documento": int,
        "Doctor_codigo": int,
        "Fecha": "YYYY-MM-DD",
        "Hora": "HH:MM"
    }
    """

    pacientes_col = db["Pacientes"]
    doctores_col = db["Doctores"]
    citas_col = db["Citas"]

    # Verificar existencia de paciente
    paciente = pacientes_col.find_one({"documento": documento["Paciente_documento"]})
    if not paciente:
        return (False, "El paciente no existe en el sistema.")


    # Verificar disponibilidad
    existe = citas_col.find_one({
        "Doctor_codigo": documento["Doctor_codigo"],
        "Fecha": documento["Fecha"],
        "Hora": documento["Hora"]
    })

    if existe:
        return (False, "El doctor ya tiene una cita en esa fecha y hora.")

    # Guardar cita
    citas_col.insert_one(documento)
    return (True, "Cita registrada correctamente.")



# ==============================================
# ELIMINAR DOCUMENTO + Citas Asociadas
# =============================================
def eliminar(nombre_coleccion: str, filtro: dict):
    coleccion = db[nombre_coleccion]

    # Buscar documento antes de eliminar
    documento = coleccion.find_one(filtro)
    if not documento:
        print("No se encontró el documento a eliminar")
        return False

    # ELIMINAR DOCUMENTO PRINCIPAL
    resultado = coleccion.delete_one(filtro)

    if resultado.deleted_count > 0:
        print("Documento eliminado correctamente")

        # SI ES PERSONA → ELIMINAR CITAS POR PACIENTE
        if nombre_coleccion == "Pacientes":
            print("Eliminando citas del paciente:", documento["documento"])
            result = db["Citas"].delete_many({"Paciente_documento": documento["documento"]})
            print("Citas eliminadas:", result.deleted_count)

        return True

    else:
        print("No se logró eliminar el documento")
        return False

def eliminar_cita(documento, fecha, hora):
    try:
        resultado = db["Citas"].delete_one({
            "Paciente_documento": int(documento),
            "Fecha": fecha,
            "Hora": hora
        })
        if resultado.deleted_count > 0:
            return True, "Cita eliminada correctamente."
        else:
            return False, "No existe una cita con esos datos."
    except Exception as e:
        return False, f"Error eliminando cita: {e}"
