'''

que hace el argumento **kwargs? dame ejemplos

El argumento **kwargs permite recibir una cantidad variable de argumentos nombrados (clave-valor) en una función o método. 
Dentro de la función, kwargs es un diccionario con todos los argumentos que se pasaron por nombre.

'''

class Persona:
    def __init__(self, **kwargs):
        self.nombre = kwargs.get("nombre", "Sin nombre") # valores por defecto
        self.edad = kwargs.get("edad", 0)

p = Persona(nombre="Carlos", edad=20)
# kwargs = {"nombre": "Carlos", "edad": 20}

p2 = Persona()
# kwargs = {} (vacío, se usan los valores por defecto)

print(p2.nombre, p2.edad)
print(p.nombre, p.edad)

#------------------------ OTRO EJEMPLO ------------------------

def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="Pereira")
# Salida:
# nombre: Ana
# edad: 25
# ciudad: Pereira


