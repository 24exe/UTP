class Libro:
    def __init__(self, titulo: str, autor: str, year: int, editorial: str, genero: str):
        self.titulo: str = titulo
        self.autor: str = autor
        self.year: int = year
        self.editorial: str = editorial
        self.genero: str = genero
    
    def __str__(self):
        return f"'{self.titulo}' de {self.autor} ({self.year}) - {self.editorial} [{self.genero}]"

if __name__ == "__main__":
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, "Editorial Sudamericana", "Realismo Mágico")
    libro2 = Libro("1984", "George Orwell", 1949, "Secker & Warburg", "Distopía")

    print(libro1)
    print(libro2)