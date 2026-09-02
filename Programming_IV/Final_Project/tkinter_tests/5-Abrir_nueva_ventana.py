import tkinter as tk

root = tk.Tk()
root.title("Ventana Principal")
root.geometry("300x200")


def abrir_nueva_ventana():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("200x150")
    etiqueta = tk.Label(nueva_ventana, text="¡Hola desde la nueva ventana!")
    etiqueta.pack(padx=20, pady=20)

boton_abrir = tk.Button(root, text="Abrir Nueva Ventana", command=abrir_nueva_ventana)
boton_abrir.pack(pady=50)

root.mainloop()