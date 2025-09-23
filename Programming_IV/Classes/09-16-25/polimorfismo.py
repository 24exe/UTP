class Animal:
    def hablar(self):
        return "este animal hace ruido no identificado"

class Gato(Animal):
    def hablar(self):
        return "Miauu"
class Perro(Animal):
    def hablar(self):
        return "Guau"
class Vaca(Animal):
    def hablar(self):
        return "Muu"
animales=[Gato(),Perro(),Vaca(),Animal()]

for i in animales:
    print(i.hablar())