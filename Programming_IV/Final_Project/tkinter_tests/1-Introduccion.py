'''
1. Introducción a tkinter
Para usar tkinter, necesitas importarla en tu script. El módulo principal se llama
tkinter, y puedes empezar creando una ventana principal (root):


# Crear Ventana principal

root = tk.Tk()

root.title("Mi primera GUI")
root.geometry("800x600")

# Ejecutar bucle principal

root.mainloop()
'''

'''
Establecer las medidas de la ventana principal
El formato básico para definir las medidas de la ventana con geometry() es:

root.geometry("anchoxalto+posX+posY")

• ancho: el ancho de la ventana en píxeles.
• alto: la altura de la ventana en píxeles.
• posX: posición horizontal de la ventana en la pantalla (opcional).
• posY: posición vertical de la ventana en la pantalla (opcional).

Posicionar la ventana en un lugar específico

También puedes controlar dónde aparece la ventana en la pantalla especificando
las coordenadas +posX+posY.

Ejemplo: Centrar la ventana

Para centrar la ventana, primero necesitas calcular las dimensiones de la pantalla
y restarlas del tamaño de tu ventana. Aquí tienes un ejemplo completo:
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

# Ejecutar bucle principal

root.mainloop()

'''
Hacer que la ventana no sea redimensionable

Si no deseas que el usuario pueda cambiar el tamaño de la ventana, puedes usar
el método resizable():

# Desactiva el redimensionamiento

root.resizable(False, False)
'''
