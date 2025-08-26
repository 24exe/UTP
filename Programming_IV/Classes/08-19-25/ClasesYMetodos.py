class Automovil:
    marca=""
    color=""
    modelo=0
    placa=""
    def datos(self):
        
         return f" marca: {self.marca}\n color:{self.color}\n modelo:{self.modelo}\n placa:{self.placa}"
    
    def modificar(self,marca,color,modelo,placa):
         self.marca=marca
         self.color=color
         self.modelo=modelo
         self.placa=placa


onix=Automovil()
onix.datos()
onix.color="azul"
onix.marca="chevrolet"
onix.modelo=2025
onix.placa="asd123"
onix.datos()
onix.modificar("mazda","gris","2020","452df")
print(onix.datos())