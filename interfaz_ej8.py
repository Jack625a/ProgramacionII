#Cuadro de seleccion con casillas de verificacion
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Paso2. Creacion de la clase de la aplicacion 
class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Componentes Avanzados")

        #Definir las variables de control (casillas de verificacion)
        self.variable1=tk.BooleanVar()
        self.variable2=tk.BooleanVar()
        self.variable3=tk.BooleanVar()
        self.variable4=tk.BooleanVar()
        self.mostrar=tk.BooleanVar(value=True)

        self.titulo=ttk.Label(ventana, text="Control de Componentes")
        self.titulo.pack(pady=8)

        #Crear las casillas de verificacion el interfaz
        self.casilla1=ttk.Checkbutton(ventana,text="Opcion 1", variable=self.variable1)
        self.casilla1.pack(pady=5)

        self.casilla2=ttk.Checkbutton(ventana,text="Opcion 2",variable=self.variable2)
        self.casilla2.pack(pady=5)

        self.casilla3=ttk.Checkbutton(ventana,text="Opcion 3", variable=self.variable3)
        self.casilla3.pack(pady=5)

        self.casilla4=ttk.Checkbutton(ventana,text="Opcion 4", variable=self.variable4)
        self.casilla4.pack(pady=5)

        #Boton para mostrar las opciones seleccionadas
        self.boton=ttk.Button(ventana,text="Mostrar Seleccion", command=self.mostrar_seleccion)
        self.boton.pack(pady=8)


    #Acciones o metodos de la clase
    def mostrar_seleccion(self):
        seleccionados=[]
        if self.variable1.get():
            seleccionados.append("Opcion 1")
        if self.variable2.get():
            seleccionados.append("Opcion 2")
        if self.variable3.get():
            seleccionados.append("Opcion 3")
        if self.variable4.get():
            seleccionados.append("Opcion 4")
        if self.mostrar.get():
            self.titulo.pack_forget()
        else:
            self.titulo.pack(pady=8)
        self.mostrar.set(not self.mostrar.get())
            


        mensaje="Seleccionados: "+",".join(seleccionados)
        messagebox.showinfo("Seleccion: ",mensaje)


ventana=tk.Tk()
app=App(ventana)
ventana.mainloop()       





