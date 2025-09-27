class Padre1:
    def saludar(self):
        print("saludo desde la clase Padre1")
        super().saludar()

class Padre2:
    def saludar(self):
        print("saludo desde la clase Padre2")
        super().saludar()

class Padre3:
    def saludar(self):
        print("saludo desde la clase Padre3")

class Hija(Padre1,Padre2,Padre3):
    def saludar(self):
        print("saludo desde la clase Hija")
        super().saludar()

#hijas=Hija()
#hijas.saludar()
#help(hijas)
