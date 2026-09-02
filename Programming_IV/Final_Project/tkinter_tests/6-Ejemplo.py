import tkinter as tk

def mostrar_texto():
    texto = entry.get()
    label_resultado.config(text=f"Hola, {texto}!")

# Ventana principal
root = tk.Tk()
root.title("App de Ejemplo")

# Widgets
label = tk.Label(root, text="Introduce tu nombre:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Mostrar", command=mostrar_texto)
button.pack()

label_resultado = tk.Label(root, text="")
label_resultado.pack()

root.mainloop()