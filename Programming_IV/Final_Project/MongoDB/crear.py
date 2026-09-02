#incluir el modulo para gestion de mongo
from pymongo import MongoClient

#configuración de conexión con atlas

cliente=MongoClient("mongodb+srv://Admin_Edu:fNO3Zkzwcawvrz5Q@prueba.0djpasi.mongodb.net/")

db=cliente["db_test"]
coleccion=db["estudiantes"]

def ingresar_dato():
    #datos usuario
    nombre=input("ingrese el nombre: ")
    edad=int(input("ingrese la edad: "))
    email=input("ingrese un email: ")

    habilidades=[]
    while True:
        habilidad=input("ingrese una habilidad o presione enter para terminar: ")
        if habilidad:
            habilidades.append(habilidad)
        else:
            break
    #documento basado en datos ingresados
    documento={
        "nombre":nombre,
        "edad":edad,
        "email":email,
        "habilidades":habilidades
    }

    #insertar documento en la coleccion
    coleccion.insert_one(documento)
    print("Datos Guardados")
