#incluir el modulo para gestion de mongo
from pymongo import MongoClient

#configuración de conexión con atlas

cliente=MongoClient("mongodb+srv://Admin_Edu:fNO3Zkzwcawvrz5Q@prueba.0djpasi.mongodb.net/")

db=cliente["db_test"]
coleccion=db["estudiantes"]

def buscar_dato(nombre):
    resultado=coleccion.find_one({"nombre":nombre})
    if resultado:
        print("Documento encontrado: ",resultado)
    else:
        print("no se encontro registro del usuario")