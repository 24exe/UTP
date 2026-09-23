from pymongo import MongoClient
# Poner Link a MongoDB dentro de las comillas
url =""

client = MongoClient(url)

db = client["Clinica"] 

coleccion = db["Doctores"]

docs = [
    {"Codigo": "12345678", "Nombre": "Michael Jackson", "Documento": "12345678", "Especialidad": "General", "Telefono": "555-1234", "Correo": "michael.jackson@example.com"},
    {"Codigo": "87654321", "Nombre": "Ibai Llanos", "Documento": "87654321", "Especialidad": "Cirugia", "Telefono": "555-5678", "Correo": "ibai.llanos@example.com"},
    {"Codigo": "11223344", "Nombre": "Juan Carlos Ozuna", "Documento": "11223344", "Especialidad": "General", "Telefono": "555-9101", "Correo": "juan.carlos.ozuna@example.com"},
    {"Codigo": "44332211", "Nombre": "Enrique Iglesias", "Documento": "44332211", "Especialidad": "Tricologo", "Telefono": "555-1121", "Correo": "enrique.iglesias@example.com"}
]





if coleccion.count_documents({}) == 0:
    coleccion.insert_many(docs)
    print("CONEXION EXITOSA")
else:
    print("CONEXION EXITOSA")
    print("Los documentos ya existen en la colección.")
