class Animal:
    def __init__(self,nombre,eps):
        self.nombre=nombre
        self.eps=eps
    def comer(self):
        return f"{self.nombre} esta comiendo."
class Mascota:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def jugar(self):
        return f"{self.nombre} esta jugando."
    
class Perro(Animal,Mascota):
    def __init__(self, nombre, eps,raza,edad):
        Animal.__init__(self,nombre, eps)
        Mascota.__init__(self,nombre,edad)
        self.raza=raza

firulais=Perro("firulais","huellitas","criollo",3)