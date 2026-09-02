'''
2. Widgets básicos

tkinter ofrece varios widgets que se pueden usar para diseñar la interfaz. Aquí
algunos de los más comunes:

Etiqueta (Label)
Se usa para mostrar texto o imágenes.

label = tk.Label(root, text = "¡Hola, tkinter! ", font=("Arial, 14"))
label.pack()
'''
import tkinter as tk


# Crear Ventana principal

root = tk.Tk()

# Dimensiones

ancho_ventana = 600
alto_ventana = 400

# Obtener info de la pantalla

ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

# Calcular posición x & y para centrar la ventana

pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

# Establecer ventana principal

root.title("Ventana Centrada")
root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

# Desactiva el redimensionamiento

root.resizable(False, False)

label = tk.Label(root, text = "¡Hola, tkinter! ", font=("Arial, 14"))
label.pack()

'''
Botón (Button)
Se usa para realizar acciones.
'''

def saludo():
    print("¡Botón presionado!")

button = tk.Button(root, text = "Presioname", command = saludo)
button.pack()

'''
Cuadro de texto (Entry)
Se usa para entradas de texto.
'''

entry = tk.Entry(root)
entry.pack()

'''
Caja de texto (Text)
Para texto más largo.
'''
text = tk.Text(root, height=5, width=30)
text.pack()


'''
Caja de selección (Checkbutton)
Permite seleccionar opciones.
'''
check_var = tk.BooleanVar()

checkbutton = tk.Checkbutton(root, text="Opción", variable=check_var)
checkbutton.pack()

# Ejecutar bucle principal

root.mainloop()