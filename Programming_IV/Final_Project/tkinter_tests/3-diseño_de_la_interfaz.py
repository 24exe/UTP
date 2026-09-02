'''
3. Diseño de la interfaz
tkinter ofrece tres métodos principales para organizar widgets:
1. pack(): Alinea widgets en la ventana.
2. grid(): Organiza widgets en una cuadrícula (recomendado para diseños
más complejos).
3. place(): Coloca widgets en posiciones absolutas.

El método pack() coloca los widgets uno debajo del otro (de manera
predeterminada) o uno al lado del otro, según el parámetro side.

import tkinter as tk

root = tk.Tk()

root.title("Ejemplo con pack()")

root.geometry("300x200")


# Crear widgets

label1 = tk.Label(root, text= "Arriba", bg="red", fg="black")
label2 = tk.Label(root, text= "Centro", bg="blue", fg="white")
label3 = tk.Label(root, text= "Abajo", bg="green", fg="white")

# Usar pack para alinearlos

label1.pack(side="top", fill="x")       # Ocupa el ancho completo arriba
label2.pack(expand=True)                # Centrado con expansión
label3.pack(side="left", fill="x")    # Ocupa el ancho completo abajo

root.mainloop()
'''



'''
El método grid() organiza widgets en una cuadrícula definida por filas y columnas.
Es más flexible para diseños complejos.

import tkinter as tk
root = tk.Tk()
root.title("Ejemplo con grid()")
root.geometry("300x200")

# Crear widgets
label1 = tk.Label(root, text="Usuario: ")
entry1 = tk.Entry(root)
label2 = tk.Label(root, text="Contraseña: ")
entry2 = tk.Entry(root, show="*")
button = tk.Button(root, text="Iniciar Sesión")

# Usar grid para organizarlos
label1.grid(row=0, column=0, padx=10, pady=10)
entry1.grid(row=0, column=1, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)
button.grid(row=2, column=0, columnspan=2, pady=10)     # Centrado en ambas columnas

root.mainloop()
'''

'''
El método place() permite colocar widgets en posiciones absolutas utilizando
coordenadas x e y.
'''

import tkinter as tk
root = tk.Tk()
root.title("Ejemplo con place()")
root.geometry("300x200")

# Crear widgets

label1 = tk.Label(root, text="Etiqueta 1", bg="red", fg="white")
label2 = tk.Label(root, text="Etiqueta 2", bg="blue", fg="white")
label3 = tk.Label(root, text="Etiqueta 3", bg="green", fg="white")

# Usar place para posicionarlos
label1.place(x=20, y=20)    # Posición absoluta en (20,20)
label2.place(x=100, y=80)   # Posición absoluta en (100,80)
label3.place(x=200, y=150)  # Posición absoluta en (200,150)

root.mainloop()


'''
Cuando usar cada método
• pack(): Ideal para disposiciones simples y alineaciones verticales u
horizontales.
• grid(): Perfecto para formularios o disposiciones tabulares.
• place(): Útil cuando necesitas control absoluto sobre las posiciones de los
widgets.
'''