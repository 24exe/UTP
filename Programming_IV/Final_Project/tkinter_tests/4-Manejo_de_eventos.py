import tkinter as tk

# Crear Ventana principal

root = tk.Tk()
import tkinter as tk
root = tk.Tk()
root.title("Eventos")
root.geometry("300x200")

def tecla_presionada(event):
    print(f"Tecla presionada: {event.char}")

button = tk.Button(root, text = "Presioname", command = lambda: print("¡Botón presionado!"))
button.pack()

text = tk.Text(root, height=5, width=30)
text.pack()

root.bind("<Key>", tecla_presionada)

root.mainloop()