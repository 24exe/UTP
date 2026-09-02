'''
Modulo 1.3: Final_Project.Clinica.Models.Pacientes
Descripción: Este módulo define la clase Pacientes
'''

from Persona import Persona
from Interfaces import Registrable
from Cita import Cita

from datetime import *

class Paciente(Persona, Registrable):
    def __init__(self, nombre: str, edad: int, fecha_ingreso: datetime|str|None = None, genero: str = "No especificado", historial_medico: str = "No se encontro historial medico"):
        super().__init__(nombre, edad, genero)

        if fecha_ingreso is None:
            fecha_ingreso = datetime.now()
        elif isinstance(fecha_ingreso, str):
            fecha_ingreso = self.convertir_a_fecha(fecha_ingreso)
        
        self._fecha_ingreso: datetime = fecha_ingreso
        self._historial_medico: str = historial_medico
        self._agenda_paciente: dict[datetime, Cita] = {}

    @property
    def historial_medico(self) -> str:
         return self._historial_medico
        
    @property
    def fecha_ingreso(self) -> datetime:
         return self._fecha_ingreso
        
    @property
    def agenda_paciente(self) -> dict[datetime, Cita]:
        return self._agenda_paciente
    
    @fecha_ingreso.setter
    def fecha_ingreso(self, fecha_ingreso: datetime):
        self._fecha_ingreso = fecha_ingreso
        
    @historial_medico.setter
    def historial_medico(self, historial_medico: str):
        self._historial_medico = historial_medico


    def convertir_a_fecha(self, fecha: str) -> datetime:
        '''
        Convierte una cadena en formato "YYYY-MM-DD HH:MM:SS" a un objeto date.
        Si ya es un objeto date, lo retorna tal cual.
        '''
        fecha_en_nuevo_formato = fecha.strip()
        return datetime.strptime(fecha_en_nuevo_formato, "%Y-%m-%d %H:%M:%S")
    

    def redondear_a_hora(self, fecha: datetime) -> datetime:
        """Redondea la fecha a la hora exacta (minutos y segundos = 0)"""
        if fecha.minute >= 30:
            return fecha.replace(hour=fecha.hour + 1, minute=0, second=0, microsecond=0)
        else:
            return fecha.replace(minute=0, second=0, microsecond=0)
    



    def registrar_cita_medica(self, fecha: datetime, cita: Cita) -> str:
        """Registra al paciente en la agenda con la fecha y el doctor proporcionados."""
        
        # Redondear a la hora exacta
        fecha_redondeada = self.redondear_a_hora(fecha)
        
        if fecha_redondeada in self._agenda_paciente.keys():
            return f"Error: El paciente {self.nombre} ya tiene una cita programada para el {fecha_redondeada.strftime('%Y-%m-%d %H:00')}."
        
        self._agenda_paciente[fecha_redondeada] = cita
        return f"Cita programada para el paciente {self.nombre}.\nEn la fecha: {fecha_redondeada.strftime('%Y-%m-%d %H:00')}.\nCon el Doctor: {cita.nombre_doctor}."
    




    def editar_cita_medica(self, nueva_fecha: datetime, nuevo_doctor: None|str) -> str:
        """Edita una cita médica existente del paciente."""
        
        # Redondear a la hora exacta
        nueva_fecha_redondeada = self.redondear_a_hora(nueva_fecha)
        
        if nueva_fecha_redondeada not in self._agenda_paciente.keys():
            return f"Error: No existe una cita programada para el paciente {self.nombre} en la fecha {nueva_fecha_redondeada.strftime('%Y-%m-%d %H:00')}."
        
        if nuevo_doctor is not None and nueva_fecha_redondeada in self._agenda_paciente.keys():
            self._agenda_paciente[nueva_fecha_redondeada] = nuevo_doctor
            return f"Cita editada para el paciente {self.nombre}.\nNueva fecha: {nueva_fecha_redondeada.strftime('%Y-%m-%d %H:00')}.\nNuevo Doctor: {nuevo_doctor.nombre}."
        
        return f"Cita editada para el paciente {self.nombre}.\nNueva fecha: {nueva_fecha_redondeada.strftime('%Y-%m-%d %H:00')}."




    def eliminar_cita_medica(self, fecha: datetime) -> str:
        """Elimina una cita médica existente del paciente."""
        
        # Redondear a la hora exacta
        fecha_redondeada = self.redondear_a_hora(fecha)
        
        if fecha_redondeada not in self._agenda_paciente.keys():
            return f"Error: No existe una cita programada para el paciente {self.nombre} en la fecha {fecha_redondeada.strftime('%Y-%m-%d %H:00')}."
        
        del self._agenda_paciente[fecha_redondeada]
        return f"Cita eliminada para el paciente {self.nombre} en la fecha {fecha_redondeada.strftime('%Y-%m-%d %H:00')}."
    
    def mostrar_agenda(self) -> str:
        """Muestra la agenda del paciente de forma legible"""
        if not self._agenda_paciente:
            return f" {self.nombre} no tiene citas programadas."
        
        resultado = f"Agenda de {self.nombre}:\n"
        resultado += "=" * 30 + "\n"
        
        # Ordenar por fecha
        agenda_ordenada = sorted(self._agenda_paciente.items())
        
        for fecha, cita in agenda_ordenada:
            fecha_formateada = fecha.strftime("%d/%m/%Y a las %H:%M")
            resultado += f"{fecha_formateada}\n"
            resultado += f"Doctor: {cita.nombre_doctor}\n"
            resultado += f"Licencia: {cita.id_doctor}\n"
            resultado += f"Paciente: {cita.nombre_paciente}\n"
            resultado += "-" * 30 + "\n"
        
        return resultado
    
    def __str__(self):
        return f"{super().__str__()}Fecha de Ingreso: {self.fecha_ingreso.strftime('%Y-%m-%d %H:%M:%S')}\nHistorial Médico: {self.historial_medico}\n"



# Test del módulo

if __name__ == "__main__":
    paciente1 = Paciente("Ana Gomez", 30, "2023-10-01 10:30:00", "Masculino", "No alergias conocidas.")
    cita1 = Cita("Dr. Juan Perez", "LIC12345", paciente1.nombre, paciente1.id)

    print(paciente1)
    print("\n")

    print(cita1)
    print("\n")

    # Registrar una cita
    resultado_registro = paciente1.registrar_cita_medica(datetime(2023, 10, 5, 14, 45), cita1)
    print(resultado_registro)
    print("\n")
    # Editar la cita (Error: No existe la cita)
    resultado_edicion = paciente1.editar_cita_medica(datetime(2023, 10, 6, 16, 0), None)
    print(resultado_edicion)    
    print("\n")

    # Editar la cita (Exito)
    resultado_edicion = paciente1.editar_cita_medica(datetime(2023, 10, 5, 15, 0), None)
    print(resultado_edicion)    
    print("\n")
    print(paciente1.mostrar_agenda())

    print("\n")
    # Eliminar la cita
    resultado_eliminacion = paciente1.eliminar_cita_medica(datetime(2023, 10, 5, 15, 0))
    print(resultado_eliminacion) 
    print(paciente1.agenda_paciente)
    print("\n")
    # Mostrar agenda
    print(paciente1.mostrar_agenda())

