'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Archivos, clases y objetos.


TALLER 2


2. Conteo de palabras en frases
- Diseñe una clase `Frase` con atributos: texto y autor.
- Crea una lista de frases (una lista de objetos, cada objeto va a ser una instancia de la clase Frase).
- Implemente un método que cuente cuántas veces aparece una palabra clave en todas las frases.
- Guarde los resultados en `frases.txt`.
'''


from io import *
import os
import re


class Frase:
    texto: str
    autor: str

    def InsertTextAndAutor(self):
        while True:
            try:
                auxPhrase = str(input("Digite una frase cualquiera: ").strip())
                if not isinstance(auxPhrase, str):
                    raise TypeError ("EL ARGUMENTO DEBE SER UNA CADENA. ")
                if 0 <= len(auxPhrase) <= 100:
                     self.texto = auxPhrase
                     break
                else:
                     print("ERROR, DIGITE UNA FRASE NO MAYOR A 100 CARACTERES\n")
            except ValueError:
                print("ERROR, DATO INVALIDO")
        while True:
            try:
                auxAutor = str(input("Digite al autor de la frase: ").strip())
                if not isinstance(auxAutor, str):
                    raise TypeError ("EL ARGUMENTO DEBE SER UNA CADENA. ")
                if 0 <= len(auxAutor) <= 20:
                     self.autor = auxAutor
                     break
                else:
                     print("ERROR, EL AUTOR NO PUEDE SER MAYOR A 20 CARACTERES\n")
            except ValueError:
                print("ERROR, DATO INVALIDO")

    # Decidí hacerlo como metodo estático ya que trabaja sobre la clase y no objetos particulares
    @staticmethod
    def CountWordInPhrases(lista_de_frases: list, keyword: str):
        total: int = 0
        pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
        for phrase in lista_de_frases:
            total += len(re.findall(pattern, phrase.texto.lower()))
        return total

    @staticmethod
    def Results(lista_de_frases: list, keyword):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "frases.txt")
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("Listas de Frases: \n")
            for objeto in lista_de_frases:
                archivo.write(f"{objeto.texto} : {objeto.autor}\n")
            repeticiones = Frase.CountWordInPhrases(lista_de_frases, keyword)
            archivo.write(f"La frase {keyword} aparece en los textos {repeticiones} veces.")
        archivo.close()  


#-----------------------------------------------
n: int
while True:
    try:    
        num = int(input("¿Cuantas Frases desea Ingresar?: "))
        n = num
        break
    except (ValueError, TypeError):
        print("ERROR DE INSERCIÓN EN EL NÚMERO DE LISTAS, SE DARA UN TAMAÑO DE 4 POR DEFECTO. \n")
        n = 4
        break

lista_frases: list[Frase] = []

for i in range(n):
    print(f"\nFrase N° {i+1}. \n")
    frase = Frase()
    frase.InsertTextAndAutor()
    lista_frases.append(frase)

palabra = str(input("¿Qué palabra va a buscar en las frases?: "))

Frase.Results(lista_frases, palabra)
print("La información y resultados estan en el archivo frases.txt \n")

