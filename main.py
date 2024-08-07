import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("Tareas app")
root.config(width=700, height=700)

class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        #self.estado = estado
def guardar_tarea():
    lista_tareas = []
    lista_tareas.append(tarea_user)

def ver_tarea():
    lista_tareas = Label(root, text=tarea_user.get(), padx=145, bg="green")
    lista_tareas.grid()


titulo = Label(root, text="Mis tareas", padx=145)
titulo.grid()  


nueva_tarea = Label(root, text="Añadir tarea", padx=145)
nueva_tarea.grid(row=2, column=2, padx=10, pady=10)

tarea_user = tk.Entry(root)
tarea_user.grid(row=3, column=2, padx=10, pady=10)

boton1 = Button(root, text="Guardar tarea", background="blue", padx=100, pady=5, command=guardar_tarea)
boton1.grid(row=4, column=2, padx=10, pady=10)

#Ver tareas
ver_tareas = Label(root, text="Ver tareas", padx=145)
ver_tareas.grid(row=2, column=5, padx=10, pady=10)

boton1 = Button(root, text="Ver tareas", background="green", padx=100, pady=5, command=ver_tarea)
boton1.grid(row=4, column=5, padx=10, pady=10)

root.mainloop()