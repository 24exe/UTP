#incluir el modulo para gestion de mongo
from pymongo import MongoClient

#incluir modulo para GUI
import tkinter as tk
from tkinter import messagebox

#configuración de conexión con atlas

# Poner Link a MongoDB dentro de las comillas
cliente=MongoClient("")

db=cliente["db_test"]
coleccion=db["estudiantes"]


def agregar_datos():
    
    nombre = entry_nombre.get()
    email = entry_email.get()
    edad=int(entry_edad.get())
    habilidades = entry_habilidades.get().split(",")

    if nombre and email and edad and habilidades:
        datos = {"nombre":nombre, "email":email, "edad": edad, "habilidades":habilidades}
        coleccion.insert_one(datos)
        messagebox.showinfo("Datos guardados con exito.")
    else:
        messagebox.showwarning("Por favor ingrese todos los campos.")

        
def buscar_usuario():
    nombre=entry_nombre.get()
    resultado=coleccion.find_one({"nombre":nombre})

    if resultado:
        entry_email.delete(0,tk.END)
        entry_edad.delete(0,tk.END)
        entry_habilidades.delete(0,tk.END)

        entry_email.insert(0,resultado["email"])
        entry_edad.insert(0,str(resultado["edad"]))
        entry_habilidades.insert(0, ", ".join(resultado["habilidades"]))
    else:
        messagebox.showinfo("No se encontraron datos para ese nombre.")


#configuracion de la ventana principal
ventana=tk.Tk()
ventana.title("Gestion de Usuario")
ventana.geometry("500x500")

#campos de entrada
tk.Label(ventana, text="Nombre: ").pack()
entry_nombre=tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Email: ").pack()
entry_email=tk.Entry(ventana)
entry_email.pack()

tk.Label(ventana, text="Edad: ").pack()
entry_edad=tk.Entry(ventana)
entry_edad.pack()

tk.Label(ventana, text="Habilidades: ").pack()
entry_habilidades=tk.Entry(ventana)
entry_habilidades.pack()

#agregar botones

tk.Button(ventana,text="Agregar usuario",command=agregar_datos).pack(pady=5)
tk.Button(ventana,text="Buscar usuario",command=buscar_usuario).pack(pady=5)


#ejecutar ventana
ventana.mainloop()
