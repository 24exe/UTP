import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clínica - Sistema de Gestión")
        self.geometry("900x600")
        self.configure(bg="#f4f4f4")
        
        # Lista para almacenar pacientes (simulando una BD)
        self.patients = []

        # --- Crear layout principal ---
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

        # --- Barra lateral ---
        sidebar = tk.Frame(self, bg="#2c3e50", width=200)
        sidebar.grid(row=0, column=0, sticky="ns")
        sidebar.grid_propagate(False)

        tk.Label(sidebar, text="Menú", bg="#2c3e50", fg="white",
                 font=("Arial", 16)).pack(pady=20)

        # --- Función para crear botones ---
        def add_button(text, command):
            return tk.Button(
                sidebar,
                text=text,
                bg="#34495e",
                fg="white",
                font=("Arial", 12),
                relief="flat",
                padx=10,
                pady=10,
                command=command
            ).pack(fill="x", padx=10, pady=5)

        # --- Área principal que cambia ---
        self.main_area = tk.Frame(self, bg="white")
        self.main_area.grid(row=0, column=1, sticky="nsew")

        # --- Botones ---
        add_button("Agregar Paciente", self.show_add_patient_form)
        add_button("Actualizar Paciente", self.show_update_patient_form)
        add_button("Agregar Cita", lambda: self.clear_main("Agregar Cita"))
        add_button("Editar Cita", lambda: self.clear_main("Editar Cita"))
        add_button("Eliminar Cita", lambda: self.clear_main("Eliminar Cita"))
        add_button("Consultar Paciente", lambda: self.clear_main("Consultar Paciente"))
        add_button("Consultar Citas", lambda: self.clear_main("Consultar Citas"))
        add_button("Consultar Doctor", lambda: self.clear_main("Consultar Doctor"))

        # Bienvenida inicial
        self.clear_main("Bienvenido al sistema")

    # ----------------------------------------------------------
    # Función para limpiar el área principal
    # ----------------------------------------------------------
    def clear_main(self, title):
        for widget in self.main_area.winfo_children():
            widget.destroy()

        tk.Label(self.main_area, text=title, bg="white",
                 font=("Arial", 18)).pack(pady=20)

    # ----------------------------------------------------------
    # Vista: Formulario para agregar paciente
    # ----------------------------------------------------------
    def show_add_patient_form(self):
        # Limpiar área principal
        self.clear_main("Agregar Paciente")

        container = tk.Frame(self.main_area, bg="#e8e8e8")
        container.pack(fill="both", expand=True, pady=10, padx=10)

        # ------ Campos ------
        labels = ["Nombre", "Documento", "Edad", "Género", "Historial Médico"]

        self.entries = {}

        for label_text in labels:
            frame = tk.Frame(container, bg="#e8e8e8")
            frame.pack(anchor="w", pady=5, fill="x")

            label = tk.Label(frame, text=label_text, bg="#e8e8e8", font=("Arial", 12), width=15, anchor="w")
            label.pack(side="left", padx=(5, 10))

            if label_text == "Historial Médico":
                entry = tk.Text(frame, font=("Arial", 12), height=3)
                entry.pack(side="left", padx=5, fill="both", expand=True)
            else:
                entry = tk.Entry(frame, font=("Arial", 12))
                entry.pack(side="left", padx=5, fill="x", expand=True)

            self.entries[label_text] = entry

        # Guardar
        save_button = tk.Button(
            container,
            text="Guardar Paciente",
            bg="#27ae60",
            fg="white",
            font=("Arial", 12),
            padx=10,
            pady=5,
            command=self.save_patient
        )
        save_button.pack(pady=20)

    # ----------------------------------------------------------
    # Acción para guardar paciente (solo ejemplo)
    # ----------------------------------------------------------
    def save_patient(self):
        data = {}
        for key, entry in self.entries.items():
            if key == "Historial Médico":
                data[key] = entry.get("1.0", "end-1c")  # Para Text widget
            else:
                data[key] = entry.get()  # Para Entry widget

        # Agregar a la lista de pacientes
        self.patients.append(data)
        print("Paciente guardado:", data)

        self.clear_main("Paciente registrado correctamente")
    
    # ----------------------------------------------------------
    # Vista: Buscador para actualizar paciente
    # ----------------------------------------------------------
    def show_update_patient_form(self):
        self.clear_main("Actualizar Paciente")
        
        container = tk.Frame(self.main_area, bg="#e8e8e8")
        container.pack(fill="both", expand=True, pady=10, padx=10)
        
        # Frame para el buscador
        search_frame = tk.Frame(container, bg="#e8e8e8")
        search_frame.pack(fill="x", pady=(0, 20))
        
        tk.Label(search_frame, text="Buscar por Documento:", bg="#e8e8e8", 
                font=("Arial", 12)).pack(side="left", padx=5)
        
        self.search_entry = tk.Entry(search_frame, font=("Arial", 12))
        self.search_entry.pack(side="left", padx=5, fill="x", expand=True)
        
        search_button = tk.Button(
            search_frame,
            text="Buscar",
            bg="#3498db",
            fg="white",
            font=("Arial", 12),
            command=self.search_patient
        )
        search_button.pack(side="left", padx=5)
        
        # Frame para mostrar resultados
        self.result_frame = tk.Frame(container, bg="#e8e8e8")
        self.result_frame.pack(fill="both", expand=True)
    
    def search_patient(self):
        search_doc = self.search_entry.get().strip()
        
        # Limpiar frame de resultados
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        if not search_doc:
            tk.Label(self.result_frame, text="Por favor ingrese un documento", 
                    bg="#e8e8e8", fg="red", font=("Arial", 12)).pack(pady=10)
            return
        
        # Buscar paciente
        found_patient = None
        for patient in self.patients:
            if patient.get("Documento", "") == search_doc:
                found_patient = patient
                break
        
        if found_patient:
            self.show_edit_patient_form(found_patient)
        else:
            tk.Label(self.result_frame, text=f"No se encontró paciente con documento: {search_doc}", 
                    bg="#e8e8e8", fg="red", font=("Arial", 12)).pack(pady=10)
    
    def show_edit_patient_form(self, patient_data):
        # Limpiar frame de resultados
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        tk.Label(self.result_frame, text="Editar Información del Paciente", 
                bg="#e8e8e8", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Campos editables
        labels = ["Nombre", "Documento", "Edad", "Género", "Historial Médico"]
        self.edit_entries = {}
        
        for label_text in labels:
            frame = tk.Frame(self.result_frame, bg="#e8e8e8")
            frame.pack(anchor="w", pady=5, fill="x")
            
            label = tk.Label(frame, text=label_text, bg="#e8e8e8", font=("Arial", 12), 
                           width=15, anchor="w")
            label.pack(side="left", padx=(5, 10))
            
            if label_text == "Historial Médico":
                entry = tk.Text(frame, font=("Arial", 12), height=3)
                entry.insert("1.0", patient_data.get(label_text, ""))
                entry.pack(side="left", padx=5, fill="both", expand=True)
            else:
                entry = tk.Entry(frame, font=("Arial", 12))
                entry.insert(0, patient_data.get(label_text, ""))
                entry.pack(side="left", padx=5, fill="x", expand=True)
            
            self.edit_entries[label_text] = entry
        
        # Botones
        button_frame = tk.Frame(self.result_frame, bg="#e8e8e8")
        button_frame.pack(pady=20)
        
        update_button = tk.Button(
            button_frame,
            text="Actualizar Paciente",
            bg="#27ae60",
            fg="white",
            font=("Arial", 12),
            padx=10,
            pady=5,
            command=lambda: self.update_patient(patient_data)
        )
        update_button.pack(side="left", padx=5)
        
        cancel_button = tk.Button(
            button_frame,
            text="Cancelar",
            bg="#e74c3c",
            fg="white",
            font=("Arial", 12),
            padx=10,
            pady=5,
            command=self.show_update_patient_form
        )
        cancel_button.pack(side="left", padx=5)
    
    def update_patient(self, original_patient):
        # Obtener datos actualizados
        updated_data = {}
        for key, entry in self.edit_entries.items():
            if key == "Historial Médico":
                updated_data[key] = entry.get("1.0", "end-1c")
            else:
                updated_data[key] = entry.get()
        
        # Actualizar en la lista
        for i, patient in enumerate(self.patients):
            if patient == original_patient:
                self.patients[i] = updated_data
                break
        
        print("Paciente actualizado:", updated_data)
        self.clear_main("Paciente actualizado correctamente")


if __name__ == "__main__":
    app = App()
    app.mainloop()
