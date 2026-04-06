import json
import os
from libros import Libro
'''
1. Para este punto usted debe generar un archivo JSON para crear entidades “libros”, para
esto deberá realizar las siguientes actividades:
a. Revisar la documentación respecto al tema archivo JSON que se adjuntará en la
sección del “parcial II”.
b. Analizar y documentar el archivo llamado “generador”, este algoritmo genera
archivos JSON y tiene unos datos que no concuerdan con el contexto de libros,
cosa que ustedes deben arreglar.
c. Va a generar un nuevo algoritmo donde ustedes van a adaptar el paradigma
orientado a objetos a ese código “generador”, esto quiere decir que por ejemplo
en vez de dejarlo como funciones deben diseñar métodos y así para cubrir las
necesidades del código.
d. Después de adaptar el código deberá realizar métodos para que se puedan realizar
las siguientes funcionalidades de agregar libro por consola y lectura de datos, para
este punto debe modularizar el código.

'''
class Libreria:

    def __init__(self):
        self.libros: list[Libro] = []

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)
        self.libros.sort(key=lambda x: x.titulo.lower())  # Ordenar por título al agregar
    
    def comprobar_vacio(self) -> bool:
        return len(self.libros) == 0

    def mostrar_libros(self):
        if self.comprobar_vacio():
            print("\nNo hay libros en la librería.")
            return
        index: int = 1
        for libro in self.libros:
            print(f"Libro {index}: {libro}")
            index += 1
    def buscar_por_autor(self, autor: str):
        if self.comprobar_vacio():
            print("\nNo hay libros en la librería.")
            return
        index: int = 1
        resultados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if resultados:
            print(f"Libros encontrados del autor '{autor}':")
            for libro in resultados:
                print(f"Libro {index}: {libro}")
                index += 1
        else:
            print(f"No se encontraron libros del autor: {autor}")

    def guardar_en_archivo_json(self):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "libros.json")
        # Lista por comprension
        datos = [
            {
                "titulo": libro.titulo,
                "autor": libro.autor,
                "year": libro.year,
                "editorial": libro.editorial,
                "genero": libro.genero
            }
            for libro in self.libros
        ]
        try:
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo_json:
                json.dump(datos, archivo_json, indent=4, ensure_ascii=False)
            print("El archivo JSON se ha generado con éxito.")
        except Exception as e:
            print(f"Ocurrió un error al guardar el archivo JSON: {e}")
    
    def cargar_desde_archivo_json(self):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "libros.json")
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo_json:
                datos = json.load(archivo_json)
                for item in datos:
                    libro = Libro(
                        titulo=item.get("titulo", ""),
                        autor=item.get("autor", ""),
                        year=item.get("year", 0),
                        editorial=item.get("editorial", ""),
                        genero=item.get("genero", "")
                    )
                    self.agregar_libro(libro)
            print("\nLos libros se han cargado desde el archivo JSON con éxito.\n")
        except FileNotFoundError:
            print("\nEl archivo JSON no existe. No se cargaron libros.\n")
        except Exception as e:
            print(f"\nOcurrió un error al cargar el archivo JSON: {e}\n")



# Test del módulo
if __name__ == "__main__":
    libreria = Libreria()
    libreria.cargar_desde_archivo_json()
    libreria.mostrar_libros()