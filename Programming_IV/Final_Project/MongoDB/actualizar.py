#incluir el modulo para gestion de mongo
from pymongo import MongoClient

#configuración de conexión con atlas

cliente=MongoClient("mongodb+srv://Admin_Edu:fNO3Zkzwcawvrz5Q@prueba.0djpasi.mongodb.net/")

db=cliente["db_test"]
coleccion=db["estudiantes"]

def actualizar_datos(nombre,nuevo_email=None,nueva_edad=None,nuevas_habilidades=None):
    campos_actualizar={}

    if nuevo_email:
        campos_actualizar["email"]=nuevo_email
    if nueva_edad:
        campos_actualizar["edad"]=nueva_edad
    if nuevas_habilidades:
        campos_actualizar["habilidades"]=nuevas_habilidades
    if campos_actualizar:
        resultado=coleccion.update_one({"nombre":nombre},{"$set":campos_actualizar})
        if resultado.matched_count>0:
            print("documento actualizado")
        else:
            print("no se encontro documento a actualizar")
    