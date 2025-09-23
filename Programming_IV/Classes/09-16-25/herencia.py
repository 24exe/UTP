class Usuario:
    def __init__(self,nombre,cedula,edad):
        self.nombre=nombre
        self.cedula=cedula
        self.edad=edad
    def mostrar_datos(self):
        return f"nombre: {self.nombre} cedula: {self.cedula} edad: {self.edad}"
class Medico(Usuario):
    def __init__(self, nombre, cedula, edad,salario,experiencia,universidad):
        super().__init__(nombre, cedula, edad)
        self.salario=salario
        self.experiencia=experiencia
        self.universidad=universidad
    def Calcular_salario(self):
        pass
    def contrato(self):
        pass
    def mostrar_datos(self):
        return super().mostrar_datos()+f"salario: {self.salario} experiencia: {self.experiencia} universidad: {self.universidad}"
class Especialista(Medico):
    def __init__(self, nombre, cedula, edad, salario, experiencia, universidad,especialidad,residencia):
        super().__init__(nombre, cedula, edad, salario, experiencia, universidad)
        self.especialidad=especialidad
        self.residencia=residencia
class Enfermera(Usuario):
    def __init__(self, nombre, cedula, edad,salario, experiencia, universidad):
        super().__init__(nombre, cedula, edad)
        self.salario=salario
        self.experiencia=experiencia
        self.universidad=universidad
    def Calcular_salario(self):
        pass
    def contrato(self):
        pass
class Auxuliar(Enfermera):
    pass
pepito=Medico("pepito",85258,52,8525842,2,"utp")

print(pepito.mostrar_datos())