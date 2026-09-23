#incluir el modulo para gestion de mongo
from pymongo import MongoClient

#configuración de conexión con atlas

# Poner Link a MongoDB dentro de las comillas
cliente=MongoClient("")

db=cliente["db_test"]
coleccion=db["estudiantes"]

def eliminar_dato(nombre):
    resultado=coleccion.delete_one({"nombre":nombre})
    if resultado:
        print("Documento elminado.")
    else:
        print("no se encontro registro del usuario")
