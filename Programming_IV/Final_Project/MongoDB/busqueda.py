#incluir el modulo para gestion de mongo
from pymongo import MongoClient

#configuración de conexión con atlas

# Poner Link a MongoDB dentro de las comillas
cliente=MongoClient("")

db=cliente["db_test"]
coleccion=db["estudiantes"]

def buscar_dato(nombre):
    resultado=coleccion.find_one({"nombre":nombre})
    if resultado:
        print("Documento encontrado: ",resultado)
    else:
        print("no se encontro registro del usuario")
