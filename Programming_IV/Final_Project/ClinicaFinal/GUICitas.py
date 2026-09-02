# INTERFAZ_CITAS.py
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from MongoDB import db, agregar_cita


class Citas(tk.Toplevel):   # ⬅ CAMBIO IMPORTANTE
    def __init__(self, parent=None):
        super().__init__(parent)

        self.title("Registro de Citas Médicas")
        self.geometry("600x500")
        self.configure(bg="#f4f4f4")

        tk.Label(self, text="Registrar Cita",
                 font=("Arial", 20), bg="#f4f4f4").pack(pady=20)

        container = tk.Frame(self, bg="#e8e8e8", padx=20, pady=20)
        container.pack(fill="both", expand=True)

        # === Paciente ===
        tk.Label(container, text="Documento del Paciente:",
                 bg="#e8e8e8").grid(row=0, column=0, sticky="w")
        self.doc_entry = tk.Entry(container, width=30)
        self.doc_entry.grid(row=0, column=1, pady=8)

        # === Doctor ===
        tk.Label(container, text="Doctor:",
                 bg="#e8e8e8").grid(row=1, column=0, sticky="w")

        self.combo_doctor = ttk.Combobox(container, width=30, state="readonly")
        self.combo_doctor.grid(row=1, column=1, pady=8)
        self.cargar_doctores()

        # === Fecha ===
        tk.Label(container, text="Fecha (YYYY-MM-DD):",
                 bg="#e8e8e8").grid(row=2, column=0, sticky="w")
        self.fecha_entry = tk.Entry(container, width=30)
        self.fecha_entry.grid(row=2, column=1, pady=8)

        # === Hora ===
        tk.Label(container, text="Hora (HH:MM):",
                 bg="#e8e8e8").grid(row=3, column=0, sticky="w")
        self.hora_entry = tk.Entry(container, width=30)
        self.hora_entry.grid(row=3, column=1, pady=8)

        # === Botón Guardar ===
        tk.Button(
            container,
            text="Registrar Cita",
            bg="#27ae60", fg="white",
            font=("Arial", 12),
            command=self.registrar_cita
        ).grid(row=4, column=0, columnspan=2, pady=20)

    # -------------------------------------------------------
    def cargar_doctores(self):
        try:
            doctores = db["Doctores"].find()
            lista = []

            for d in doctores:
                texto = f"{d['Codigo']} - {d['Nombre']} ({d['Especialidad']})"
                lista.append(texto)

            self.combo_doctor["values"] = lista

        except Exception as e:
            print("ERROR al cargar doctores:", e)

    # -------------------------------------------------------
    def registrar_cita(self):
        documento = self.doc_entry.get().strip()
        doctor_txt = self.combo_doctor.get().strip()
        fecha = self.fecha_entry.get().strip()
        hora = self.hora_entry.get().strip()

        # Validaciones
        if not documento.isdigit():
            messagebox.showerror("Error", "Documento debe ser numérico.")
            return

        if doctor_txt == "":
            messagebox.showerror("Error", "Debe seleccionar un doctor.")
            return

        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except:
            messagebox.showerror("Error", "Formato de fecha incorrecto.")
            return

        try:
            datetime.strptime(hora, "%H:%M")
        except:
            messagebox.showerror("Error", "Formato de hora incorrecto.")
            return

        codigo_doctor = int(doctor_txt.split(" - ")[0])

        nueva_cita = {
            "Paciente_documento": int(documento),
            "Doctor_codigo": codigo_doctor,
            "Fecha": fecha,
            "Hora": hora
        }

        ok, mensaje = agregar_cita(nueva_cita)

        if ok:
            messagebox.showinfo("Éxito", mensaje)
            self.limpiar()
        else:
            messagebox.showerror("Error", mensaje)

    # -------------------------------------------------------
    def limpiar(self):
        self.doc_entry.delete(0, tk.END)
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.combo_doctor.set("")
