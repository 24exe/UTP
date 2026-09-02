import tkinter as tk
from tkinter import ttk, messagebox
from paciente import Paciente
from MongoDB import ingresar_dato, actualizar, obtener_todos, db, agregar_cita, eliminar
from GUICitas import Citas

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clínica - Sistema de Gestión")
        ancho_ventana = 900
        alto_ventana = 500

        # Obtener info de la pantalla

        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        # Calcular posición x & y para centrar la ventana

        pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

        # Establecer ventana principal

        self.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
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
        add_button("Agregar Paciente", self.show_add_patient_form) #
        add_button("Actualizar Paciente", self.show_update_patient_form) #
        add_button("Eliminar Paciente", self.show_delete_patient_form)
        add_button("Consultar Pacientes", self.show_consultar_pacientes) #
        add_button("Registrar Cita", self.open_citas) #
        #add_button("Editar Cita", lambda: self.clear_main("Editar Cita"))
        #add_button("Eliminar Cita", lambda: self.clear_main("Eliminar Cita")) #
        #add_button("Consultar Citas", lambda: self.clear_main("Consultar Citas"))
        add_button("Consultar Doctor", self.show_consultar_doctor) #
        add_button("Salir", self.quit) #

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
        try:
            nombre = self.entries["Nombre"].get()
            documento = int(self.entries["Documento"].get())
            edad = int(self.entries["Edad"].get())
            genero = self.entries["Género"].get()
            historial_medico = self.entries["Historial Médico"].get("1.0", "end-1c")

            paciente = Paciente(nombre, documento, edad, genero, historial_medico)
            self.patients.append(paciente)

            messagebox.showinfo("Éxito", f"Paciente registrado\nID: {paciente.id}")

            self.clear_main("Paciente registrado correctamente")

        except ValueError:
            messagebox.showerror("Error", "Documento y edad deben ser números.")
    
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

    # ----------------------------------------------------------
    # Vista: Formulario para eliminar paciente
    # ----------------------------------------------------------

    def show_delete_patient_form(self):
        self.clear_main("Eliminar Paciente")

        container = tk.Frame(self.main_area, bg="#e8e8e8")
        container.pack(fill="both", expand=True, pady=10, padx=10)

        tk.Label(container, text="Documento del Paciente:", bg="#e8e8e8", font=("Arial",12)).pack()
        self.doc_entry_del = tk.Entry(container, font=("Arial",12))
        self.doc_entry_del.pack(pady=5)

        tk.Button(
            container, text="Eliminar", bg="#c0392b", fg="white",
            font=("Arial",12), command=self.delete_patient
        ).pack(pady=10)

    def delete_patient(self):
        doc = self.doc_entry_del.get().strip()

        if not doc.isdigit():
            messagebox.showerror("Error", "Documento inválido")
            return

        ok = eliminar("Pacientes", {"documento": int(doc)})
        if ok:
            messagebox.showinfo("Éxito", "Paciente y citas eliminadas")
            self.clear_main("Paciente eliminado")

    # ----------------------------------------------------------
    
    def search_patient(self):
        documento = self.search_entry.get().strip()

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        if not documento.isdigit():
            tk.Label(
                self.result_frame, text="Documento inválido",
                bg="#e8e8e8", fg="red"
            ).pack(pady=10)
            return

        documento = int(documento)
        paciente = db["Pacientes"].find_one({"documento": documento})

        if paciente:
            self.show_edit_patient_form(paciente)
        else:
            tk.Label(
                self.result_frame, text="Paciente no encontrado",
                bg="#e8e8e8", fg="red"
            ).pack(pady=10)
    
    # ----------------------------------------------------------

    def show_edit_patient_form(self, patient_data):
        # Limpiar frame de resultados
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        tk.Label(self.result_frame, text="Editar Información del Paciente", 
                bg="#e8e8e8", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Campos editables
        labels = ["Nombre", "Edad", "Género", "Historial Médico"]
        self.edit_entries = {}
        
        for label_text in labels:
            frame = tk.Frame(self.result_frame, bg="#e8e8e8")
            frame.pack(anchor="w", pady=5, fill="x")
            
            label = tk.Label(frame, text=label_text, bg="#e8e8e8", font=("Arial", 12), 
                           width=15, anchor="w")
            label.pack(side="left", padx=(5, 10))
            
            if label_text == "Historial Médico":
                entry = tk.Text(frame, font=("Arial", 12), height=3)
                entry.insert("1.0", patient_data["historial_medico"])
                entry.pack(side="left", padx=5, fill="both", expand=True)
            else:
                entry = tk.Entry(frame, font=("Arial", 12))
                if label_text == "Nombre":
                    entry.insert(0, patient_data["nombre"])
                elif label_text == "Edad":
                    entry.insert(0, str(patient_data["edad"]))
                elif label_text == "Género":
                    entry.insert(0, patient_data["genero"])
                    
                entry.pack(side="left", padx=5, fill="x", expand=True)
            self.edit_entries[label_text] = entry
        tk.Button(
            self.result_frame, text="Actualizar",
            bg="#27ae60", fg="white",
            padx=10, pady=5,
            command=lambda: self.update_patient(patient_data)
        ).pack(pady=10)


    def update_patient(self, persona):
        nuevos = {
            "nombre": self.edit_entries["Nombre"].get(),
            "edad": int(self.edit_entries["Edad"].get()),
            "genero": self.edit_entries["Género"].get(),
            "historial_medico": self.edit_entries["Historial Médico"].get("1.0", "end-1c")
        }

        filtro = {"documento": persona["documento"]}
        actualizar("Pacientes", filtro, nuevos)

        messagebox.showinfo("Éxito", "Paciente actualizado")
        self.clear_main("Paciente actualizado correctamente")
    # ----------------------------------------------------------
    # Vista: Consultar Pacientes desde MongoDB
    # ----------------------------------------------------------
    def show_consultar_pacientes(self):
        # Limpiar pantalla
        self.clear_main("Consultar Pacientes")

        container = tk.Frame(self.main_area, bg="white")
        container.pack(fill="both", expand=True, padx=10, pady=10)

        # Obtener pacientes desde MongoDB
        try:
            pacientes = obtener_todos("Pacientes")
            print(f"Pacientes obtenidos: {len(pacientes)}")  # Debug
        except Exception as e:
            tk.Label(container, text=f"Error al obtener pacientes: {e}",
                    fg="red", bg="white", font=("Arial", 12)).pack(pady=10)
            return

        if not pacientes:
            tk.Label(container, text="No hay pacientes registrados.",
                    bg="white", font=("Arial", 12)).pack(pady=10)
            return

        # Frame para tabla y scrollbars
        table_frame = tk.Frame(container, bg="white")
        table_frame.pack(fill="both", expand=True)

        # --- Scrollbars ---
        scrollbar_y = tk.Scrollbar(table_frame, orient="vertical")
        scrollbar_x = tk.Scrollbar(table_frame, orient="horizontal")

        columnas = ("nombre", "documento", "edad", "genero", "historial_medico", "fecha_ingreso")

        tabla = ttk.Treeview(
            table_frame,
            columns=columnas,
            show="headings",
            height=15,
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        # Posicionar scrollbars
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")

        scrollbar_y.config(command=tabla.yview)
        scrollbar_x.config(command=tabla.xview)

        tabla.pack(fill="both", expand=True)

        # Encabezados
        tabla.heading("nombre", text="Nombre")
        tabla.heading("documento", text="Documento")
        tabla.heading("edad", text="Edad")
        tabla.heading("genero", text="Género")
        tabla.heading("historial_medico", text="Historial Médico")
        tabla.heading("fecha_ingreso", text="Fecha Ingreso")

        # Ajustar anchos de columnas
        tabla.column("nombre", width=200, anchor="center")
        tabla.column("documento", width=120, anchor="center")
        tabla.column("edad", width=80, anchor="center")
        tabla.column("genero", width=100, anchor="center")
        tabla.column("historial_medico", width=250, anchor="w")
        tabla.column("fecha_ingreso", width=150, anchor="center")

        # Insertar pacientes
        for paciente in pacientes:
            print(f"Insertando paciente: {paciente}")  # Debug
            
            # Formatear fecha de ingreso si existe
            fecha_ingreso = "N/A"
            if paciente.get("fecha_ingreso"):
                try:
                    fecha_obj = paciente.get("fecha_ingreso")
                    if hasattr(fecha_obj, 'strftime'):
                        fecha_ingreso = fecha_obj.strftime("%d/%m/%Y")
                    else:
                        fecha_ingreso = str(fecha_obj)
                except:
                    fecha_ingreso = "Error fecha"
            
            tabla.insert("", "end", values=(
                paciente.get("nombre", "N/A"),
                paciente.get("documento", "N/A"),
                paciente.get("edad", "N/A"),
                paciente.get("genero", "N/A"),
                paciente.get("historial_medico", "N/A")[:50] + "..." if len(str(paciente.get("historial_medico", ""))) > 50 else paciente.get("historial_medico", "N/A"),
                fecha_ingreso
            ))

        # Botones inferiores
        button_frame = tk.Frame(container, bg="white")
        button_frame.pack(pady=20)

        # Botón actualizar
        refresh_button = tk.Button(
            button_frame,
            text="Actualizar Lista",
            bg="#3498db",
            fg="white",
            font=("Arial", 12),
            command=self.show_consultar_pacientes
        )
        refresh_button.pack(side="left", padx=5)
    
    # ----------------------------------------------------------
    # Vista: Consultar Doctor desde MongoDB
    # ----------------------------------------------------------
    def show_consultar_doctor(self):
        # Limpiar pantalla
        self.clear_main("Consultar Doctor")

        container = tk.Frame(self.main_area, bg="white")
        container.pack(fill="both", expand=True, padx=10, pady=10)

        # Obtener doctores desde MongoDB
        try:
            doctores = obtener_todos("Doctores")
            print(f"Doctores obtenidos: {len(doctores)}")  # Debug
        except Exception as e:
            tk.Label(container, text=f"Error al obtener doctores: {e}",
                    fg="red", bg="white", font=("Arial", 12)).pack(pady=10)
            return

        if not doctores:
            tk.Label(container, text="No hay doctores registrados.",
                    bg="white", font=("Arial", 12)).pack(pady=10)
            return

        # Frame para tabla y scrollbars
        table_frame = tk.Frame(container, bg="white")
        table_frame.pack(fill="both", expand=True)

        # --- Scrollbars ---
        scrollbar_y = tk.Scrollbar(table_frame, orient="vertical")
        scrollbar_x = tk.Scrollbar(table_frame, orient="horizontal")

        columnas = ("nombre", "codigo", "documento", "especialidad", "telefono", "correo")

        tabla = ttk.Treeview(
            table_frame,
            columns=columnas,
            show="headings",
            height=15,
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        # Posicionar scrollbars
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")

        scrollbar_y.config(command=tabla.yview)
        scrollbar_x.config(command=tabla.xview)

        tabla.pack(fill="both", expand=True)

        # Encabezados
        tabla.heading("nombre", text="Nombre")
        tabla.heading("codigo", text="Código")
        tabla.heading("documento", text="Documento")
        tabla.heading("especialidad", text="Especialidad")
        tabla.heading("telefono", text="Teléfono")
        tabla.heading("correo", text="Correo")

        for col in columnas:
            tabla.column(col, width=150, anchor="center")

        # Insertar doctores
        for doc in doctores:
            print(f"Insertando doctor: {doc}")  # Debug
            tabla.insert("", "end", values=(
                doc.get("Nombre", "N/A"),
                doc.get("Codigo", "N/A"),
                doc.get("Documento", "N/A"),
                doc.get("Especialidad", "N/A"),
                doc.get("Telefono", "N/A"),
                doc.get("Correo", "N/A")
            ))

        # Botones inferiores
        button_frame = tk.Frame(container, bg="white")
        button_frame.pack(pady=20)

    def open_citas(self):
        ventana_citas = Citas(self)
        ventana_citas.grab_set()   # Bloquea la ventana principal hasta cerrar la de citas

        
       
if __name__ == "__main__":
    app = App()
    app.mainloop()
